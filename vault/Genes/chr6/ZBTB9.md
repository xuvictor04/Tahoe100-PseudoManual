---
symbol: "ZBTB9"
type: "gene"
col: 13115
ensembl_id: "ENSG00000213588"
name: "zinc finger and BTB domain containing 9"
location: "6p21.32"
module: 16
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZBTB9

*zinc finger and BTB domain containing 9* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.38× (z +11.6, q 4e-28, up in 38 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF574]] (+0.71, fdr 7e-06), [[GEMIN4]] (+0.69, fdr 7e-06), [[INTS5]] (+0.67, fdr 7e-06); moves opposite to [[SNX3]] (-0.57, fdr 1e-05), [[RAB6A]] (-0.56, fdr 1e-05), [[SOS1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.38×** | +11.6 | 4e-28 | 38/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.47×** | +8.6 | 3e-15 | 34/43 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +7.4 | 2e-11 | 18/35 (SNU-423, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +7.3 | 4e-11 | 19/31 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +6.9 | 7e-10 | 6/11 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.94×** | +6.3 | 3e-08 | 21/44 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.96×** | +6.1 | 8e-08 | 0/2 | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +5.2 | 1e-05 | 3/15 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.80×** | +5.1 | 2e-05 | 0/3 | inconsistent across doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.0 | 4e-05 | 8/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +4.8 | 1e-04 | 10/43 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +4.5 | 4e-04 | 8/45 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.3 | 7e-04 | 6/44 (A-172, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +4.3 | 7e-04 | 11/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +4.2 | 0.001 | 9/32 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +4.0 | 0.003 | 6/37 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.009 | 3/44 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.47×** | +3.3 | 0.025 | 6/24 (SK-MEL-2, J82, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +3.2 | 0.040 | 4/31 (KATO III, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Canagliflozin (drug)]] 0.5 µM |  | 0.727× | -3.1 | 0.94 | 4/43 (SW48, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 2.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 2.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +11.6) | — |
| [[A-172 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF574]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 | same gene group |
| [[GEMIN4]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[INTS5]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[NOL6]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC14]] | +0.64 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[REXO1]] | +0.64 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CHERP]] | +0.64 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CACTIN]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.63 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[GRWD1]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PUF60]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[CHTOP]] | +0.62 | +0.71 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX3]] | -0.57 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[SOS1]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[WWP1]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RTN3]] | -0.54 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[ALDH2]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[HINT1]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[PIK3C2A]] | -0.52 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[NAP1L1]] | -0.52 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ZMYM2]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ELF2]] | -0.51 | -0.55 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.8, -0.5); signed map (-0.9, -32.5). **Vector** length 39.7, 3.81% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.9 | +7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.6 | +4.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.4 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +1.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,453,970-33,457,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23166, ZNF919 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C00](https://www.uniprot.org/uniprotkb/Q96C00) (Zinc finger and BTB domain-containing protein 9):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [221504](https://www.ncbi.nlm.nih.gov/gene/221504):

> Enables identical protein binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28323) · Entrez [221504](https://www.ncbi.nlm.nih.gov/gene/221504) · UniProt [Q96C00](https://www.uniprot.org/uniprotkb/Q96C00) · Ensembl [ENSG00000213588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213588)

## Data

Gene col 13115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13115); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13115]; `tensor/DDL_lfc|DDL_z.npy` [13115]; `embed/gene_vectors.npy` [13115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13115 or target_col == 13115). Every well: [[ZBTB9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
