---
symbol: "RFNG"
type: "gene"
col: 9845
ensembl_id: "ENSG00000169733"
name: "RFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase"
location: "17q25.3"
module: 24
arm: "+"
pooled_cpm: 4.27
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RFNG

*RFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.57× (z +8.0, q 1e-12, up in 5 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.04× (z +3.8, q 0.018, up in 7 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.597× (z -4.5, q 0.003, down in 17 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAT2]] (+0.66, fdr 7e-06), [[ENKD1]] (+0.65, fdr 1e-05), [[DNLZ]] (+0.63, fdr 1e-04); moves opposite to [[XRCC5]] (-0.59, fdr 1e-05), [[G3BP1]] (-0.58, fdr 1e-05), [[SRP9]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STON2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +8.0 | 1e-12 | 5/8 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +7.7 | 5e-12 | 17/24 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +4.3 | 0.003 | 10/30 (NCI-H23, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.04×** | +3.8 | 0.018 | 7/33 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.036 | 10/38 (A549, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.42× | +3.1 | 0.19 | 7/41 (J82, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.42× | +3.0 | 0.19 | 3/45 (SNU-423, HCT15, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.597×** | -4.5 | 0.003 | 17/39 (RPMI-7951, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -4.2 | 0.007 | 17/45 (BT-474, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.746×** | -3.7 | 0.047 | 17/45 (A498, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.657×** | -3.6 | 0.052 | 10/44 (BT-474, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.061 | 17/39 (A498, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (drug)]] 5 µM |  | **0.762×** | -3.4 | 0.063 | 16/45 (LoVo, SW48, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.668×** | -3.4 | 0.063 | 11/44 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.685× | -3.1 | 0.12 | 6/46 (H4, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | 0.697× | -3.1 | 0.12 | 14/44 (A-427, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.707× | -3.1 | 0.12 | 8/46 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.711× | -3.0 | 0.13 | 8/46 (HT-29, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 4.31 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0393× (z -9.2) |
| [[A-172 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ENKD1]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[DNLZ]] | +0.63 | +0.35 / +0.72 | both halves | 1e-04 |  |
| [[ARL8A]] | +0.63 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[PLEKHM2]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FBXW5]] | +0.62 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[ALKBH7]] | +0.62 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[ZNF446]] | +0.61 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[ZNF358]] | +0.61 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[HRAS]] | +0.61 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[ISCU]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC5]] | -0.59 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SRP9]] | -0.58 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[HNRNPA2B1]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[H2AX]] | -0.58 | -0.40 / -0.64 | both halves | 5e-05 | pathway: Pre-NOTCH Expression and Processing |
| [[GLO1]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[CBX5]] | -0.56 | -0.31 / -0.68 | both halves | 2e-04 |  |
| [[TMX1]] | -0.55 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[PRKDC]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[SSX2IP]] | -0.54 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[PAICS]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TUBA1B]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STON2]] | B | STON2 activity lowers RFNG's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.20× higher at baseline in the lines without STON2 | 0.074 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.2, -15.5); signed map (-17.3, -2.1). **Vector** length 45.1, 5.71% of its response variance represented; |z| ≥ 3 in 618 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +7.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -4.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,047,902-82,051,831 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 3 pathways, smallest: Pre-NOTCH Processing in Golgi; Pre-NOTCH Expression and Processing; Signaling by NOTCH |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y644](https://www.uniprot.org/uniprotkb/Q9Y644) (Beta-1,3-N-acetylglucosaminyltransferase radical fringe):

> Glycosyltransferase that initiates the elongation of O-linked fucose residues attached to EGF-like repeats in the extracellular domain of Notch molecules. Modulates NOTCH1 activity by modifying O-fucose residues at specific EGF-like domains resulting in enhancement of NOTCH1 activation by DLL1 and JAG1. May be involved in limb formation and in neurogenesis.

**Summary**, from NCBI Gene [5986](https://www.ncbi.nlm.nih.gov/gene/5986):

> Predicted to enable O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase activity. Predicted to be involved in regulation of Notch signaling pathway. Predicted to act upstream of or within positive regulation of Notch signaling pathway. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9974) · Entrez [5986](https://www.ncbi.nlm.nih.gov/gene/5986) · UniProt [Q9Y644](https://www.uniprot.org/uniprotkb/Q9Y644) · Ensembl [ENSG00000169733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169733)

## Data

Gene col 9845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9845); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9845]; `tensor/DDL_lfc|DDL_z.npy` [9845]; `embed/gene_vectors.npy` [9845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9845 or target_col == 9845). Every well: [[RFNG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFNG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
