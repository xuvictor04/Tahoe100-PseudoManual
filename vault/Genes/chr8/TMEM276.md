---
symbol: "TMEM276"
type: "gene"
col: 16642
ensembl_id: "ENSG00000291317"
name: "transmembrane protein 276"
location: "8q24.3"
module: 58
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# TMEM276

*transmembrane protein 276* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.99× (z +6.8, q 8e-09, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.79× (z +3.7, q 0.026, up in 14 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.379× (z -8.8, q 7e-16, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICOS13]] (+0.78, fdr 7e-06), [[METRN]] (+0.73, fdr 1e-05), [[NME3]] (+0.72, fdr 2e-05); moves opposite to [[PSME3IP1]] (-0.62, fdr 3e-05), [[MLH1]] (-0.62, fdr 1e-05), [[ELK4]] (-0.61, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +6.8 | 8e-09 | 3/5 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +6.0 | 5e-07 | 10/18 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +4.1 | 0.007 | 11/21 (J82, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +3.7 | 0.026 | 14/41 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +3.4 | 0.063 | 13/44 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +3.4 | 0.063 | 13/36 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.60× | +3.0 | 0.20 | 7/32 (SW480, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.379×** | -8.8 | 7e-16 | 33/34 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.367×** | -6.4 | 4e-08 | 25/35 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.460×** | -4.8 | 2e-04 | 19/40 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.240×** | -4.8 | 2e-04 | 24/37 (LS 180, C-33 A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.254×** | -4.6 | 5e-04 | 17/34 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -4.3 | 0.002 | 20/42 (BT-474, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.546×** | -3.9 | 0.008 | 19/44 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.611× | -3.2 | 0.11 | 12/39 (SW 900, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.64 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.6) |
| [[A498 (line)]] | wt | 3.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -10.3) |
| [[A549 (line)]] | wt | 4.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0212× (z -12.5) |
| [[HS-578T (line)]] | alt | 6.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0952× (z -8.8) |
| [[LoVo (line)]] | wt | 3.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 4.63 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0587× (z -8.6) |
| [[A-427 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 9 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICOS13]] | +0.78 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[METRN]] | +0.73 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[NME3]] | +0.72 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[ANTKMT]] | +0.71 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ZDHHC12]] | +0.68 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[TMEM256]] | +0.68 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[C4orf48]] | +0.68 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[MALSU1]] | +0.67 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[LAMTOR2]] | +0.67 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[PHAF1]] | +0.67 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[MHENCR]] | +0.66 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[SLC39A4]] | +0.66 | +0.51 / +0.63 | both halves | 1e-05 | ⚠ same locus (47.0 kb, same strand: neighbours can correlate without regulation) |
| [[LSM2]] | +0.66 | +0.38 / +0.65 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3IP1]] | -0.62 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[MLH1]] | -0.62 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ELK4]] | -0.61 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[CSTF3]] | -0.61 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[ZNF655]] | -0.60 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[VPS52]] | -0.59 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[KRR1]] | -0.59 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[PSMD6-AS1]] | -0.59 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[U2AF2]] | -0.58 | -0.19 / -0.54 | ⚠ one half (not replicated) | 9e-04 |  |
| [[MYSM1]] | -0.58 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PARD6G-AS1]] | -0.57 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[MAGOHB]] | -0.57 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[SMIM15-AS1]] | -0.57 | -0.47 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TMEM276's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.0, -16.9); signed map (-32.3, 6.3). **Vector** length 50.2, 7.72% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.9 | +6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 276 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,463,817-144,465,667 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [P0DTL5](https://www.uniprot.org/uniprotkb/P0DTL5) carries no function annotation.

**Summary**, from NCBI Gene [84773](https://www.ncbi.nlm.nih.gov/gene/84773):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:56235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56235) · Entrez [84773](https://www.ncbi.nlm.nih.gov/gene/84773) · UniProt [P0DTL5](https://www.uniprot.org/uniprotkb/P0DTL5) · Ensembl [ENSG00000291317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000291317)

## Data

Gene col 16642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16642); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16642]; `tensor/DDL_lfc|DDL_z.npy` [16642]; `embed/gene_vectors.npy` [16642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16642 or target_col == 16642). Every well: [[TMEM276 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM276.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
