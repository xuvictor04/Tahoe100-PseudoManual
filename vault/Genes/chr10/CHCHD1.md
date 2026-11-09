---
symbol: "CHCHD1"
type: "gene"
col: 10271
ensembl_id: "ENSG00000172586"
name: "coiled-coil-helix-coiled-coil-helix domain containing 1"
location: "10q22.2"
module: 54
arm: "+"
pooled_cpm: 13.2
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

# CHCHD1

*coiled-coil-helix-coiled-coil-helix domain containing 1* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.27× (z +5.3, q 5e-05, up in 32 of 40 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.523× (z -6.2, q 3e-07, down in 37 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.292×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCR10]] (+0.84, fdr 7e-06, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[LAMTOR5]] (+0.81, fdr 7e-06), [[POP7]] (+0.80, fdr 1e-05), [[EMC6]] (+0.77, fdr 1e-04); moves opposite to [[MAPRE1]] (-0.66, fdr 4e-05), [[WDR1]] (-0.64, fdr 1e-05), [[SFPQ]] (-0.63, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.3 | 5e-05 | 32/40 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **2.02×** | +4.8 | 4e-04 | 31/41 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.14×** | +4.7 | 4e-04 | 26/37 (NCI-H460, A498, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.82×** | +3.9 | 0.012 | 16/28 (A498, CFPAC-1, …) | two highest doses | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.59× | +3.2 | 0.18 | 18/45 (NCI-H2347, HT-29, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.38× | +3.1 | 0.20 | 20/48 (PANC-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10271.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.292×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.523×** | -6.2 | 3e-07 | 37/46 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.363× | -3.3 | 0.27 | 23/43 (C-33 A, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.612× | -3.1 | 0.28 | 16/47 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.636× | -3.1 | 0.28 | 20/44 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -8.5) |
| [[A-172 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 22 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCR10]] ⚠ | +0.84 | +0.66 / +0.90 | both halves | 7e-06 | STRING 489; ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | +0.81 | +0.59 / +0.87 | both halves | 7e-06 |  |
| [[POP7]] | +0.80 | +0.55 / +0.83 | both halves | 1e-05 |  |
| [[EMC6]] | +0.77 | +0.33 / +0.86 | both halves | 1e-04 |  |
| [[ATP5MJ]] | +0.77 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.77 | +0.49 / +0.82 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LSM2]] | +0.76 | +0.55 / +0.83 | both halves | 1e-05 |  |
| [[ROMO1]] | +0.76 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | +0.76 | +0.49 / +0.80 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NCBP2AS2]] | +0.75 | +0.58 / +0.79 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.74 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[C4orf48]] | +0.74 | +0.49 / +0.81 | both halves | 1e-05 |  |
| [[NDUFB4]] | +0.73 | +0.46 / +0.79 | both halves | 2e-05 | STRING 551 |
| [[ATP5MK]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 | STRING 485 |
| [[GADD45GIP1]] | +0.72 | +0.31 / +0.82 | both halves | 2e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 922 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.66 | -0.42 / -0.72 | both halves | 4e-05 |  |
| [[WDR1]] | -0.64 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.63 | -0.32 / -0.66 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.832). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.2, -19.5); signed map (-32.2, 8.0). **Vector** length 57.6, 13.5% of its response variance represented; |z| ≥ 3 in 432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.6 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -4.8 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -4.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil-helix-coiled-coil-helix domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,782,047-73,783,652 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25854, mS37; previously C10orf34 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins; Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q96BP2](https://www.uniprot.org/uniprotkb/Q96BP2) carries no function annotation.

**Summary**, from NCBI Gene [118487](https://www.ncbi.nlm.nih.gov/gene/118487):

> Enables RNA binding activity. Predicted to be involved in mitochondrial translation. Located in fibrillar center; mitochondrion; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23518) · Entrez [118487](https://www.ncbi.nlm.nih.gov/gene/118487) · UniProt [Q96BP2](https://www.uniprot.org/uniprotkb/Q96BP2) · Ensembl [ENSG00000172586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172586)

## Data

Gene col 10271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10271); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10271]; `tensor/DDL_lfc|DDL_z.npy` [10271]; `embed/gene_vectors.npy` [10271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10271 or target_col == 10271). Every well: [[CHCHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHCHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
