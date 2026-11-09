---
symbol: "DDX28"
type: "gene"
col: 11329
ensembl_id: "ENSG00000182810"
name: "DEAD-box helicase 28"
location: "16q22.1"
module: 7
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DDX28

*DEAD-box helicase 28* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.58× (z +6.3, q 1e-07, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.16× (z +5.3, q 2e-05, up in 14 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0744×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPS6]] (+0.86, fdr 7e-06), [[MOCS3]] (+0.80, fdr 7e-06), [[JMJD4]] (+0.79, fdr 7e-06); moves opposite to [[MGAT4A]] (-0.66, fdr 1e-05), [[SEPTIN2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EID2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +6.3 | 1e-07 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +5.7 | 4e-06 | 2/10 (NCI-H1792, HEC-1-A) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +5.3 | 2e-05 | 14/27 (NCI-H2030, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +4.4 | 0.002 | 7/43 (NCI-H2030, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +4.3 | 0.002 | 17/43 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +4.1 | 0.003 | 4/11 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +3.9 | 0.008 | 1/2 (SW480) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +3.6 | 0.025 | 11/40 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.041 | 6/24 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.081 | 4/38 (A498, LoVo, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0744×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0744× (z -9.0) |
| [[A-172 (line)]] | wt | 0.914 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.873 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPS6]] | +0.86 | +0.76 / +0.85 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.80 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[JMJD4]] | +0.79 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[KTI12]] | +0.79 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.77 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.75 | +0.76 / +0.72 | both halves | 7e-06 | STRING 518 |
| [[CCDC137]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[RRN3]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[UTP3]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 | STRING 928 |
| [[TACO1]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 | STRING 535 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT4A]] | -0.66 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[SEPTIN2]] | -0.66 | -0.57 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2]] | C | EID2 activity raises DDX28's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-39.9, 9.1); signed map (-3.6, -25.7). **Vector** length 40.7, 4.79% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,020,916-68,023,232 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MDDX28, FLJ11282 |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUL7](https://www.uniprot.org/uniprotkb/Q9NUL7) (Probable ATP-dependent RNA helicase DDX28):

> Plays an essential role in facilitating the proper assembly of the mitochondrial large ribosomal subunit and its helicase activity is essential for this function. May be involved in RNA processing or transport. Has RNA and Mg(2+)-dependent ATPase activity.

**Summary**, from NCBI Gene [55794](https://www.ncbi.nlm.nih.gov/gene/55794):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of the DEAD box protein family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. …

**Accessions** — [HGNC:17330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17330) · Entrez [55794](https://www.ncbi.nlm.nih.gov/gene/55794) · UniProt [Q9NUL7](https://www.uniprot.org/uniprotkb/Q9NUL7) · Ensembl [ENSG00000182810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182810)

## Data

Gene col 11329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11329); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11329]; `tensor/DDL_lfc|DDL_z.npy` [11329]; `embed/gene_vectors.npy` [11329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11329 or target_col == 11329). Every well: [[DDX28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
