---
symbol: "MRPL2"
type: "gene"
col: 3388
ensembl_id: "ENSG00000112651"
name: "mitochondrial ribosomal protein L2"
location: "6p21.1"
module: 49
arm: "+"
pooled_cpm: 14.85
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# MRPL2

*mitochondrial ribosomal protein L2* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.74× (z +7.4, q 8e-11, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.330× (z -6.9, q 3e-09, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED8]] (+0.68, fdr 7e-06), [[YIF1A]] (+0.68, fdr 7e-06), [[C16orf91]] (+0.67, fdr 1e-05); moves opposite to [[GNG12]] (-0.57, fdr 4e-05), [[CDC42]] (-0.56, fdr 1e-04), [[HNRNPA3]] (-0.56, fdr 8e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +7.4 | 8e-11 | 35/48 (SW480, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.61×** | +6.4 | 5e-08 | 31/48 (SW480, BT-474, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.2 | 9e-08 | 30/41 (J82, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.55×** | +5.8 | 8e-07 | 25/44 (SW 900, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.7 | 1e-06 | 4/48 (HOP62, HCT15, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 2e-05 | 24/46 (LOX-IMVI, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +5.0 | 5e-05 | 23/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.45×** | +4.9 | 6e-05 | 24/47 (SW480, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 4e-04 | 22/46 (HOP62, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3388.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.330×** | -6.9 | 3e-09 | 34/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.384×** | -5.9 | 8e-07 | 28/44 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -5.9 | 8e-07 | 30/47 (NCI-H460, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -4.7 | 3e-04 | 26/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.727×** | -4.2 | 0.002 | 21/46 (NCI-H460, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.735×** | -3.9 | 0.010 | 18/47 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.778×** | -3.3 | 0.067 | 16/47 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.165× (z -8.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0641× (z -8.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 9.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0586× (z -19.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0739× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED8]] | +0.68 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[YIF1A]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[C16orf91]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[ZCCHC9]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.66 | +0.47 / +0.72 | both halves | 2e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 924 |
| [[RARS1]] | +0.66 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SDE2]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SKIC8]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[RNF113A]] | +0.64 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[TMEM208]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[UFL1]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG12]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[CDC42]] | -0.56 | -0.35 / -0.68 | both halves | 1e-04 |  |
| [[HNRNPA3]] | -0.56 | -0.37 / -0.66 | both halves | 8e-05 |  |
| [[APP]] | -0.55 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[LINC00342]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[FAM81A]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CTSZ]] | -0.54 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[VSIG10]] | -0.54 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[LAMP1]] | -0.53 | -0.42 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MRPL2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.1, -10.6); signed map (-13.0, -6.2). **Vector** length 74.1, 14.6% of its response variance represented; |z| ≥ 3 in 703 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.1 | +0.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.0 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +0.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,054,029-43,059,438 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-L14, RPML14, CGI-22, uL2m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q5T653](https://www.uniprot.org/uniprotkb/Q5T653) carries no function annotation.

**Summary**, from NCBI Gene [51069](https://www.ncbi.nlm.nih.gov/gene/51069):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14056) · Entrez [51069](https://www.ncbi.nlm.nih.gov/gene/51069) · UniProt [Q5T653](https://www.uniprot.org/uniprotkb/Q5T653) · Ensembl [ENSG00000112651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112651)

## Data

Gene col 3388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3388); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3388]; `tensor/DDL_lfc|DDL_z.npy` [3388]; `embed/gene_vectors.npy` [3388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3388 or target_col == 3388). Every well: [[MRPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
