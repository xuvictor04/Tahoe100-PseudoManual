---
symbol: "COMMD6"
type: "gene"
col: 11994
ensembl_id: "ENSG00000188243"
name: "COMM domain containing 6"
location: "13q22.2"
module: 3
arm: "+"
pooled_cpm: 32.04
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# COMMD6

*COMM domain containing 6* — 13q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.24× (z +5.1, q 2e-04, up in 39 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.78× (z +3.8, q 0.019, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -6.2, q 4e-07, down in 40 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.258×, NCI-H460 0.345×); [[TAK-901 (drug)]] 0.05 µM in 1 line (AN3 CA 0.0595×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MJ]] (+0.89, fdr 7e-06), [[RPL36]] (+0.89, fdr 7e-06), [[RPS27]] (+0.88, fdr 7e-06); moves opposite to [[PSME3]] (-0.74, fdr 7e-06), [[HNRNPL]] (-0.73, fdr 7e-06), [[DARS2]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.24×** | +5.1 | 2e-04 | 39/44 (NCI-H1573, LS 180, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.08×** | +4.6 | 0.001 | 25/34 (NCI-H460, RPMI-7951, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.5 | 0.001 | 40/46 (SW1417, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.91×** | +4.2 | 0.003 | 35/45 (KATO III, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +3.8 | 0.019 | 39/48 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.70×** | +3.5 | 0.051 | 34/48 (A-172, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.088 | 31/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.61× | +3.1 | 0.13 | 31/47 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.59× | +3.0 | 0.16 | 27/48 (LoVo, A-172, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11994.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.258×, NCI-H460 0.345×); [[TAK-901 (drug)]] 0.05 µM in 1 line (AN3 CA 0.0595×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -6.2 | 4e-07 | 40/47 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.608× | -3.2 | 0.32 | 27/47 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.401× | -3.1 | 0.32 | 30/47 (NCI-H460, J82, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.629× | -3.0 | 0.32 | 30/48 (LOX-IMVI, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0595× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 50.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.9) |
| [[A-172 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MJ]] | +0.89 | +0.78 / +0.89 | both halves | 7e-06 |  |
| [[RPL36]] | +0.89 | +0.84 / +0.89 | both halves | 7e-06 |  |
| [[RPS27]] | +0.88 | +0.80 / +0.90 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.88 | +0.78 / +0.87 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | STRING 448 |
| [[RPL18]] ⚠ | +0.87 | +0.76 / +0.88 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.87 | +0.81 / +0.85 | both halves | 7e-06 | STRING 593 |
| [[RPL23]] | +0.86 | +0.76 / +0.87 | both halves | 7e-06 |  |
| [[RPS14]] | +0.86 | +0.76 / +0.86 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | STRING 418 |
| [[RPL36AL]] ⚠ | +0.85 | +0.74 / +0.88 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS19]] | +0.85 | +0.81 / +0.88 | both halves | 7e-06 |  |
| [[RPS29]] | +0.85 | +0.81 / +0.86 | both halves | 7e-06 | STRING 448 |
| [[LAMTOR5]] | +0.84 | +0.71 / +0.87 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.74 | -0.65 / -0.81 | both halves | 7e-06 |  |
| [[HNRNPL]] | -0.73 | -0.59 / -0.74 | both halves | 7e-06 |  |
| [[DARS2]] | -0.73 | -0.67 / -0.67 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.73 | -0.51 / -0.77 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers COMMD6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.839). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.4, -23.8); signed map (-32.4, 9.3). **Vector** length 79.4, 29.1% of its response variance represented; |z| ≥ 3 in 435 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.6 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -5.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -5.6 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.2 — chr13:75,525,214-75,549,439 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Acrg |
| Gene groups (HGNC) | COMM domain containing; CCC complex |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4G1](https://www.uniprot.org/uniprotkb/Q7Z4G1) (COMM domain-containing protein 6):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. Down-regulates activation of NF-kappa-B. Inhibits TNF-induced NFKB1 activation.

**Summary**, from NCBI Gene [170622](https://www.ncbi.nlm.nih.gov/gene/170622):

> COMMD6 belongs to a family of NF-kappa-B (see RELA; MIM 164014)-inhibiting proteins characterized by the presence of a COMM domain (see COMMD1; MIM 607238) (de Bie et al., 2006 [PubMed 16573520]).[supplied by OMIM, Mar 2009]

**Accessions** — [HGNC:24015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24015) · Entrez [170622](https://www.ncbi.nlm.nih.gov/gene/170622) · UniProt [Q7Z4G1](https://www.uniprot.org/uniprotkb/Q7Z4G1) · Ensembl [ENSG00000188243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188243)

## Data

Gene col 11994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11994); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11994]; `tensor/DDL_lfc|DDL_z.npy` [11994]; `embed/gene_vectors.npy` [11994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11994 or target_col == 11994). Every well: [[COMMD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
