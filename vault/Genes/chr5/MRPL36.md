---
symbol: "MRPL36"
type: "gene"
col: 10102
ensembl_id: "ENSG00000171421"
name: "mitochondrial ribosomal protein L36"
location: "5p15.33"
module: 11
arm: "+"
pooled_cpm: 13.0
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRPL36

*mitochondrial ribosomal protein L36* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.07× (z +4.8, q 1e-03, up in 32 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMC6]] (+0.87, fdr 7e-06), [[ZNF593]] (+0.81, fdr 7e-06), [[EXOSC4]] (+0.80, fdr 7e-06); moves opposite to [[DHFR]] (-0.72, fdr 2e-04), [[DPY19L4]] (-0.65, fdr 1e-04), [[FKBP9]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.07×** | +4.8 | 1e-03 | 32/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.04×** | +4.5 | 0.002 | 28/46 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.96×** | +4.4 | 0.002 | 32/41 (Panc 03.27, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +4.3 | 0.003 | 26/41 (H4, A-427, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.88×** | +4.2 | 0.004 | 28/47 (HOP62, SNU-423, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.038 | 21/46 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.334× | -3.7 | 0.13 | 31/46 (H4, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.716× | -3.1 | 0.47 | 22/48 (Panc 03.27, NCI-H661, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 18 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC6]] | +0.87 | +0.68 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[ZNF593]] | +0.81 | +0.64 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[EXOSC4]] | +0.80 | +0.62 / +0.85 | both halves | 7e-06 | STRING 403 |
| [[GADD45GIP1]] | +0.76 | +0.46 / +0.81 | both halves | 3e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 961 |
| [[C16orf91]] | +0.73 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[MRPL46]] | +0.72 | +0.44 / +0.78 | both halves | 3e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 996 |
| [[FAM174C]] ⚠ | +0.71 | +0.50 / +0.75 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS12]] | +0.70 | +0.36 / +0.76 | both halves | 1e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 999 |
| [[SMIM26]] ⚠ | +0.70 | +0.38 / +0.74 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[OXLD1]] | +0.70 | +0.46 / +0.79 | both halves | 3e-05 |  |
| [[BLOC1S4]] | +0.70 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[SCAND1]] | +0.70 | +0.46 / +0.77 | both halves | 2e-05 |  |
| [[NCBP2AS2]] | +0.69 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[KRTCAP2]] | +0.67 | +0.40 / +0.74 | both halves | 5e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR]] | -0.72 | -0.31 / -0.80 | both halves | 2e-04 |  |
| [[DPY19L4]] | -0.65 | -0.35 / -0.70 | both halves | 1e-04 |  |
| [[FKBP9]] | -0.62 | -0.44 / -0.69 | both halves | 3e-05 |  |
| [[DCTN1]] | -0.61 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[AP2B1]] | -0.61 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[CTSZ]] | -0.61 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[HNRNPA3]] | -0.60 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[TMEM30A]] | -0.60 | -0.41 / -0.70 | both halves | 4e-05 |  |
| [[RPN1]] | -0.60 | -0.38 / -0.68 | both halves | 6e-05 |  |
| [[EDEM1]] | -0.60 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TMEM237]] | -0.60 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[MOB1A]] | -0.59 | -0.33 / -0.64 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.1, -11.5); signed map (-12.4, -7.5). **Vector** length 63.6, 15.8% of its response variance represented; |z| ≥ 3 in 487 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +2.5 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.1 | +0.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +2.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.0 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:1,798,385-1,801,366 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPMJ, L36mt, PRPL36, MRP-L36, bL36m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9P0J6](https://www.uniprot.org/uniprotkb/Q9P0J6) carries no function annotation.

**Summary**, from NCBI Gene [64979](https://www.ncbi.nlm.nih.gov/gene/64979):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14490) · Entrez [64979](https://www.ncbi.nlm.nih.gov/gene/64979) · UniProt [Q9P0J6](https://www.uniprot.org/uniprotkb/Q9P0J6) · Ensembl [ENSG00000171421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171421)

## Data

Gene col 10102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10102); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10102]; `tensor/DDL_lfc|DDL_z.npy` [10102]; `embed/gene_vectors.npy` [10102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10102 or target_col == 10102). Every well: [[MRPL36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
