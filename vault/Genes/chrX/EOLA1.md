---
symbol: "EOLA1"
type: "gene"
col: 12433
ensembl_id: "ENSG00000197620"
name: "endothelium and lymphocyte associated ASCH domain 1"
location: "Xq28"
module: 103
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# EOLA1

*endothelium and lymphocyte associated ASCH domain 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +5.0, q 3e-04, up in 18 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.519× (z -4.7, q 0.001, down in 17 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EOLA2]] (+0.79, fdr 7e-06), [[CRYBB2P1]] (+0.74, fdr 7e-06), [[ALKBH5]] (+0.63, fdr 7e-06); moves opposite to [[GPATCH8]] (-0.56, fdr 1e-05), [[SLC25A13]] (-0.54, fdr 1e-05), [[TFAM]] (-0.52, fdr 2e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.0 | 3e-04 | 18/35 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.519×** | -4.7 | 0.001 | 17/39 (hTERT-HPNE, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -3.8 | 0.037 | 14/26 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.620×** | -3.6 | 0.064 | 9/20 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.635×** | -3.4 | 0.094 | 6/44 (MIA PaCa-2, HCT15, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.641×** | -3.3 | 0.098 | 15/44 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.664× | -3.1 | 0.20 | 10/42 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.78 | 0 | 1 | — | [[4EGI-1 (drug)]] 0.05 µM 0.0512× (z -10.0) |
| [[A-172 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOLA2]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 | STRING 877 |
| [[CRYBB2P1]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ALKBH5]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PRSS53]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[HK2]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[CLK3]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[TIMM10B]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SEC24C]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[HYOU1]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[AJM1]] | +0.58 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[EEF1AKMT3]] | +0.57 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH8]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TFAM]] | -0.52 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[RPL7L1]] | -0.51 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[FJX1]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[DIP2B]] | -0.49 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[ANKRD17]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.2, -23.0); signed map (-40.5, 25.2). **Vector** length 54.6, 7.18% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | -3.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.2 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | -0.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.2 | -2.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.8 | -3.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.6 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | endothelium and lymphocyte associated ASCH domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:149,540,355-149,550,510 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CXorf40, CXorf40A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE69](https://www.uniprot.org/uniprotkb/Q8TE69) (Protein EOLA1):

> May play a role in cell protection during the inflammatory response. In epithelial cells, negatively regulates IL6 production and apoptosis through the regulation of MT2A expression.

**Summary**, from NCBI Gene [91966](https://www.ncbi.nlm.nih.gov/gene/91966):

> Involved in regulation of interleukin-6 production. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28089) · Entrez [91966](https://www.ncbi.nlm.nih.gov/gene/91966) · UniProt [Q8TE69](https://www.uniprot.org/uniprotkb/Q8TE69) · Ensembl [ENSG00000197620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197620)

## Data

Gene col 12433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12433); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12433]; `tensor/DDL_lfc|DDL_z.npy` [12433]; `embed/gene_vectors.npy` [12433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12433 or target_col == 12433). Every well: [[EOLA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EOLA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
