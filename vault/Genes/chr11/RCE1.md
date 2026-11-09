---
symbol: "RCE1"
type: "gene"
col: 10413
ensembl_id: "ENSG00000173653"
name: "Ras converting CAAX endopeptidase 1"
location: "11q13.2"
module: 24
arm: "+"
pooled_cpm: 10.31
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RCE1

*Ras converting CAAX endopeptidase 1* — 11q13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.465× (z -4.2, q 0.016, down in 24 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.120×); [[Malotilate (drug)]] 0.05 µM in 1 line (C-33 A 0.0703×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC34]] (+0.73, fdr 7e-06), [[FBXW5]] (+0.71, fdr 1e-05), [[ZFAND2B]] (+0.71, fdr 7e-06); moves opposite to [[HNRNPA3]] (-0.62, fdr 3e-05), [[PTGR2]] (-0.59, fdr 1e-05), [[IPO5]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | 1.39× | +3.5 | 0.27 | 16/41 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.83× | +3.3 | 0.28 | 9/26 (HOP62, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 1.38× | +3.2 | 0.28 | 5/20 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10413.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.120×); [[Malotilate (drug)]] 0.05 µM in 1 line (C-33 A 0.0703×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.465×** | -4.2 | 0.016 | 24/45 (SNU-423, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.520×** | -3.6 | 0.098 | 18/42 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.730× | -3.2 | 0.25 | 15/42 (SNU-423, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adenosine (drug)]] 0.5 µM |  | 0.739× | -3.1 | 0.25 | 6/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 7.78 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0703× (z -8.9) |
| [[SNU-423 (line)]] | alt | 9.24 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -9.3) |
| [[A-172 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | +0.73 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[FBXW5]] | +0.71 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[ZFAND2B]] | +0.71 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[RNF166]] | +0.70 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[MAP1S]] | +0.69 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PCGF1]] ⚠ | +0.69 | +0.49 / +0.74 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PMM1]] | +0.67 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SIRT6]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[INAFM1]] | +0.65 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[SIRT7]] | +0.63 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[TRAPPC4]] | +0.63 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[WIPF2]] | +0.63 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[RPP21]] | +0.62 | +0.43 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | -0.62 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[PTGR2]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[IPO5]] | -0.56 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[BRCC3]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 | pathway: Deubiquitination |
| [[TMX3]] | -0.56 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[XRCC5]] | -0.55 | -0.29 / -0.65 | both halves | 2e-04 |  |
| [[DHFR]] | -0.55 | -0.24 / -0.64 | both halves | 5e-04 |  |
| [[RCN1]] | -0.54 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[PIGK]] | -0.54 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[STMP1]] | -0.54 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[FAM81A]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.4, -14.8); signed map (-16.7, -1.8). **Vector** length 48.9, 6.94% of its response variance represented; |z| ≥ 3 in 551 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | +1.9 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -1.3 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.1 | -3.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Ras converting CAAX endopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,842,835-66,846,552 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hRCE1, FACE-2, FACE2; previously RCE1A, RCE1B |
| Hallmark sets | COMPLEMENT |
| Reactome | 6 pathways, smallest: RAS processing; Ub-specific processing proteases; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y256](https://www.uniprot.org/uniprotkb/Q9Y256) (CAAX prenyl protease 2):

> Protease involved in the processing of a variety of prenylated proteins containing the C-terminal CAAX motif, where C is a cysteine modified with an isoprenoid lipid, A is an aliphatic amino acid and X is any C-terminal amino acid. Proteolytically removes the C-terminal three residues of farnesylated and geranylated proteins, leaving the prenylated cysteine as the new C-terminus. Is able to process K-Ras, N-Ras, H-Ras, RAP1B and G-gamma-1.

**Summary**, from NCBI Gene [9986](https://www.ncbi.nlm.nih.gov/gene/9986):

> This gene encodes an integral membrane protein which is classified as a member of the metalloproteinase family. This enzyme is thought to function in the maintenance and processing of CAAX-type prenylated proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13721) · Entrez [9986](https://www.ncbi.nlm.nih.gov/gene/9986) · UniProt [Q9Y256](https://www.uniprot.org/uniprotkb/Q9Y256) · Ensembl [ENSG00000173653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173653)

## Data

Gene col 10413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10413); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10413]; `tensor/DDL_lfc|DDL_z.npy` [10413]; `embed/gene_vectors.npy` [10413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10413 or target_col == 10413). Every well: [[RCE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
