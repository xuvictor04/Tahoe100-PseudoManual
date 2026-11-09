---
symbol: "YDJC"
type: "gene"
col: 8418
ensembl_id: "ENSG00000161179"
name: "YdjC chitooligosaccharide deacetylase homolog"
location: "22q11.21"
module: 1
arm: "+"
pooled_cpm: 6.03
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# YDJC

*YdjC chitooligosaccharide deacetylase homolog* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.74× (z +4.6, q 0.003, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.449× (z -6.7, q 2e-08, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMP4]] (+0.70, fdr 7e-06), [[NOB1]] (+0.68, fdr 7e-06), [[MRPL15]] (+0.68, fdr 7e-06); moves opposite to [[PRKACA]] (-0.61, fdr 2e-05), [[APLP2]] (-0.56, fdr 1e-05), [[AP2A1]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +4.6 | 0.003 | 21/44 (Panc 03.27, J82, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.2 | 0.007 | 15/30 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.1 | 0.007 | 11/24 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.0 | 0.009 | 4/14 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.9 | 0.011 | 12/29 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.449×** | -6.7 | 2e-08 | 29/45 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.503×** | -5.7 | 3e-06 | 25/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -4.7 | 5e-04 | 19/43 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -4.4 | 0.001 | 15/36 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.619×** | -4.0 | 0.007 | 20/44 (KATO III, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.635×** | -3.8 | 0.013 | 21/44 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.636×** | -3.8 | 0.013 | 20/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.657×** | -3.5 | 0.032 | 17/41 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.33 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -9.9) |
| [[COLO 205 (line)]] | alt | 5.91 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0592× (z -8.9) |
| [[LoVo (line)]] | wt | 7.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.1) |
| [[LS 180 (line)]] | wt | 6.29 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0754× (z -10.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.17 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SNU-423 (line)]] | alt | 4.55 | 0 | 1 | — | [[Hydroxyurea (drug)]] 5 µM 0.0449× (z -9.9) |
| [[A-172 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMP4]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[NOB1]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[COA4]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.65 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[RDH14]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[NIFK]] | +0.64 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[NDUFAF4]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[RPP25]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ZNF639]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RPP38]] | +0.63 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKACA]] | -0.61 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[APLP2]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[AP2A1]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[TMA7]] | -0.55 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[NPTN]] | -0.53 | -0.59 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises YDJC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.8, -7.4); signed map (-3.2, -36.7). **Vector** length 58.6, 9.82% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.5 | +1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.7 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.1 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | YdjC chitooligosaccharide deacetylase homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:21,628,089-21,630,064 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MPS7](https://www.uniprot.org/uniprotkb/A8MPS7) (Carbohydrate deacetylase):

> Probably catalyzes the deacetylation of acetylated carbohydrates an important step in the degradation of oligosaccharides.

**Summary**, from NCBI Gene [150223](https://www.ncbi.nlm.nih.gov/gene/150223):

> Predicted to enable deacetylase activity and magnesium ion binding activity. Predicted to be involved in carbohydrate metabolic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27158) · Entrez [150223](https://www.ncbi.nlm.nih.gov/gene/150223) · UniProt [A8MPS7](https://www.uniprot.org/uniprotkb/A8MPS7) · Ensembl [ENSG00000161179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161179)

## Data

Gene col 8418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8418); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8418]; `tensor/DDL_lfc|DDL_z.npy` [8418]; `embed/gene_vectors.npy` [8418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8418 or target_col == 8418). Every well: [[YDJC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YDJC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
