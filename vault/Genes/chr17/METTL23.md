---
symbol: "METTL23"
type: "gene"
col: 11163
ensembl_id: "ENSG00000181038"
name: "methyltransferase 23, arginine"
location: "17q25.2"
module: 20
arm: "-"
pooled_cpm: 23.12
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# METTL23

*methyltransferase 23, arginine* — 17q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.73× (z +4.9, q 6e-04, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 3.56×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 5.57×; ⚠ cell-cycle shift, explains ~49% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.343× (z -5.0, q 3e-04, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTG1]] (+0.68, fdr 7e-06), [[TMEM205]] (+0.67, fdr 7e-06), [[MFAP1]] (+0.67, fdr 7e-06); moves opposite to [[RPSA]] (-0.67, fdr 7e-06), [[EIF3F]] (-0.67, fdr 2e-04), [[CTSZ]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11163.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 3.56×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 5.57×; ⚠ cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.73×** | +4.9 | 6e-04 | 30/47 (A-172, KATO III, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +3.6 | 0.057 | 23/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.48×** | +3.6 | 0.057 | 20/45 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.28× | +3.3 | 0.15 | 22/48 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.22 | 21/47 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.343×** | -5.0 | 3e-04 | 38/45 (SNU-423, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.592×** | -4.9 | 3e-04 | 28/47 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.361×** | -4.7 | 4e-04 | 37/48 (PANC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -4.4 | 0.002 | 29/47 (NCI-H1792, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.667×** | -3.8 | 0.020 | 23/48 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -3.3 | 0.098 | 21/44 (J82, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.714× | -3.1 | 0.14 | 22/47 (SNU-1, AN3 CA, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -11.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0646× (z -9.6) |
| [[A-427 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTG1]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TMEM205]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[MED19]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[FOXA2]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[OFD1]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[NBPF10]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | +0.64 | +0.41 / +0.68 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ACAP1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MRPL36]] | +0.63 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[EID2]] | +0.62 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[FOXD1]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | -0.67 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[EIF3F]] | -0.67 | -0.31 / -0.78 | both halves | 2e-04 |  |
| [[CTSZ]] | -0.67 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.65 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[RPN1]] | -0.64 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.64 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[COPS7B]] | -0.63 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[PPT1]] | -0.63 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[CIZ1]] | -0.62 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.62 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[DHFR]] | -0.62 | -0.40 / -0.68 | both halves | 5e-05 |  |
| [[ARPP19]] | -0.61 | -0.52 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.3, -25.3); signed map (-3.7, 10.0). **Vector** length 86.2, 23.2% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.5 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.3 | +2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.9 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Omeprazole (sodium) (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.8 | +0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 23, arginine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.2 — chr17:76,726,830-76,733,936 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC124512; previously C17orf95 |
| Gene groups (HGNC) | 7BS protein arginine methyltranferases; Arginine methyltransferases |
| Reactome | 3 pathways, smallest: Replacement of protamines by nucleosomes in the male pronucleus; Chromatin modifications during the maternal to zygotic transition (MZT); Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XA0](https://www.uniprot.org/uniprotkb/Q86XA0) (Histone-arginine methyltransferase METTL23):

> Histone methyltransferase that dimethylates histone H3 at 'Arg-17', forming asymmetric dimethylarginine (H3R17me2a), leading to activate transcription via chromatin remodeling (By similarity). Maternal factor involved in epigenetic chromatin reprogramming of the paternal genome in the zygote: mediates H3R17me2a, promoting histone H3.3 incorporation in the male pronucleus, leading to TET3 recruitment and subsequent DNA demethylation (By similarity).

**Summary**, from NCBI Gene [124512](https://www.ncbi.nlm.nih.gov/gene/124512):

> The protein encoded by this gene functions as a transcription factor regulator in the transcriptional pathway for human cognition. It is a partner of the alpha subunit of the GA-binding protein transcription factor. Mutations in this gene cause mild autosomal recessive intellectual disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2014]

**Accessions** — [HGNC:26988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26988) · Entrez [124512](https://www.ncbi.nlm.nih.gov/gene/124512) · UniProt [Q86XA0](https://www.uniprot.org/uniprotkb/Q86XA0) · Ensembl [ENSG00000181038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181038)

## Data

Gene col 11163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11163); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11163]; `tensor/DDL_lfc|DDL_z.npy` [11163]; `embed/gene_vectors.npy` [11163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11163 or target_col == 11163). Every well: [[METTL23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
