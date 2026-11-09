---
symbol: "WDR18"
type: "gene"
col: 778
ensembl_id: "ENSG00000065268"
name: "WD repeat domain 18"
location: "19p13.3"
module: 1
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# WDR18

*WD repeat domain 18* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +10.0, q 9e-21, up in 24 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.48× (z +4.0, q 0.006, up in 13 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.668× (z -4.2, q 0.013, down in 15 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRG2]] (+0.72, fdr 7e-06), [[IFRD2]] (+0.71, fdr 7e-06), [[IMP4]] (+0.69, fdr 7e-06); moves opposite to [[TMA7]] (-0.62, fdr 1e-05), [[ATP5F1E]] (-0.59, fdr 1e-05), [[GNAS]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +10.0 | 9e-21 | 24/29 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +9.2 | 1e-17 | 8/10 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.2 | 8e-08 | 12/15 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.8 | 3e-04 | 10/30 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.006 | 13/44 (C32, SK-MEL-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.27×** | +3.5 | 0.045 | 6/47 (Hs 766T, A-172, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.39×** | +3.4 | 0.058 | 11/33 (HCT15, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.080 | 10/42 (NCI-H1792, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.2 | 0.080 | 8/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 778.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -4.2 | 0.013 | 15/46 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -4.0 | 0.016 | 14/40 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.713×** | -3.6 | 0.072 | 12/46 (H4, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 0.734× | -3.2 | 0.15 | 13/46 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.737× | -3.2 | 0.15 | 13/42 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.748× | -3.1 | 0.21 | 11/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -12.3) |
| [[HT-29 (line)]] | alt | 5.17 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0706× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 6.72 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0665× (z -11.7) |
| [[PANC-1 (line)]] | alt | 6.72 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 7.48 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.117× (z -8.5) |
| [[SNU-1 (line)]] | wt | 6.78 | 0 | 1 | — | [[Bestatin (drug)]] 5 µM 0.0465× (z -9.0) |
| [[A-172 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRG2]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[IMP4]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 891 |
| [[RITA1]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[BCS1L]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PSMG1]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[HMBS]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MCRS1]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[BYSL]] | +0.63 | +0.58 / +0.63 | both halves | 8e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 729 |
| [[COX10]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SARS2]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMA7]] | -0.62 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[ATP5F1E]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[GNAS]] | -0.55 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[FGFR1OP2]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PTMA]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.0, -39.6); signed map (-2.9, -43.7). **Vector** length 49.6, 6.20% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.7 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.2 | +1.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Ciclopirox (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -0.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:984,332-998,438 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ipi3 |
| Gene groups (HGNC) | WD repeat domain containing; Large ribosomal subunit biogenesis complex |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV38](https://www.uniprot.org/uniprotkb/Q9BV38) (WD repeat-containing protein 18):

> Functions as a component of the Five Friends of Methylated CHTOP (5FMC) complex; the 5FMC complex is recruited to ZNF148 by methylated CHTOP, leading to desumoylation of ZNF148 and subsequent transactivation of ZNF148 target genes. Component of the PELP1 complex involved in the nucleolar steps of 28S rRNA maturation and the subsequent nucleoplasmic transit of the pre-60S ribosomal subunit. May play a role during development (By similarity).

**Summary**, from NCBI Gene [57418](https://www.ncbi.nlm.nih.gov/gene/57418):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17956) · Entrez [57418](https://www.ncbi.nlm.nih.gov/gene/57418) · UniProt [Q9BV38](https://www.uniprot.org/uniprotkb/Q9BV38) · Ensembl [ENSG00000065268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065268)

## Data

Gene col 778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 778); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 778]; `tensor/DDL_lfc|DDL_z.npy` [778]; `embed/gene_vectors.npy` [778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 778 or target_col == 778). Every well: [[WDR18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
