---
symbol: "ANKRD30BL"
type: "gene"
col: 8623
ensembl_id: "ENSG00000163046"
name: "ankyrin repeat domain 30B like"
location: "2q21.2"
module: 20
arm: "+"
pooled_cpm: 2.8
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ANKRD30BL

*ankyrin repeat domain 30B like* — 2q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.37× (z +6.8, q 5e-09, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 1.61× (z +3.9, q 0.009, up in 17 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HFM1]] (+0.84, fdr 7e-06), [[RPL10]] (+0.79, fdr 7e-06), [[RPL18A]] (+0.78, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.70, fdr 7e-06), [[PIGBOS1]] (-0.65, fdr 7e-06), [[MRPS18B]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +6.8 | 5e-09 | 4/5 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +6.5 | 3e-08 | 9/16 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.20×** | +6.3 | 7e-08 | 5/6 (HOP62, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +4.3 | 0.002 | 10/17 (LOX-IMVI, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.9 | 0.009 | 9/25 (LoVo, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.009 | 17/46 (SW 900, A498, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.019 | 14/33 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.571× | -3.3 | 0.40 | 11/31 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.570× | -3.2 | 0.40 | 11/41 (COLO 205, HS-578T, …) | top dose only | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HFM1]] | +0.84 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RPL10]] | +0.79 | +0.72 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[RPL18A]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RPS18]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[EEF1A1P5]] | +0.77 | +0.67 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[DHFR]] | +0.76 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC03009]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MTX1]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RPSA]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RPL4]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.70 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.65 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[MRPS18B]] | -0.63 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[RBMX2]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[GGNBP2]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.58 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[NKAP]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PHACTR4]] | -0.57 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[ZNF503]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[NEMF]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[ESF1]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ADPRS]] | -0.57 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.6, -25.2); signed map (-21.3, -34.4). **Vector** length 51.2, 6.39% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.59 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.59 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.61 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +0.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.2 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.4 | -1.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Darolutamide (drug)]] 0.05 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 30B like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.2 — chr2:132,147,591-132,257,969 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NCRNA00164, ANKRD30BP3 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [A7E2S9](https://www.uniprot.org/uniprotkb/A7E2S9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35167) · Entrez [554226](https://www.ncbi.nlm.nih.gov/gene/554226) · UniProt [A7E2S9](https://www.uniprot.org/uniprotkb/A7E2S9) · Ensembl [ENSG00000163046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163046)

## Data

Gene col 8623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8623); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8623]; `tensor/DDL_lfc|DDL_z.npy` [8623]; `embed/gene_vectors.npy` [8623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8623 or target_col == 8623). Every well: [[ANKRD30BL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD30BL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
