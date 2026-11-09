---
symbol: "SPATC1"
type: "gene"
col: 11833
ensembl_id: "ENSG00000186583"
name: "spermatogenesis and centriole associated 1"
location: "8q24.3"
module: 21
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SPATC1

*spermatogenesis and centriole associated 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.89× (z +12.2, q 1e-31, up in 32 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB14]] (+0.84, fdr 7e-06), [[EAF1-AS1]] (+0.84, fdr 7e-06), [[PKD2L2]] (+0.82, fdr 7e-06); moves opposite to [[PPP5C]] (-0.71, fdr 7e-06), [[ICMT]] (-0.69, fdr 1e-05), [[RPE]] (-0.69, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +12.2 | 1e-31 | 32/34 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +9.9 | 2e-20 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +8.0 | 3e-13 | 7/13 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +6.9 | 7e-10 | 23/35 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.9 | 1e-04 | 3/13 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.005 | 13/41 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.032 | 10/34 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.3 | 0.067 | 5/14 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +3.2 | 0.081 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.48× | +3.1 | 0.12 | 5/28 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11833.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -3.1 | 0.68 | 11/47 (HT-29, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB14]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[EAF1-AS1]] | +0.84 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.82 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.81 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.81 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.78 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[USH2A]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.76 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | +0.76 | +0.70 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TOMM20L-DT]] | +0.76 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.76 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.76 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[TTC36-AS1]] | +0.76 | +0.78 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP5C]] | -0.71 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[ICMT]] | -0.69 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[RPE]] | -0.69 | -0.61 / -0.72 | both halves | 7e-06 |  |
| [[PRPS1]] | -0.66 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[AGO1]] | -0.66 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[CS]] | -0.66 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, 26.5); signed map (31.9, 6.2). **Vector** length 42.0, 4.52% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis and centriole associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,012,280-144,047,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC61633, SPATA15, SPERIOLIN |
| Matched by | ensembl_id |

UniProt [Q76KD6](https://www.uniprot.org/uniprotkb/Q76KD6) carries no function annotation.

**Summary**, from NCBI Gene [375686](https://www.ncbi.nlm.nih.gov/gene/375686):

> Predicted to enable gamma-tubulin binding activity. Located in centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30510) · Entrez [375686](https://www.ncbi.nlm.nih.gov/gene/375686) · UniProt [Q76KD6](https://www.uniprot.org/uniprotkb/Q76KD6) · Ensembl [ENSG00000186583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186583)

## Data

Gene col 11833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11833); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11833]; `tensor/DDL_lfc|DDL_z.npy` [11833]; `embed/gene_vectors.npy` [11833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11833 or target_col == 11833). Every well: [[SPATC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
