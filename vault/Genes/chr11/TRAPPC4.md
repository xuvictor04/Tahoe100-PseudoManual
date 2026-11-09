---
symbol: "TRAPPC4"
type: "gene"
col: 12258
ensembl_id: "ENSG00000196655"
name: "trafficking protein particle complex subunit 4"
location: "11q23.3"
module: 3
arm: "+"
pooled_cpm: 13.51
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TRAPPC4

*trafficking protein particle complex subunit 4* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.31× (z +7.3, q 2e-10, up in 34 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.68× (z +4.7, q 2e-04, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.233× (z -6.5, q 4e-08, down in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.05 µM in 1 line (BT-474 0.0599×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL41]] (+0.74, fdr 3e-05, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[POP7]] (+0.72, fdr 8e-05), [[RPL36AL]] (+0.70, fdr 3e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[CDC34]] (+0.70, fdr 1e-05), [[LSM2]] (+0.69, fdr 4e-05); moves opposite to [[YWHAE]] (-0.64, fdr 3e-05), [[DHFR]] (-0.63, fdr 2e-04), [[EEF1A1]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +7.3 | 2e-10 | 34/39 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.19×** | +7.1 | 4e-10 | 37/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.96×** | +6.1 | 2e-07 | 34/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.84×** | +5.5 | 5e-06 | 29/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.75×** | +5.1 | 4e-05 | 26/45 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +4.7 | 2e-04 | 32/44 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.68×** | +4.7 | 2e-04 | 27/42 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.54×** | +3.7 | 0.013 | 19/39 (J82, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.46×** | +3.4 | 0.041 | 20/45 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.44×** | +3.3 | 0.049 | 20/46 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12258.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.05 µM in 1 line (BT-474 0.0599×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.233×** | -6.5 | 4e-08 | 36/47 (A-427, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.305×** | -5.3 | 3e-05 | 34/43 (LOX-IMVI, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.706× | -3.1 | 0.31 | 11/48 (SK-MEL-2, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.21 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0599× (z -10.4) |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 25 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL41]] ⚠ | +0.74 | +0.45 / +0.77 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POP7]] | +0.72 | +0.37 / +0.79 | both halves | 8e-05 |  |
| [[RPL36AL]] ⚠ | +0.70 | +0.44 / +0.75 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDC34]] | +0.70 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[LSM2]] | +0.69 | +0.41 / +0.74 | both halves | 4e-05 |  |
| [[PUSL1]] | +0.69 | +0.42 / +0.74 | both halves | 4e-05 |  |
| [[LAMTOR5]] | +0.67 | +0.37 / +0.70 | both halves | 8e-05 |  |
| [[EMC6]] | +0.67 | +0.31 / +0.78 | both halves | 2e-04 | STRING 405 |
| [[PLEKHJ1]] | +0.66 | +0.45 / +0.73 | both halves | 3e-05 | same gene group |
| [[SF3B5]] ⚠ | +0.66 | +0.29 / +0.77 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CIAO2B]] | +0.65 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[CCNQ]] | +0.65 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[KRTCAP2]] | +0.64 | +0.42 / +0.69 | both halves | 4e-05 |  |
| [[CHCHD1]] | +0.63 | +0.23 / +0.77 | both halves | 5e-04 |  |
| [[RCE1]] | +0.63 | +0.46 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAE]] | -0.64 | -0.45 / -0.66 | both halves | 3e-05 | pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[DHFR]] | -0.63 | -0.31 / -0.71 | both halves | 2e-04 |  |
| [[EEF1A1]] | -0.62 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[PAPOLA]] | -0.62 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[GALC]] | -0.62 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[EWSR1]] | -0.62 | -0.32 / -0.65 | both halves | 2e-04 |  |
| [[EIF4B]] | -0.61 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[ACAA2]] | -0.61 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[PTGR2]] | -0.61 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[PCBP2]] | -0.60 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[VPS52]] | -0.59 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[U2AF2]] | -0.58 | -0.27 / -0.58 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.0, -17.9); signed map (-33.1, 4.3). **Vector** length 72.7, 16.6% of its response variance represented; |z| ≥ 3 in 650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +3.0 | +5.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.2 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.6 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.1 | +0.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.8 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,018,763-119,025,454 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRS23, SBDN, PTD009 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits; MicroRNA protein coding host genes |
| Reactome | 11 pathways, smallest: Syndecan interactions; COPII-mediated vesicle transport; Non-integrin membrane-ECM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y296](https://www.uniprot.org/uniprotkb/Q9Y296) (Trafficking protein particle complex subunit 4):

> Core component of the TRAPP complexes which has a function of guanine nucleotide exchange factor activity for Rab1 GTPase (Probable). Plays a role in vesicular transport from endoplasmic reticulum to Golgi and autophagy. May play a role in dendrite postsynaptic membrane trafficking (By similarity).

**Summary**, from NCBI Gene [51399](https://www.ncbi.nlm.nih.gov/gene/51399):

> Involved in autophagy and endoplasmic reticulum to Golgi vesicle-mediated transport. Part of TRAPP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19943) · Entrez [51399](https://www.ncbi.nlm.nih.gov/gene/51399) · UniProt [Q9Y296](https://www.uniprot.org/uniprotkb/Q9Y296) · Ensembl [ENSG00000196655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196655)

## Data

Gene col 12258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12258); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12258]; `tensor/DDL_lfc|DDL_z.npy` [12258]; `embed/gene_vectors.npy` [12258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12258 or target_col == 12258). Every well: [[TRAPPC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
