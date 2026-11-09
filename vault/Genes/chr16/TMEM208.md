---
symbol: "TMEM208"
type: "gene"
col: 9685
ensembl_id: "ENSG00000168701"
name: "transmembrane protein 208"
location: "16q22.1"
module: 49
arm: "+"
pooled_cpm: 20.96
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# TMEM208

*transmembrane protein 208* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.18× (z +6.2, q 3e-07, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.144×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL55]] (+0.82, fdr 7e-06), [[ACBD3]] (+0.79, fdr 7e-06), [[SSR2]] (+0.77, fdr 7e-06); moves opposite to [[SEPTIN11]] (-0.66, fdr 1e-05), [[CHRAC1]] (-0.64, fdr 1e-05), [[HNRNPK]] (-0.63, fdr 4e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +6.2 | 3e-07 | 43/48 (SW480, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.8 | 0.034 | 29/43 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +3.7 | 0.049 | 29/47 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.56×** | +3.5 | 0.059 | 18/39 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.95×** | +3.5 | 0.059 | 24/46 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.93×** | +3.4 | 0.059 | 28/46 (A498, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.92×** | +3.4 | 0.059 | 24/46 (A498, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.066 | 23/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.49×** | +3.2 | 0.090 | 24/45 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.84×** | +3.2 | 0.090 | 18/47 (AsPC-1, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.82×** | +3.1 | 0.099 | 23/44 (NCI-H460, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.100 | 20/48 (HOP62, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9685.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.144×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.719× | -3.7 | 0.10 | 26/47 (NCI-H2347, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.659× | -3.3 | 0.24 | 22/48 (KATO III, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL55]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.79 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[SSR2]] | +0.77 | +0.70 / +0.73 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[SCNM1]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[MED8]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[NAT9]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[PEX16]] | +0.70 | +0.55 / +0.71 | both halves | 1e-05 | pathway: Protein localization |
| [[SEC61B]] | +0.70 | +0.59 / +0.70 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN11]] | -0.66 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[CHRAC1]] | -0.64 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.63 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[GNG12]] | -0.61 | -0.38 / -0.66 | both halves | 7e-05 |  |
| [[NHLRC2]] | -0.61 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[LEPROT]] | -0.61 | -0.59 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.6, -33.5); signed map (-49.1, 11.4). **Vector** length 78.9, 21.2% of its response variance represented; |z| ≥ 3 in 474 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.56 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.56 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | -4.3 | +3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | +0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 208 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,227,103-67,229,278 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC171, hSND2, SND2 |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTX3](https://www.uniprot.org/uniprotkb/Q9BTX3) (Transmembrane protein 208):

> May function as a negative regulator of endoplasmic reticulum-stress induced autophagy.

**Summary**, from NCBI Gene [29100](https://www.ncbi.nlm.nih.gov/gene/29100):

> This gene encodes a highly conserved protein which is localized in the endoplasmic reticulum (ER). The protein is linked to autophagy and ER stress. Knockdown of this gene increased autophagy and triggered ER stress. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:25015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25015) · Entrez [29100](https://www.ncbi.nlm.nih.gov/gene/29100) · UniProt [Q9BTX3](https://www.uniprot.org/uniprotkb/Q9BTX3) · Ensembl [ENSG00000168701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168701)

## Data

Gene col 9685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9685); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9685]; `tensor/DDL_lfc|DDL_z.npy` [9685]; `embed/gene_vectors.npy` [9685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9685 or target_col == 9685). Every well: [[TMEM208 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM208.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
