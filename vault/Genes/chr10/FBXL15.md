---
symbol: "FBXL15"
type: "gene"
col: 2892
ensembl_id: "ENSG00000107872"
name: "F-box and leucine rich repeat protein 15"
location: "10q24.32"
module: 24
arm: "+"
pooled_cpm: 4.54
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# FBXL15

*F-box and leucine rich repeat protein 15* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.96× (z +10.2, q 8e-22, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.565× (z -3.8, q 0.076, down in 19 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.104×, NCI-H2030 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.0773×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG9]] (+0.73, fdr 1e-05), [[DCXR]] (+0.70, fdr 7e-06), [[TMEM134]] (+0.69, fdr 6e-05); moves opposite to [[EFTUD2]] (-0.65, fdr 1e-05), [[NONO]] (-0.61, fdr 7e-05), [[SFPQ]] (-0.61, fdr 3e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +10.2 | 8e-22 | 40/41 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.75×** | +5.3 | 4e-05 | 20/38 (NCI-H460, HOP62, …) | top dose only | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.15×** | +5.1 | 6e-05 | 18/30 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.6 | 7e-04 | 17/27 (SW 900, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.3 | 0.085 | 13/37 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.10×** | +3.3 | 0.085 | 8/41 (NCI-H460, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +3.3 | 0.088 | 14/34 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | 1.38× | +3.0 | 0.16 | 8/45 (NCI-H2347, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2892.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.104×, NCI-H2030 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.0773×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -3.8 | 0.076 | 19/45 (C-33 A, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.634× | -3.1 | 0.50 | 17/44 (NCI-H23, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 7.69 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0773× (z -10.0) |
| [[HOP62 (line)]] | alt | 3.07 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +9.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.94 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +10.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW1417 (line)]] | alt | 9.09 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[A-172 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | +0.73 | +0.54 / +0.80 | both halves | 1e-05 |  |
| [[DCXR]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[TMEM134]] | +0.69 | +0.38 / +0.78 | both halves | 6e-05 |  |
| [[POLR1H]] | +0.69 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[SMIM27]] | +0.67 | +0.43 / +0.72 | both halves | 3e-05 |  |
| [[SELENOM]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[CDK7]] | +0.66 | +0.40 / +0.74 | both halves | 4e-05 |  |
| [[ICAM3]] | +0.65 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[TRIM52-AS1]] | +0.65 | +0.32 / +0.73 | both halves | 2e-04 |  |
| [[MPLKIP]] | +0.64 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[RNF7]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.65 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[NONO]] | -0.61 | -0.38 / -0.68 | both halves | 7e-05 |  |
| [[SFPQ]] | -0.61 | -0.28 / -0.73 | both halves | 3e-04 |  |
| [[PABIR2]] | -0.60 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.60 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[API5]] | -0.59 | -0.21 / -0.71 | both halves | 7e-04 |  |
| [[TARDBP]] | -0.59 | -0.45 / -0.72 | both halves | 3e-05 |  |
| [[LAS1L]] | -0.59 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[XRCC5]] | -0.58 | -0.39 / -0.69 | both halves | 6e-05 |  |
| [[NUP155]] | -0.58 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[ADAMTSL5]] | -0.58 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[MAPK9]] | -0.57 | -0.35 / -0.63 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FBXL15's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.0, -20.2); signed map (-12.5, 0.4). **Vector** length 67.4, 13.5% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.1 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +0.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | -4.1 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,419,189-102,423,136 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11279, Fbl15; previously FBXO37 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H469](https://www.uniprot.org/uniprotkb/Q9H469) (F-box/LRR-repeat protein 15):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of SMURF1, thereby acting as a positive regulator of the BMP signaling pathway. Required for dorsal/ventral pattern formation and bone mass maintenance. Also mediates ubiquitination of SMURF2 and WWP2.

**Summary**, from NCBI Gene [79176](https://www.ncbi.nlm.nih.gov/gene/79176):

> Involved in several processes, including G2/M transition of mitotic cell cycle; SCF-dependent proteasomal ubiquitin-dependent protein catabolic process; and positive regulation of BMP signaling pathway. Located in cytoplasm. Part of SCF ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28155) · Entrez [79176](https://www.ncbi.nlm.nih.gov/gene/79176) · UniProt [Q9H469](https://www.uniprot.org/uniprotkb/Q9H469) · Ensembl [ENSG00000107872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107872)

## Data

Gene col 2892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2892); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2892]; `tensor/DDL_lfc|DDL_z.npy` [2892]; `embed/gene_vectors.npy` [2892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2892 or target_col == 2892). Every well: [[FBXL15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
