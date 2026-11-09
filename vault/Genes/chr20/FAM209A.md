---
symbol: "FAM209A"
type: "gene"
col: 4478
ensembl_id: "ENSG00000124103"
name: "family with sequence similarity 209 member A"
location: "20q13.31"
module: 38
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# FAM209A

*family with sequence similarity 209 member A* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +13.6, q 2e-39, up in 30 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.636× (z -5.0, q 4e-04, down in 17 of 43 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 0.05 µM: 0.690× (z -4.0, q 0.017, down in 8 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0901×; ⚠ toxic); [[Naproxen (drug)]] 5 µM in 1 line (HOP62 0.0681×); [[Menadione (drug)]] 0.05 µM in 1 line (NCI-H2030 0.102×); [[Radotinib (drug)]] 0.5 µM in 1 line (LoVo 0.0756×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISY1-RAB43]] (+0.83, fdr 7e-06), [[RRH]] (+0.78, fdr 7e-06), [[CD200R1]] (+0.77, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C5AR1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +13.6 | 2e-39 | 30/36 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +10.0 | 6e-21 | 21/36 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.21×** | +9.0 | 6e-17 | 24/43 (NCI-H23, BT-474, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +7.8 | 1e-12 | 18/34 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +6.3 | 5e-08 | 18/46 (SW1417, HOP62, …) | rises with dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.7 | 1e-06 | 9/19 (SW480, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.6 | 2e-06 | 16/46 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +4.7 | 2e-04 | 12/47 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.7 | 2e-04 | 5/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.004 | 4/40 (RKO, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.94×** | +3.9 | 0.005 | 1/43 (Hs 766T) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.005 | 7/34 (RKO, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +3.5 | 0.022 | 5/42 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.063 | 4/44 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.1 | 0.073 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.097 | 1/47 (SW480) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4478.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0901×; ⚠ toxic); [[Naproxen (drug)]] 5 µM in 1 line (HOP62 0.0681×); [[Menadione (drug)]] 0.05 µM in 1 line (NCI-H2030 0.102×); [[Radotinib (drug)]] 0.5 µM in 1 line (LoVo 0.0756×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.636×** | -5.0 | 4e-04 | 17/43 (LOX-IMVI, CFPAC-1, …) | rises with dose | composition shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.690×** | -4.0 | 0.017 | 8/41 (NCI-H23, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.715×** | -3.7 | 0.042 | 13/41 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 2.81 | 0 | 3 | — | [[Radotinib (drug)]] 0.5 µM 0.0756× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 5.60 | 0 | 2 (1 ⚠) | — | [[Menadione (drug)]] 0.05 µM 0.102× (z -9.2) |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0901× (z -10.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 3.15 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0681× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 2.26 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[A-172 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISY1-RAB43]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[RRH]] | +0.78 | +0.71 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CD200R1]] | +0.77 | +0.79 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ARL9]] | +0.77 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.74 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.73 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.73 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[LINC00672]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.70 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.70 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C5AR1]] | C | C5AR1 activity raises FAM209A's level | lines that do not express C5AR1 (3) vs lines expressing it (47) | 1.24× lower at baseline in the lines without C5AR1 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FARP1, PER3, NECAB2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.9, -17.7); signed map (13.5, 7.9). **Vector** length 52.8, 6.12% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +13.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.0 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 209 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:56,517,187-56,526,152 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1153D9.3; previously C20orf106 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JX71](https://www.uniprot.org/uniprotkb/Q5JX71) (Protein FAM209A):

> May play a role in sperm acrosome biogenesis.

**Summary**, from NCBI Gene [200232](https://www.ncbi.nlm.nih.gov/gene/200232):

> Predicted to be involved in cell differentiation and spermatogenesis. Located in extracellular exosome and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16100) · Entrez [200232](https://www.ncbi.nlm.nih.gov/gene/200232) · UniProt [Q5JX71](https://www.uniprot.org/uniprotkb/Q5JX71) · Ensembl [ENSG00000124103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124103)

## Data

Gene col 4478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4478); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4478]; `tensor/DDL_lfc|DDL_z.npy` [4478]; `embed/gene_vectors.npy` [4478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4478 or target_col == 4478). Every well: [[FAM209A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM209A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
