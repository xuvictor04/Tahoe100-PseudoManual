---
symbol: "TMEM179B"
type: "gene"
col: 11681
ensembl_id: "ENSG00000185475"
name: "transmembrane protein 179B"
location: "11q12.3"
module: 58
arm: "+"
pooled_cpm: 10.28
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# TMEM179B

*transmembrane protein 179B* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +9.4, q 3e-18, up in 29 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.11× (z +6.5, q 2e-08, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.681× (z -4.7, q 0.001, down in 22 of 43 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC5]] (+0.64, fdr 2e-05), [[MRPL40]] (+0.60, fdr 4e-05), [[HINT2]] (+0.58, fdr 3e-05); moves opposite to [[LINC01355]] (-0.53, fdr 2e-04), [[LY6G5B]] (-0.53, fdr 6e-05), [[ING5]] (-0.52, fdr 4e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.94×** | +9.4 | 3e-18 | 29/34 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.48×** | +7.6 | 7e-12 | 15/21 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +6.5 | 2e-08 | 35/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +5.9 | 4e-07 | 35/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +5.1 | 4e-05 | 30/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.79×** | +4.7 | 3e-04 | 21/29 (NCI-H1573, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.59×** | +4.1 | 0.004 | 18/42 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.6 | 0.025 | 18/39 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.031 | 13/48 (Hs 766T, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11681.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.681×** | -4.7 | 0.001 | 22/43 (SK-MEL-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.387×** | -4.3 | 0.003 | 26/43 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.609×** | -4.3 | 0.003 | 26/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.592×** | -4.2 | 0.004 | 25/47 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.657×** | -3.7 | 0.029 | 16/47 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.667×** | -3.5 | 0.040 | 17/45 (LoVo, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.679×** | -3.4 | 0.061 | 18/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -8.7) |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0880× (z -8.5) |
| [[LoVo (line)]] | wt | 10.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 7.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.0) |
| [[A-172 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 14 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC5]] | +0.64 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[MRPL40]] | +0.60 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[HINT2]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[MIEN1]] | +0.57 | +0.28 / +0.65 | both halves | 3e-04 |  |
| [[LAMTOR2]] | +0.56 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[PSENEN]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ISCA2]] | +0.56 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[MRTFA]] | +0.55 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[RNF114]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[LAGE3]] | +0.54 | +0.24 / +0.61 | both halves | 5e-04 |  |
| [[NDUFAF3]] | +0.53 | +0.27 / +0.65 | both halves | 3e-04 |  |
| [[ANTKMT]] | +0.53 | +0.23 / +0.55 | both halves | 5e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01355]] | -0.53 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[LY6G5B]] | -0.53 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ING5]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[SMG1P6]] | -0.52 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[U2AF2]] | -0.51 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[GCN1]] | -0.51 | -0.51 / -0.55 | both halves | 1e-05 | same gene group |
| [[EOGT]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ILF3]] | -0.50 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[KLRA1P]] | -0.50 | -0.19 / -0.46 | ⚠ not reproduced | 9e-04 |  |
| [[DHX38]] | -0.49 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[MTA1]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[YJEFN3]] | -0.49 | -0.19 / -0.36 | ⚠ not reproduced | 8e-04 |  |
| [[CCDC18]] | -0.49 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[SLC9A5]] | -0.49 | -0.28 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TMEM179B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.7, -11.9); signed map (-20.9, -3.7). **Vector** length 50.3, 8.09% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.7 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 179B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,787,402-62,790,400 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [Q7Z7N9](https://www.uniprot.org/uniprotkb/Q7Z7N9) carries no function annotation.

**Summary**, from NCBI Gene [374395](https://www.ncbi.nlm.nih.gov/gene/374395):

> Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33744) · Entrez [374395](https://www.ncbi.nlm.nih.gov/gene/374395) · UniProt [Q7Z7N9](https://www.uniprot.org/uniprotkb/Q7Z7N9) · Ensembl [ENSG00000185475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185475)

## Data

Gene col 11681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11681); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11681]; `tensor/DDL_lfc|DDL_z.npy` [11681]; `embed/gene_vectors.npy` [11681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11681 or target_col == 11681). Every well: [[TMEM179B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM179B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
