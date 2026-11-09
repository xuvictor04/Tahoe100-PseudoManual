---
symbol: "MRPL46"
type: "gene"
col: 15204
ensembl_id: "ENSG00000259494"
name: "mitochondrial ribosomal protein L46"
location: "15q25.3"
module: 11
arm: "+"
pooled_cpm: 5.04
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRPL46

*mitochondrial ribosomal protein L46* — 15q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.07× (z +5.7, q 6e-06, up in 18 of 29 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.61× (z +3.9, q 0.014, up in 16 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.632× (z -3.8, q 0.096, down in 22 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Tadalafil (drug)]] 5 µM in 2 lines (NCI-H2347 0.0640×, J82 0.0705×); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.113×); [[Trifluridine (drug)]] 0.5 µM in 1 line (SHP-77 0.0567×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS18C]] (+0.79, fdr 1e-05), [[ZNF593]] (+0.78, fdr 7e-06), [[LEO1]] (+0.75, fdr 1e-05); moves opposite to [[RPN1]] (-0.69, fdr 1e-05), [[DHFR]] (-0.69, fdr 4e-05), [[TXNDC5]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +5.7 | 6e-06 | 18/29 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.68×** | +4.2 | 0.005 | 12/31 (NCI-H2030, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.71×** | +4.2 | 0.005 | 21/44 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.014 | 16/45 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.53× | +3.2 | 0.17 | 14/39 (C32, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Tadalafil (drug)]] 5 µM in 2 lines (NCI-H2347 0.0640×, J82 0.0705×); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.113×); [[Trifluridine (drug)]] 0.5 µM in 1 line (SHP-77 0.0567×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -3.8 | 0.096 | 22/45 (NCI-H460, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.404× | -3.3 | 0.20 | 12/38 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Baicalin (drug)]] 5 µM |  | 0.754× | -3.3 | 0.20 | 11/48 (MIA PaCa-2, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.77 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0705× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 4.28 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0640× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 4.49 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.113× (z -9.5) |
| [[SHP-77 (line)]] | alt | 5.86 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0567× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18C]] | +0.79 | +0.55 / +0.87 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 981 |
| [[ZNF593]] | +0.78 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[LEO1]] | +0.75 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[PDRG1]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.74 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.74 | +0.42 / +0.79 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL32]] | +0.74 | +0.60 / +0.78 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 996 |
| [[COA3]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[PHAX]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.73 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[COIL]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.72 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[C18orf21]] | +0.72 | +0.64 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | -0.69 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[DHFR]] | -0.69 | -0.42 / -0.72 | both halves | 4e-05 |  |
| [[TXNDC5]] | -0.68 | -0.51 / -0.75 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.67 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[EIF4EBP2]] | -0.65 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[CTSZ]] | -0.64 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[TM9SF3]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.63 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[FAM81A]] | -0.63 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[TMEM30A]] | -0.62 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[CDC42]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.7, -10.8); signed map (-12.8, -7.3). **Vector** length 47.0, 6.50% of its response variance represented; |z| ≥ 3 in 570 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.3 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.8 | +2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +0.7 | +1.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.7 | -3.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.3 — chr15:88,459,477-88,467,390 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIECG2, P2ECSL, mL46; previously C15orf4 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9H2W6](https://www.uniprot.org/uniprotkb/Q9H2W6) carries no function annotation.

**Summary**, from NCBI Gene [26589](https://www.ncbi.nlm.nih.gov/gene/26589):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:1192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1192) · Entrez [26589](https://www.ncbi.nlm.nih.gov/gene/26589) · UniProt [Q9H2W6](https://www.uniprot.org/uniprotkb/Q9H2W6) · Ensembl [ENSG00000259494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259494)

## Data

Gene col 15204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15204); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15204]; `tensor/DDL_lfc|DDL_z.npy` [15204]; `embed/gene_vectors.npy` [15204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15204 or target_col == 15204). Every well: [[MRPL46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
