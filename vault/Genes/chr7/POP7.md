---
symbol: "POP7"
type: "gene"
col: 10241
ensembl_id: "ENSG00000172336"
name: "POP7 ribonuclease P/MRP subunit"
location: "7q22.1"
module: 54
arm: "+"
pooled_cpm: 6.68
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# POP7

*POP7 ribonuclease P/MRP subunit* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.62× (z +7.8, q 3e-12, up in 33 of 35 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.559× (z -5.2, q 1e-04, down in 29 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.107×, SW480 0.119×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.136×); [[Verteporfin (drug)]] 5 µM in 1 line (J82 0.0756×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHCHD1]] (+0.80, fdr 1e-05), [[NCBP2AS2]] (+0.80, fdr 1e-05), [[SF3B5]] (+0.78, fdr 3e-05, ⚠ SF3B5 in the vector space only through flagged drug-doses), [[MRPS12]] (+0.77, fdr 1e-05); moves opposite to [[CROCC]] (-0.73, fdr 2e-05), [[PRKAR1A]] (-0.68, fdr 6e-05), [[CCDC200]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.62×** | +7.8 | 3e-12 | 33/35 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.89×** | +4.0 | 0.016 | 18/33 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.81×** | +3.7 | 0.034 | 18/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.75×** | +3.5 | 0.058 | 25/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.64× | +3.1 | 0.19 | 20/47 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.61× | +3.0 | 0.23 | 14/41 (A549, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10241.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.107×, SW480 0.119×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.136×); [[Verteporfin (drug)]] 5 µM in 1 line (J82 0.0756×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.559×** | -5.2 | 1e-04 | 29/41 (NCI-H2030, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | 0.400× | -3.0 | 0.69 | 14/46 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.6) |
| [[J82 (line)]] | alt | 6.34 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0756× (z -9.1) |
| [[SW480 (line)]] | alt | 8.95 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 10 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD1]] | +0.80 | +0.55 / +0.83 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.80 | +0.52 / +0.86 | both halves | 1e-05 |  |
| [[SF3B5]] ⚠ | +0.78 | +0.45 / +0.84 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL41]] ⚠ | +0.77 | +0.47 / +0.80 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS12]] | +0.77 | +0.52 / +0.80 | both halves | 1e-05 |  |
| [[C16orf91]] | +0.77 | +0.40 / +0.84 | both halves | 5e-05 |  |
| [[SDHAF1]] | +0.77 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[SAC3D1]] | +0.76 | +0.50 / +0.79 | both halves | 1e-05 |  |
| [[PET117]] | +0.76 | +0.45 / +0.77 | both halves | 3e-05 |  |
| [[MRPL55]] | +0.75 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[LSM2]] | +0.75 | +0.56 / +0.78 | both halves | 1e-05 |  |
| [[EMC6]] | +0.74 | +0.31 / +0.82 | both halves | 2e-04 |  |
| [[EIF4E2]] | +0.74 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.74 | +0.47 / +0.78 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCC]] | -0.73 | -0.46 / -0.67 | both halves | 2e-05 |  |
| [[PRKAR1A]] | -0.68 | -0.38 / -0.67 | both halves | 6e-05 |  |
| [[CCDC200]] | -0.67 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[CYB5D2]] | -0.64 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[ATN1]] | -0.62 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[ZNF655]] | -0.62 | -0.31 / -0.62 | both halves | 2e-04 |  |
| [[LYRM1]] | -0.62 | -0.32 / -0.64 | both halves | 2e-04 |  |
| [[SDCBP2-AS1]] | -0.61 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[CHMP3]] | -0.61 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[CHD3]] | -0.61 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[IL6ST]] | -0.61 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[TUG1]] | -0.61 | -0.42 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.888). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.8, -12.5); signed map (-33.7, 4.2). **Vector** length 63.5, 13.6% of its response variance represented; |z| ≥ 3 in 481 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.70 to 9); *Mitochondrial translation* (reactome, mean cos +0.70 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.70 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.5 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +2.2 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +2.1 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.8 | +1.0 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +0.8 | +2.5 |
|  | [[Bendamustine (drug)]] 5 µM |  | +0.8 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.8 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.1 | -0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | POP7 ribonuclease P/MRP subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,706,121-100,707,486 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPP20, RPP2 |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Hallmark sets | E2F_TARGETS |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O75817](https://www.uniprot.org/uniprotkb/O75817) (Ribonuclease P protein subunit p20):

> Component of ribonuclease P, a ribonucleoprotein complex that generates mature tRNA molecules by cleaving their 5'-ends. Also a component of the MRP ribonuclease complex, which cleaves pre-rRNA sequences.

**Summary**, from NCBI Gene [10248](https://www.ncbi.nlm.nih.gov/gene/10248):

> Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Located in nucleolus. Part of multimeric ribonuclease P complex and ribonuclease MRP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19949) · Entrez [10248](https://www.ncbi.nlm.nih.gov/gene/10248) · UniProt [O75817](https://www.uniprot.org/uniprotkb/O75817) · Ensembl [ENSG00000172336](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172336)

## Data

Gene col 10241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10241); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10241]; `tensor/DDL_lfc|DDL_z.npy` [10241]; `embed/gene_vectors.npy` [10241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10241 or target_col == 10241). Every well: [[POP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
