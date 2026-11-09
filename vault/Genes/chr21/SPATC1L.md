---
symbol: "SPATC1L"
type: "gene"
col: 8331
ensembl_id: "ENSG00000160284"
name: "spermatogenesis and centriole associated 1 like"
location: "21q22.3"
module: 58
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 40
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# SPATC1L

*spermatogenesis and centriole associated 1 like* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.48× (z +7.2, q 4e-10, up in 26 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.458× (z -6.2, q 3e-07, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAC3]] (+0.68, fdr 4e-05), [[MRPL55]] (+0.66, fdr 1e-04), [[CAMK2G]] (+0.65, fdr 3e-05); moves opposite to [[ANKRD18A]] (-0.62, fdr 6e-05), [[ELK4]] (-0.60, fdr 4e-05), [[CGGBP1]] (-0.60, fdr 8e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[PBXIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +7.2 | 4e-10 | 26/35 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +6.5 | 2e-08 | 26/34 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.18×** | +6.0 | 5e-07 | 2/4 (A498, HOP62) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.93×** | +5.2 | 3e-05 | 16/35 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.86×** | +4.9 | 9e-05 | 12/33 (HOP62, A-427, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +4.4 | 0.001 | 11/35 (HOP62, A-427, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +4.3 | 0.002 | 2/13 (SNU-423, NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.67×** | +4.1 | 0.004 | 7/12 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +4.0 | 0.005 | 11/32 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.009 | 8/26 (A-172, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.58×** | +3.6 | 0.014 | 2/33 (A-427, SW480) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.5 | 0.025 | 2/24 (J82, RPMI-7951) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.4 | 0.030 | 1/28 (SW480) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.1 | 0.084 | 5/35 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.458×** | -6.2 | 3e-07 | 16/27 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -4.3 | 0.004 | 14/35 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.579×** | -4.2 | 0.005 | 15/34 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 3.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0479× (z -10.7) |
| [[A-172 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.763 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.247 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAC3]] | +0.68 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[MRPL55]] | +0.66 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[CAMK2G]] | +0.65 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MYPOP]] | +0.65 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[MPST]] | +0.64 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[MOSPD3]] | +0.63 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[IGSF8]] | +0.62 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[SLC27A1]] | +0.62 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[RBIS]] | +0.61 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[MPND]] | +0.61 | +0.32 / +0.52 | both halves | 2e-04 |  |
| [[TMEM256]] | +0.60 | +0.31 / +0.43 | both halves | 2e-04 |  |
| [[ANKRD27]] | +0.60 | +0.29 / +0.46 | both halves | 2e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18A]] | -0.62 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[ELK4]] | -0.60 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CGGBP1]] | -0.60 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[RXYLT1]] | -0.60 | -0.47 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[RBM26-AS1]] | -0.59 | -0.45 / -0.24 | both halves | 4e-04 |  |
| [[PRKAR1A]] | -0.58 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[CHRAC1]] | -0.58 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ST7L]] | -0.58 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[OGFRL1]] | -0.58 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[RC3H2]] | -0.57 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[ZNF337-AS1]] | -0.57 | -0.36 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[RO60]] | -0.56 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.56 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[LRRC57]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBXIP1]] | B | SPATC1L activity raises PBXIP1's level | lines that do not express SPATC1L (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without SPATC1L | 0.073 | ⚠ within organs, on part of the lines; also absent: TIAM1 |
| [[LPGAT1]] | B | SPATC1L activity lowers LPGAT1's level | lines that do not express SPATC1L (10) vs lines expressing it (40) | 1.41× higher at baseline in the lines without SPATC1L | 0.079 | ⚠ within organs, on part of the lines; also absent: TIAM1 |
| [[NFS1]] | B | SPATC1L activity raises NFS1's level | lines that do not express SPATC1L (10) vs lines expressing it (40) | 1.22× lower at baseline in the lines without SPATC1L | 0.085 | ⚠ within organs, on part of the lines; also absent: TIAM1 |
| [[SLC27A1]] | B | SPATC1L activity raises SLC27A1's level | lines that do not express SPATC1L (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without SPATC1L | 0.091 | ⚠ within organs, on part of the lines; also absent: TIAM1 |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.6, -15.5); signed map (-35.8, 3.3). **Vector** length 37.0, 4.86% of its response variance represented; |z| ≥ 3 in 621 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +2.3 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.9 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.8 | +6.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.8 | -0.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.8 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis and centriole associated 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:46,161,148-46,184,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C21orf56 |
| Matched by | ensembl_id |

UniProt [Q9H0A9](https://www.uniprot.org/uniprotkb/Q9H0A9) carries no function annotation.

**Summary**, from NCBI Gene [84221](https://www.ncbi.nlm.nih.gov/gene/84221):

> Enables identical protein binding activity. Predicted to be involved in spermatogenesis. Predicted to act upstream of or within actin polymerization or depolymerization; positive regulation of cAMP-dependent protein kinase activity; and positive regulation of cAMP/PKA signal transduction. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:1298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1298) · Entrez [84221](https://www.ncbi.nlm.nih.gov/gene/84221) · UniProt [Q9H0A9](https://www.uniprot.org/uniprotkb/Q9H0A9) · Ensembl [ENSG00000160284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160284)

## Data

Gene col 8331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8331); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8331]; `tensor/DDL_lfc|DDL_z.npy` [8331]; `embed/gene_vectors.npy` [8331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8331 or target_col == 8331). Every well: [[SPATC1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATC1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
