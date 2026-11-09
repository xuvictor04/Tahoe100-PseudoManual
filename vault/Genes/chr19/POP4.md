---
symbol: "POP4"
type: "gene"
col: 2553
ensembl_id: "ENSG00000105171"
name: "POP4 ribonuclease P/MRP subunit"
location: "19q12"
module: 7
arm: "+"
pooled_cpm: 10.24
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# POP4

*POP4 ribonuclease P/MRP subunit* — 19q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.85× (z +6.1, q 5e-07, up in 31 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vandetanib (drug)]] 0.5 µM in 1 line (BT-474 0.0890×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.144×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC8]] (+0.74, fdr 7e-06), [[ZNF513]] (+0.74, fdr 7e-06), [[MRM3]] (+0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF613]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +6.1 | 5e-07 | 31/46 (HOP62, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.83×** | +6.0 | 5e-07 | 19/33 (A498, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.90×** | +5.9 | 8e-07 | 21/27 (LoVo, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.84×** | +5.8 | 8e-07 | 13/20 (HEC-1-A, CFPAC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.73×** | +5.4 | 6e-06 | 26/42 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +5.4 | 7e-06 | 30/41 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +5.3 | 1e-05 | 27/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.2 | 1e-05 | 21/47 (CFPAC-1, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.61×** | +4.5 | 3e-04 | 21/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.55×** | +4.4 | 7e-04 | 21/47 (HOP62, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.51×** | +4.1 | 0.002 | 17/47 (HOP62, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.002 | 21/46 (HOP62, HT-29, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.34×** | +3.9 | 0.004 | 15/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 14/48 (PANC-1, A498, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.0 | 0.095 | 2/48 (NCI-H661, SW 1088) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2553.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vandetanib (drug)]] 0.5 µM in 1 line (BT-474 0.0890×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.144×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.693× | -3.6 | 0.11 | 22/47 (SW 900, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.700× | -3.5 | 0.11 | 17/45 (Panc 03.27, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~16% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.709× | -3.3 | 0.20 | 18/45 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 6.74 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0890× (z -8.6) |
| [[RKO (line)]] | wt | 11.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -8.5) |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC8]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ZNF513]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MRM3]] | +0.73 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.72 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.70 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[LLPH]] | +0.70 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.70 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[KTI12]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.69 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.69 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[TIMM22]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MRPS18A]] | +0.68 | +0.72 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF613]] | B | ZNF613 activity raises POP4's level | lines that do not express ZNF613 (7) vs lines expressing it (43) | 1.03× lower at baseline in the lines without ZNF613 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF850, ENSG00000283201, ZNF571 |
| [[ZNF813]] | B | ZNF813 activity raises POP4's level | lines that do not express ZNF813 (14) vs lines expressing it (36) | 1.08× lower at baseline in the lines without ZNF813 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF256, ZNF331, ZNF625; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.7, 9.3); signed map (-3.1, -24.8). **Vector** length 64.3, 12.0% of its response variance represented; |z| ≥ 3 in 631 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | POP4 ribonuclease P/MRP subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q12 — chr19:29,606,283-29,617,237 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPP29 |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O95707](https://www.uniprot.org/uniprotkb/O95707) (Ribonuclease P protein subunit p29):

> Component of ribonuclease P, a ribonucleoprotein complex that generates mature tRNA molecules by cleaving their 5'-ends.

**Summary**, from NCBI Gene [10775](https://www.ncbi.nlm.nih.gov/gene/10775):

> This gene encodes one of the protein subunits of the small nucleolar ribonucleoprotein complexes: the endoribonuclease for mitochondrial RNA processing complex and the ribonuclease P complex. The encoded protein is localized to the nucleus and associates directly with the RNA component of these complexes. This protein is involved in processing of precursor RNAs. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:30081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30081) · Entrez [10775](https://www.ncbi.nlm.nih.gov/gene/10775) · UniProt [O95707](https://www.uniprot.org/uniprotkb/O95707) · Ensembl [ENSG00000105171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105171)

## Data

Gene col 2553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2553); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2553]; `tensor/DDL_lfc|DDL_z.npy` [2553]; `embed/gene_vectors.npy` [2553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2553 or target_col == 2553). Every well: [[POP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
