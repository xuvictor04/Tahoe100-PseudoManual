---
symbol: "GALK1"
type: "gene"
col: 2954
ensembl_id: "ENSG00000108479"
name: "galactokinase 1"
location: "17q25.1"
module: 113
arm: "+"
pooled_cpm: 5.14
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# GALK1

*galactokinase 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.68× (z +9.3, q 7e-18, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Budesonide (drug)]] 0.5 µM: 1.43× (z +3.5, q 0.044, up in 7 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.463× (z -7.6, q 2e-11, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTSL4]] (+0.57, fdr 2e-05), [[MMP15]] (+0.53, fdr 2e-05), [[TEX264]] (+0.52, fdr 4e-05); moves opposite to [[PRKACB]] (-0.39, fdr 7e-04, ⚠ not reproduced).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDZD4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +9.3 | 7e-18 | 7/10 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.00×** | +6.8 | 3e-09 | 15/27 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.2 | 3e-05 | 6/15 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.48×** | +3.9 | 0.016 | 10/28 (J82, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.044 | 7/42 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.83×** | +3.4 | 0.058 | 2/37 (NCI-H460, A498) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.078 | 3/40 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.38× | +3.2 | 0.11 | 5/35 (LOX-IMVI, LoVo, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2954.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.463×** | -7.6 | 2e-11 | 29/45 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.468×** | -7.5 | 2e-11 | 28/43 (HepG2/C3A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.500×** | -6.8 | 2e-09 | 26/36 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.501×** | -6.8 | 2e-09 | 24/44 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -5.6 | 3e-06 | 23/38 (NCI-H2030, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.660×** | -3.9 | 0.011 | 14/42 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -3.5 | 0.031 | 12/42 (SK-MEL-2, SHP-77, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.699×** | -3.5 | 0.031 | 16/44 (HepG2/C3A, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.721×** | -3.2 | 0.082 | 12/45 (NCI-H2030, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.510× | -3.1 | 0.10 | 5/37 (A-427, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.730× | -3.1 | 0.10 | 10/42 (NCI-H2030, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.716× | -3.0 | 0.11 | 9/43 (BT-474, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +8.6) ⚠ cell-cycle shift, explains ~78% of this change | [[Folic acid (drug)]] 5 µM 0.335× (z -8.6) |
| [[LS 180 (line)]] | wt | 4.28 | 0 | 2 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0632× (z -9.3) |
| [[A-172 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HEC-1-A (line)]] | alt | 5.30 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0489× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 5.60 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0837× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 6.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 4.46 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0491× (z -10.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL4]] | +0.57 | +0.62 / +0.48 | both halves | 2e-05 | pathway: Diseases of glycosylation |
| [[MMP15]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[TEX264]] | +0.52 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[FKBP1B]] | +0.52 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[TWF2]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[EHD2]] | +0.51 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[ITGA5]] | +0.51 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[FIBP]] | +0.50 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[CORO2A]] | +0.50 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[FBXO41]] | +0.50 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[PANX1]] | +0.49 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[APC2]] | +0.48 | +0.46 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKACB]] | -0.39 | -0.37 / -0.20 | ⚠ not reproduced | 7e-04 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | PDZD4 activity raises GALK1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.26× lower at baseline in the lines without PDZD4 | 0.063 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, 8.8); signed map (-21.9, 34.1). **Vector** length 50.9, 6.97% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +3.3 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.2 | +6.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -5.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | galactokinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,751,594-75,765,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GALK |
| Gene groups (HGNC) | Galactokinase family |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 5 pathways, smallest: Galactose catabolism; Diseases associated with glycosylation precursor biosynthesis; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P51570](https://www.uniprot.org/uniprotkb/P51570) (Galactokinase):

> Catalyzes the transfer of a phosphate from ATP to alpha-D-galactose and participates in the first committed step in the catabolism of galactose.

**Summary**, from NCBI Gene [2584](https://www.ncbi.nlm.nih.gov/gene/2584):

> Galactokinase is a major enzyme for the metabolism of galactose and its deficiency causes congenital cataracts during infancy and presenile cataracts in the adult population. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4118) · Entrez [2584](https://www.ncbi.nlm.nih.gov/gene/2584) · UniProt [P51570](https://www.uniprot.org/uniprotkb/P51570) · Ensembl [ENSG00000108479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108479)

## Data

Gene col 2954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2954); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2954]; `tensor/DDL_lfc|DDL_z.npy` [2954]; `embed/gene_vectors.npy` [2954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2954 or target_col == 2954). Every well: [[GALK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
