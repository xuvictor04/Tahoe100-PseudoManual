---
symbol: "LHX4"
type: "gene"
col: 4276
ensembl_id: "ENSG00000121454"
name: "LIM homeobox 4"
location: "1q25.2"
module: 53
arm: "+"
pooled_cpm: 2.27
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# LHX4

*LIM homeobox 4* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.39× (z +16.4, q 0e+00, up in 21 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CELF5]] (+0.77, fdr 7e-06), [[GRAMD2A]] (+0.69, fdr 7e-06), [[ITGA7]] (+0.67, fdr 1e-05); moves opposite to [[IPP]] (-0.57, fdr 6e-05), [[TRAPPC11]] (-0.56, fdr 1e-05), [[COG4]] (-0.54, fdr 1e-04).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPHA1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +16.4 | 0e+00 | 21/25 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.97×** | +13.1 | 1e-36 | 32/42 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +12.8 | 4e-35 | 15/28 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.19×** | +11.0 | 7e-26 | 30/42 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.06×** | +10.6 | 4e-24 | 29/41 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.5 | 1e-23 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.90×** | +10.1 | 5e-22 | 31/44 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.0 | 2e-17 | 5/10 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +8.2 | 2e-14 | 21/42 (NCI-H460, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +8.0 | 9e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +7.8 | 2e-13 | 16/33 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +5.3 | 5e-06 | 8/23 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.3 | 5e-06 | 4/42 (J82, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.3 | 5e-06 | 14/31 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.3 | 5e-06 | 1/8 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +4.8 | 6e-05 | 6/24 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +4.1 | 0.002 | 4/32 (PANC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.49×** | +3.7 | 0.005 | 3/33 (LOX-IMVI, J82, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.56×** | +3.2 | 0.037 | 1/20 (BT-474) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.791× | -3.2 | 0.62 | 9/39 (Panc 03.27, LOX-IMVI, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 0.5 µM |  | 0.728× | -3.1 | 0.62 | 3/40 (SW 900, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 1.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +10.1) | — |
| [[A-172 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.901 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.834 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.885 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.964 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.912 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.890 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.736 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELF5]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ITGA7]] | +0.67 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PIP5KL1]] | +0.66 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[AZU1]] | +0.65 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[APC2]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[EPHA1-AS1]] | +0.62 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[KIF17]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.61 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SYN1]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPP]] | -0.57 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[TRAPPC11]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[COG4]] | -0.54 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[ARMC1]] | -0.54 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CEPT1]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ASH2L]] | -0.52 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[PHC3]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[QRSL1]] | -0.50 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[RPAP2]] | -0.49 | -0.29 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity lowers LHX4's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without EPHA1-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.1, -16.7); signed map (17.6, 14.7). **Vector** length 40.2, 4.49% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +16.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | +2.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.9 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | LIM homeobox 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:180,230,264-180,278,984 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Gsh4 |
| Gene groups (HGNC) | LIM class homeoboxes |
| Reactome | 4 pathways, smallest: Regulation of expression of SLITs and ROBOs; Signaling by ROBO receptors; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969G2](https://www.uniprot.org/uniprotkb/Q969G2) (LIM/homeobox protein Lhx4):

> May play a critical role in the development of respiratory control mechanisms and in the normal growth and maturation of the lung. Binds preferentially to methylated DNA.

**Summary**, from NCBI Gene [89884](https://www.ncbi.nlm.nih.gov/gene/89884):

> This gene encodes a member of a large protein family which contains the LIM domain, a unique cysteine-rich zinc-binding domain. The encoded protein is a transcription factor involved in the control of differentiation and development of the pituitary gland. Mutations in this gene cause combined pituitary hormone deficiency 4. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:21734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21734) · Entrez [89884](https://www.ncbi.nlm.nih.gov/gene/89884) · UniProt [Q969G2](https://www.uniprot.org/uniprotkb/Q969G2) · Ensembl [ENSG00000121454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121454)

## Data

Gene col 4276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4276); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4276]; `tensor/DDL_lfc|DDL_z.npy` [4276]; `embed/gene_vectors.npy` [4276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4276 or target_col == 4276). Every well: [[LHX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
