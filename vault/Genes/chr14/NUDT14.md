---
symbol: "NUDT14"
type: "gene"
col: 11462
ensembl_id: "ENSG00000183828"
name: "nudix hydrolase 14"
location: "14q32.33"
module: 59
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# NUDT14

*nudix hydrolase 14* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.22× (z +9.0, q 9e-17, up in 17 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.24× (z +4.2, q 0.004, up in 9 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.580× (z -6.0, q 1e-06, down in 25 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAT2]] (+0.67, fdr 1e-05), [[SPACA9]] (+0.61, fdr 2e-05), [[DCXR]] (+0.61, fdr 2e-05); moves opposite to [[CCT6A]] (-0.57, fdr 1e-05), [[AHSA1]] (-0.51, fdr 5e-05), [[XRCC5]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AP1M2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +9.0 | 9e-17 | 17/21 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +8.2 | 5e-14 | 5/8 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +5.7 | 3e-06 | 7/11 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.91×** | +5.0 | 8e-05 | 17/25 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.24×** | +4.2 | 0.004 | 9/23 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.59×** | +3.4 | 0.056 | 13/39 (Hs 766T, A-427, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.056 | 5/34 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.85× | +3.2 | 0.10 | 4/36 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.580×** | -6.0 | 1e-06 | 25/35 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.382×** | -3.9 | 0.027 | 19/35 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -3.5 | 0.078 | 11/33 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -3.5 | 0.078 | 13/43 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -3.4 | 0.081 | 14/43 (NCI-H460, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.664× | -3.2 | 0.14 | 12/38 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.68 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0789× (z -10.5) |
| [[SW1417 (line)]] | alt | 7.19 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -8.6) |
| [[A-172 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SPACA9]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[DCXR]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[UAP1L1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[LAMTOR4]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[JUND]] | +0.59 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[RRAGC]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[FLCN]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[NDUFS7]] | +0.57 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[DBP]] | +0.57 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[PNPLA2]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6A]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.51 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[XRCC5]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[NAA50]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[L3HYPDH]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TXN]] | -0.49 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[TPM3]] | -0.49 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[TCP1]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AP1M2]] | B | AP1M2 activity raises NUDT14's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without AP1M2 | 0.014 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[NOXA1]] | B | NOXA1 activity raises NUDT14's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without NOXA1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[CRB3]] | B | CRB3 activity raises NUDT14's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without CRB3 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1 |
| [[EPS8L2]] | B | EPS8L2 activity raises NUDT14's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without EPS8L2 | 0.065 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[HES6]] | B | HES6 activity raises NUDT14's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without HES6 | 0.071 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-49.1, -17.4); signed map (-6.3, 19.3). **Vector** length 45.2, 6.03% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +4.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +9.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +3.4 |
| fall | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,172,938-105,181,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UGPP |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 3 pathways, smallest: Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Asparagine N-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95848](https://www.uniprot.org/uniprotkb/O95848) (Uridine diphosphate glucose pyrophosphatase NUDT14):

> Cytosolic pyrophosphatase hydrolyzing the diphosphate bond in various nucleotide-sugars with a higher efficiency for UDP-alpha-D-glucose and ADP-D-ribose.

**Summary**, from NCBI Gene [256281](https://www.ncbi.nlm.nih.gov/gene/256281):

> The protein encoded by this gene is a member of the Nudix hydrolase family. Nudix hydrolases eliminate potentially toxic nucleotide metabolites from the cell and regulate the concentrations and availability of many different nucleotide substrates, cofactors, and signaling molecules. This enzyme contains a Nudix hydrolase domain and is a UDPG pyrophosphatase that hydrolyzes UDPG to produce glucose 1-phosphate and UMP. Alternatively spliced transcript variants encoding different isoforms have …

**Accessions** — [HGNC:20141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20141) · Entrez [256281](https://www.ncbi.nlm.nih.gov/gene/256281) · UniProt [O95848](https://www.uniprot.org/uniprotkb/O95848) · Ensembl [ENSG00000183828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183828)

## Data

Gene col 11462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11462); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11462]; `tensor/DDL_lfc|DDL_z.npy` [11462]; `embed/gene_vectors.npy` [11462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11462 or target_col == 11462). Every well: [[NUDT14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
