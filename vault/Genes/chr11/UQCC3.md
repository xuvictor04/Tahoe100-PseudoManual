---
symbol: "UQCC3"
type: "gene"
col: 12934
ensembl_id: "ENSG00000204922"
name: "ubiquinol-cytochrome c reductase complex assembly factor 3"
location: "11q12.3"
module: 24
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# UQCC3

*ubiquinol-cytochrome c reductase complex assembly factor 3* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.98× (z +6.5, q 4e-08, up in 28 of 30 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.94× (z +4.1, q 0.005, up in 22 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNLZ]] (+0.72, fdr 1e-05), [[SNHG9]] (+0.72, fdr 1e-05), [[CHCHD1]] (+0.70, fdr 4e-05); moves opposite to [[LIN7C]] (-0.61, fdr 4e-04), [[DHFR]] (-0.59, fdr 0.002, ⚠ one half only (not replicated)), [[IPO5]] (-0.59, fdr 5e-05), [[TWF1]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.98×** | +6.5 | 4e-08 | 28/30 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.54×** | +5.8 | 2e-06 | 20/27 (LoVo, A549, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **2.51×** | +5.7 | 2e-06 | 22/30 (CFPAC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.38×** | +5.2 | 3e-05 | 3/13 (NCI-H2030, PANC-1, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +4.1 | 0.005 | 22/44 (HT-29, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.013 | 17/39 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.54× | +3.2 | 0.10 | 10/41 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.42× | +3.1 | 0.15 | 13/46 (HEC-1-A, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 26 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNLZ]] | +0.72 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.72 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[CHCHD1]] | +0.70 | +0.41 / +0.77 | both halves | 4e-05 | STRING 509 |
| [[RANGRF]] | +0.69 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[NCBP2AS2]] | +0.69 | +0.48 / +0.76 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | +0.69 | +0.38 / +0.78 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2H]] | +0.69 | +0.37 / +0.76 | both halves | 8e-05 |  |
| [[LAGE3]] | +0.68 | +0.46 / +0.76 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | +0.68 | +0.37 / +0.77 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SCAND1]] | +0.67 | +0.46 / +0.76 | both halves | 3e-05 |  |
| [[EMC6]] | +0.66 | +0.32 / +0.76 | both halves | 1e-04 |  |
| [[POP7]] | +0.66 | +0.28 / +0.77 | both halves | 3e-04 |  |
| [[MINCR]] | +0.65 | +0.35 / +0.75 | both halves | 1e-04 |  |
| [[LAMTOR4]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.61 | -0.25 / -0.71 | both halves | 4e-04 |  |
| [[DHFR]] | -0.59 | -0.14 / -0.74 | ⚠ one half (not replicated) | 0.002 |  |
| [[IPO5]] | -0.59 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[TWF1]] | -0.58 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[MACROH2A1]] | -0.57 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[OCRL]] | -0.57 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[UGGT1]] | -0.57 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[DNAJC10]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[NONO]] | -0.57 | -0.31 / -0.67 | both halves | 2e-04 |  |
| [[API5]] | -0.56 | -0.30 / -0.64 | both halves | 2e-04 |  |
| [[WDR1]] | -0.56 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[ACTR3]] | -0.56 | -0.25 / -0.65 | both halves | 4e-04 |  |
| [[DCTN1]] | -0.56 | -0.33 / -0.62 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.4, -20.2); signed map (-29.7, 8.5). **Vector** length 50.9, 8.86% of its response variance represented; |z| ≥ 3 in 551 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -1.8 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -1.8 | +5.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase complex assembly factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,670,273-62,673,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ655; previously C11orf83 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UW78](https://www.uniprot.org/uniprotkb/Q6UW78) (Ubiquinol-cytochrome-c reductase complex assembly factor 3):

> Required for the assembly of the ubiquinol-cytochrome c reductase complex (mitochondrial respiratory chain complex III or cytochrome b-c1 complex), mediating cytochrome b recruitment and probably stabilization within the complex. Thereby, plays an important role in ATP production by mitochondria. Cardiolipin-binding protein, it may also control the cardiolipin composition of mitochondria membranes and their morphology.

**Summary**, from NCBI Gene [790955](https://www.ncbi.nlm.nih.gov/gene/790955):

> Complex III is a mitochondrial inner membrane protein complex that transfers electrons from ubiquinol to cytochrome c. This gene encodes a protein that functions in complex III assembly. Mutations in this gene result in Mitochondrial complex III deficiency, nuclear type 9. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:34399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34399) · Entrez [790955](https://www.ncbi.nlm.nih.gov/gene/790955) · UniProt [Q6UW78](https://www.uniprot.org/uniprotkb/Q6UW78) · Ensembl [ENSG00000204922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204922)

## Data

Gene col 12934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12934); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12934]; `tensor/DDL_lfc|DDL_z.npy` [12934]; `embed/gene_vectors.npy` [12934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12934 or target_col == 12934). Every well: [[UQCC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
