---
symbol: "THAP11"
type: "gene"
col: 9627
ensembl_id: "ENSG00000168286"
name: "THAP domain containing 11"
location: "16q22.1"
module: 7
arm: "+"
pooled_cpm: 3.88
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# THAP11

*THAP domain containing 11* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.97× (z +6.2, q 3e-07, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +4.0, q 0.008, up in 13 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.176×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0941×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Saquinavir (drug)]] 5 µM in 1 line (SHP-77 0.135×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SHP-77 0.0474×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM115]] (+0.58, fdr 3e-05), [[ZBTB14]] (+0.57, fdr 1e-05), [[MRPL20-AS1]] (+0.55, fdr 1e-05); moves opposite to [[TPMT]] (-0.51, fdr 1e-05), [[STK40]] (-0.49, fdr 3e-05), [[ASPHD1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.2 | 3e-07 | 2/6 (J82, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.57×** | +4.3 | 0.005 | 9/23 (SW480, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.1 | 0.008 | 8/29 (HS-578T, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.008 | 13/38 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +3.8 | 0.019 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.026 | 8/46 (SHP-77, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.41× | +3.2 | 0.12 | 6/23 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | 1.39× | +3.0 | 0.18 | 5/27 (A498, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9627.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.176×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0941×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Saquinavir (drug)]] 5 µM in 1 line (SHP-77 0.135×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SHP-77 0.0474×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.689× | -3.5 | 0.26 | 11/45 (HT-29, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.783× | -3.2 | 0.33 | 14/38 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.1) |
| [[SHP-77 (line)]] | alt | 5.23 | 0 | 2 | — | [[Saquinavir (drug)]] 5 µM 0.135× (z -9.9) |
| [[HOP62 (line)]] | alt | 3.09 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.5 µM 0.0638× (z -9.4) |
| [[A-172 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM115]] | +0.58 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[ZBTB14]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MRPL20-AS1]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CTCF]] | +0.55 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[RPP25]] | +0.53 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[UBL4A]] | +0.53 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PRAME]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FZD1]] | +0.52 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SETD2]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[FANCF]] | +0.51 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[CHD8]] | +0.51 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[RDH14]] | +0.50 | +0.37 / +0.60 | both halves | 8e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPMT]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[STK40]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ASPHD1]] | -0.49 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[UFM1]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[DAP]] | -0.48 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[LINC00513]] | -0.47 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MALAT1]] | -0.47 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[TALAM1]] | -0.47 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[ARL5B]] | -0.45 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[SEPTIN10]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[MAGT1]] | -0.44 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[TRD-AS1]] | -0.43 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-49.9, -0.9); signed map (-3.7, -35.5). **Vector** length 43.1, 4.61% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | +1.3 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | -0.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -2.7 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.5 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,842,320-67,844,195 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRIHFB2206, CTG-B45d, CTG-B43a, RONIN |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EK4](https://www.uniprot.org/uniprotkb/Q96EK4) (THAP domain-containing protein 11):

> Transcription factor, which has both transcriptional activation and repression activities. Also modulates chromatin accessibility. In complex with HCFC1 and ZNF143, regulates the expression of several genes, including AP2S1, ESCO2, OPHN1, RBL1, UBXN8 and ZNF32. May regulate the expression of genes that encode both cytoplasmic and mitochondrial ribosomal proteins (By similarity). Required for normal mitochondrial development and function. Regulates mitochondrial gene expression, including that …

**Summary**, from NCBI Gene [57215](https://www.ncbi.nlm.nih.gov/gene/57215):

> The protein encoded by this gene contains a THAP domain, which is a conserved DNA-binding domain that has striking similarity to the site-specific DNA-binding domain (DBD) of Drosophila P element transposases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23194) · Entrez [57215](https://www.ncbi.nlm.nih.gov/gene/57215) · UniProt [Q96EK4](https://www.uniprot.org/uniprotkb/Q96EK4) · Ensembl [ENSG00000168286](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168286)

## Data

Gene col 9627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9627); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9627]; `tensor/DDL_lfc|DDL_z.npy` [9627]; `embed/gene_vectors.npy` [9627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9627 or target_col == 9627). Every well: [[THAP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
