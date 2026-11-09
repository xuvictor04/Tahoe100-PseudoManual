---
symbol: "PTCHD1"
type: "gene"
col: 9083
ensembl_id: "ENSG00000165186"
name: "patched domain containing 1"
location: "Xp22.11"
module: 102
arm: "+"
pooled_cpm: 3.08
n_lines_expressing: 18
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# PTCHD1

*patched domain containing 1* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.48× (z +14.5, q 4e-45, up in 6 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 0.249×, HS-578T 0.164×); [[Panobinostat (drug)]] 0.5 µM in 1 line (BT-474 0.0895×; ⚠ cell-cycle shift, explains ~30% of this change); [[Auranofin (drug)]] 5 µM in 1 line (PANC-1 0.0361×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRMP1]] (+0.52, fdr 1e-04), [[PLAAT1]] (+0.52, fdr 2e-04), [[KCNQ3]] (+0.51, fdr 8e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MSI1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[TDRP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.48×** | +14.5 | 4e-45 | 6/12 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.66×** | +12.2 | 1e-31 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.97×** | +11.3 | 1e-27 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.91×** | +9.8 | 1e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +9.4 | 8e-19 | 9/15 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.66×** | +8.0 | 8e-14 | 11/15 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.40×** | +5.1 | 2e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.9 | 6e-05 | 1/14 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +4.7 | 1e-04 | 2/13 (PANC-1, NCI-H460) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.2 | 0.001 | 2/12 (NCI-H460, NCI-H2347) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.04×** | +4.2 | 0.002 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +3.9 | 0.004 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.9 | 0.004 | 1/9 (NCI-H23) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.39×** | +3.7 | 0.007 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.58×** | +3.6 | 0.012 | 0/14 | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.013 | 2/15 (NCI-H2347, NCI-H460) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +3.5 | 0.014 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +3.4 | 0.018 | 2/15 (NCI-H2030, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.063 | 2/14 (H4, HS-578T) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.28×** | +2.9 | 0.097 | 1/13 (SK-MEL-2) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 0.249×, HS-578T 0.164×); [[Panobinostat (drug)]] 0.5 µM in 1 line (BT-474 0.0895×; ⚠ cell-cycle shift, explains ~30% of this change); [[Auranofin (drug)]] 5 µM in 1 line (PANC-1 0.0361×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 44.9 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0895× (z -16.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.5) |
| [[PANC-1 (line)]] | alt | 1.88 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.0361× (z -11.4) |
| [[CHP-212 (line)]] | wt | 84.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.160× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.381 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRMP1]] | +0.52 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[PLAAT1]] | +0.52 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[KCNQ3]] | +0.51 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[SNAP91]] | +0.51 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[EBF4]] | +0.51 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[GABBR1]] | +0.50 | +0.29 / +0.58 | both halves | 2e-04 |  |
| [[FAM184A]] | +0.50 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[CELF4]] | +0.50 | +0.20 / +0.55 | both halves | 7e-04 |  |
| [[SYN2]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[SRCIN1]] | +0.50 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[LINC01287]] | +0.50 | +0.41 / +0.37 | both halves | 9e-05 |  |
| [[KIF5A]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | C | MSI1 activity raises PTCHD1's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without MSI1 | 0.061 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TDRP]] | C | PTCHD1 activity raises TDRP's level | lines that do not express PTCHD1 (32) vs lines expressing it (18) | 3.71× lower at baseline in the lines without PTCHD1 | 0.079 | ⚠ within organs, on part of the lines; also absent: EPGN, ENSG00000260958, DCN; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.8, 30.2); signed map (31.5, 22.0). **Vector** length 32.2, 6.50% of its response variance represented; |z| ≥ 3 in 372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | patched domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:23,334,849-23,404,374 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC65C1, FLJ30296 |
| Gene groups (HGNC) | Solute carrier family 65 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NR3](https://www.uniprot.org/uniprotkb/Q96NR3) (Patched domain-containing protein 1):

> Required for the development and function of the thalamic reticular nucleus (TRN), a part of the thalamus that is critical for thalamocortical transmission, generation of sleep rhythms, sensorimotor processing and attention. Can bind cholesterol in vitro.

**Summary**, from NCBI Gene [139411](https://www.ncbi.nlm.nih.gov/gene/139411):

> This gene encodes a membrane protein with a patched domain. The encoded protein is similar to Drosophila proteins which act as receptors for the morphogen sonic hedgehog. Deletions in this gene, which is located on the X chromosome, are associated with intellectual disability and autism (PMID: 21091464, PMID: 20844286). [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:26392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26392) · Entrez [139411](https://www.ncbi.nlm.nih.gov/gene/139411) · UniProt [Q96NR3](https://www.uniprot.org/uniprotkb/Q96NR3) · Ensembl [ENSG00000165186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165186)

## Data

Gene col 9083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9083); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9083]; `tensor/DDL_lfc|DDL_z.npy` [9083]; `embed/gene_vectors.npy` [9083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9083 or target_col == 9083). Every well: [[PTCHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTCHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
