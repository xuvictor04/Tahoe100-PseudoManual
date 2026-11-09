---
symbol: "CINP"
type: "gene"
col: 2032
ensembl_id: "ENSG00000100865"
name: "cyclin dependent kinase 2 interacting protein"
location: "14q32.31"
module: 12
arm: "+"
pooled_cpm: 16.89
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CINP

*cyclin dependent kinase 2 interacting protein* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.52× (z +4.7, q 0.001, up in 24 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.89× (z +3.7, q 0.032, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 4.74×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.740× (z -4.7, q 0.001, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C18orf21]] (+0.85, fdr 7e-06), [[NDUFA8]] (+0.82, fdr 7e-06), [[MPHOSPH10]] (+0.77, fdr 7e-06); moves opposite to [[SUMO3]] (-0.61, fdr 4e-05), [[MOB1A]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2032.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 4.74×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.52×** | +4.7 | 0.001 | 24/42 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.54×** | +4.6 | 0.001 | 18/28 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +3.7 | 0.032 | 20/48 (RKO, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.032 | 20/48 (BT-474, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.34× | +3.2 | 0.12 | 17/47 (NCI-H1573, NCI-H2030, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.23× | +3.2 | 0.12 | 11/48 (A-172, BT-474, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | 1.33× | +3.2 | 0.13 | 17/43 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -4.7 | 0.001 | 25/47 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -4.5 | 0.002 | 28/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.708×** | -3.8 | 0.023 | 20/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.750× | -3.2 | 0.19 | 19/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.759× | -3.1 | 0.24 | 17/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 17.4 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -13.0) |
| [[C32 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0643× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C18orf21]] | +0.85 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[NDUFA8]] | +0.82 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[DHX57]] | +0.77 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | +0.75 | +0.67 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RBSN]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[REXO4]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PUS3]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RP9]] | +0.73 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[MRPL21]] | +0.72 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[FRA10AC1]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[PRPF6]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO3]] | -0.61 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[MOB1A]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.789). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.8, -8.7); signed map (-16.7, -8.7). **Vector** length 70.3, 14.8% of its response variance represented; |z| ≥ 3 in 537 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.0 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | +0.2 |
|  | [[Ivermectin (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 2 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.31 — chr14:102,341,102-102,362,916 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC849 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW66](https://www.uniprot.org/uniprotkb/Q9BW66) (Cyclin-dependent kinase 2-interacting protein):

> Component of the DNA replication complex, which interacts with two kinases, CDK2 and CDC7, thereby providing a functional and physical link between CDK2 and CDC7 during firing of the origins of replication. Regulates ATR-mediated checkpoint signaling in response to DNA damage. Part of the 55LCC heterohexameric ATPase complex which is chromatin-associated and promotes replisome proteostasis to maintain replication fork progression and genome stability. Required for replication fork progression, …

**Summary**, from NCBI Gene [51550](https://www.ncbi.nlm.nih.gov/gene/51550):

> The protein encoded by this gene is reported to be a component of the DNA replication complex as well as a genome-maintenance protein. It may interact with proteins important for replication initiation and has been shown to bind chromatin at the G1 phase of the cell cycle and dissociate from chromatin with replication initiation. It may also serve to regulate checkpoint signaling as part of the DNA damage response. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:23789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23789) · Entrez [51550](https://www.ncbi.nlm.nih.gov/gene/51550) · UniProt [Q9BW66](https://www.uniprot.org/uniprotkb/Q9BW66) · Ensembl [ENSG00000100865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100865)

## Data

Gene col 2032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2032); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2032]; `tensor/DDL_lfc|DDL_z.npy` [2032]; `embed/gene_vectors.npy` [2032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2032 or target_col == 2032). Every well: [[CINP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CINP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
