---
symbol: "LIME1"
type: "gene"
col: 12800
ensembl_id: "ENSG00000203896"
name: "Lck interacting transmembrane adaptor 1"
location: "20q13.33"
module: 29
arm: "-"
pooled_cpm: 3.4
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# LIME1

*Lck interacting transmembrane adaptor 1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.57× (z +12.4, q 2e-32, up in 29 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MROH6]] (+0.77, fdr 7e-06), [[CDK3]] (+0.73, fdr 7e-06), [[WASHC1]] (+0.68, fdr 7e-06); moves opposite to [[PPT1]] (-0.64, fdr 1e-05), [[TMED7]] (-0.62, fdr 1e-05), [[PGAM1]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.57×** | +12.4 | 2e-32 | 29/35 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.36×** | +5.9 | 1e-06 | 17/35 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.31×** | +5.5 | 6e-06 | 22/41 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.16×** | +5.1 | 6e-05 | 0/4 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.9 | 1e-04 | 6/16 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.90×** | +4.4 | 0.001 | 11/27 (SW1417, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.2 | 0.002 | 11/36 (HepG2/C3A, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.82×** | +4.1 | 0.003 | 5/18 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.29×** | +3.7 | 0.015 | 6/26 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +3.5 | 0.028 | 10/46 (SNU-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.12×** | +3.3 | 0.049 | 2/12 (NCI-H23, HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.56× | +3.0 | 0.12 | 8/36 (SW1417, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.654× | -3.0 | 0.93 | 7/46 (SW 900, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +12.2) | — |
| [[A498 (line)]] | wt | 2.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 2.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +12.2) | — |
| [[A-427 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MROH6]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[CDK3]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.68 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[FBXL6]] | +0.68 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[LCAT]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[EIF4EBP3]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SEMA4C]] | +0.62 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[ZNF316]] | +0.61 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[NUDT4]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NBPF19]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[STARD10]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[PAQR6]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | -0.64 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[TMED7]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[PGAM1]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[PAICS]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[BPNT2]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SLC39A6]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[RPE]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SCARB2]] | -0.56 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SUMO1]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[AIDA]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (24.2, -8.9); signed map (2.5, -10.6). **Vector** length 54.0, 7.89% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[Erlotinib (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | Lck interacting transmembrane adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,736,283-63,739,103 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20406, dJ583P15.4, LIME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H400](https://www.uniprot.org/uniprotkb/Q9H400) (Lck-interacting transmembrane adapter 1):

> Involved in BCR (B-cell antigen receptor)-mediated signaling in B-cells and TCR (T-cell antigen receptor)-mediated T-cell signaling in T-cells. In absence of TCR signaling, may be involved in CD4-mediated inhibition of T-cell activation. Couples activation of these receptors and their associated kinases with distal intracellular events such as calcium mobilization or MAPK activation through the recruitment of PLCG2, GRB2, GRAP2, and other signaling molecules.

**Summary**, from NCBI Gene [54923](https://www.ncbi.nlm.nih.gov/gene/54923):

> This gene encodes a transmembrane adaptor protein that links the T and B-cell receptor stimulation to downstream signaling pathways via its association with the Src family kinases Lck and Lyn, respectively. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Mar 2015]

**Accessions** — [HGNC:26016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26016) · Entrez [54923](https://www.ncbi.nlm.nih.gov/gene/54923) · UniProt [Q9H400](https://www.uniprot.org/uniprotkb/Q9H400) · Ensembl [ENSG00000203896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203896)

## Data

Gene col 12800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12800); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12800]; `tensor/DDL_lfc|DDL_z.npy` [12800]; `embed/gene_vectors.npy` [12800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12800 or target_col == 12800). Every well: [[LIME1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIME1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
