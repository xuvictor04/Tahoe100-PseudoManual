---
symbol: "RPL26L1"
type: "gene"
col: 441
ensembl_id: "ENSG00000037241"
name: "ribosomal protein L26 like 1"
location: "5q35.1"
module: 7
arm: "+"
pooled_cpm: 13.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RPL26L1

*ribosomal protein L26 like 1* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.00× (z +11.0, q 3e-25, up in 33 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.67× (z +5.1, q 4e-05, up in 29 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0811×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO38]] (+0.61, fdr 1e-05), [[EIF6]] (+0.57, fdr 1e-05), [[RPF1]] (+0.56, fdr 1e-05); moves opposite to [[CNNM3]] (-0.55, fdr 1e-05), [[PTMA]] (-0.53, fdr 1e-05), [[TXNDC16]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.00×** | +11.0 | 3e-25 | 33/38 (A549, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.45×** | +8.6 | 2e-15 | 25/27 (A549, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.29×** | +7.7 | 4e-12 | 26/31 (A549, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.1 | 4e-05 | 29/47 (NCI-H1573, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.0 | 6e-05 | 21/40 (SW1417, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.65×** | +5.0 | 6e-05 | 26/42 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.60×** | +4.7 | 2e-04 | 26/48 (LoVo, SNU-423, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.002 | 22/47 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.51×** | +4.0 | 0.004 | 22/47 (NCI-H1573, C32, …) | two highest doses | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.005 | 20/47 (H4, LoVo, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.025 | 16/48 (A-172, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.030 | 15/46 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.082 | 10/48 (NCI-H460, C32, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 441.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0811×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.779× | -3.5 | 0.16 | 13/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.713× | -3.4 | 0.16 | 17/47 (HS-578T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.528× | -3.3 | 0.16 | 15/46 (NCI-H2030, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pentagastrin (drug)]] 5 µM |  | 0.801× | -3.1 | 0.25 | 12/48 (NCI-H460, RKO, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 12.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0811× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 8.04 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.15× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO38]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[EIF6]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 | STRING 902 |
| [[RPF1]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 | STRING 906 |
| [[MRPL20]] | +0.56 | +0.67 / +0.51 | both halves | 1e-05 | STRING 960 |
| [[MRPL47]] | +0.56 | +0.60 / +0.53 | both halves | 1e-05 | STRING 876 |
| [[PFDN1]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[VPS25]] | +0.55 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SF3A3]] | +0.55 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[TXNDC9]] | +0.55 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[POP4]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TACO1]] | +0.54 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ZNF81]] | +0.53 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM3]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PTMA]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.50 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[NAP1L1]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ARL6IP1]] | -0.46 | -0.44 / -0.40 | both halves | 5e-05 | STRING 862 |
| [[ANKRD10]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[GAD1]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[PTMS]] | -0.44 | -0.44 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-46.7, 2.5); signed map (-2.3, -24.3). **Vector** length 53.6, 8.80% of its response variance represented; |z| ≥ 3 in 627 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +2.7 | +7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Afatinib (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L26 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:172,958,729-172,969,771 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RPL26P1 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

UniProt [Q9UNX3](https://www.uniprot.org/uniprotkb/Q9UNX3) carries no function annotation.

**Summary**, from NCBI Gene [51121](https://www.ncbi.nlm.nih.gov/gene/51121):

> This gene encodes a protein that shares high sequence similarity with ribosomal protein L26. Alternative splicing results in multiple transcript variants encoding the same protein. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:17050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17050) · Entrez [51121](https://www.ncbi.nlm.nih.gov/gene/51121) · UniProt [Q9UNX3](https://www.uniprot.org/uniprotkb/Q9UNX3) · Ensembl [ENSG00000037241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037241)

## Data

Gene col 441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 441); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 441]; `tensor/DDL_lfc|DDL_z.npy` [441]; `embed/gene_vectors.npy` [441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 441 or target_col == 441). Every well: [[RPL26L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL26L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
