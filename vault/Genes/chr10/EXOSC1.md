---
symbol: "EXOSC1"
type: "gene"
col: 10090
ensembl_id: "ENSG00000171311"
name: "exosome component 1"
location: "10q24.1"
module: 3
arm: "+"
pooled_cpm: 19.76
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# EXOSC1

*exosome component 1* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.58× (z +5.8, q 3e-06, up in 32 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +5.7, q 3e-06, up in 26 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (BT-474 0.0764×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.437×; ⚠ cell-cycle shift, explains ~0% of this change); [[Menadione (drug)]] 5 µM in 1 line (AN3 CA 0.0853×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL55]] (+0.68, fdr 1e-05), [[CCDC167]] (+0.66, fdr 1e-05), [[MTIF3]] (+0.66, fdr 1e-05); moves opposite to [[PIEZO1]] (-0.61, fdr 2e-05), [[SFPQ]] (-0.58, fdr 8e-05), [[HMGN1]] (-0.57, fdr 8e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.8 | 3e-06 | 32/44 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.7 | 3e-06 | 26/47 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.50×** | +5.3 | 2e-05 | 26/47 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 3e-05 | 29/47 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 2e-04 | 26/47 (PANC-1, HOP62, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +4.7 | 2e-04 | 25/48 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.38×** | +4.2 | 0.002 | 22/48 (LS 180, A-172, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.003 | 22/47 (PANC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.31×** | +3.4 | 0.037 | 15/45 (SNU-1, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.043 | 21/47 (HCT15, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.28×** | +3.3 | 0.050 | 16/48 (LoVo, LS 180, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.085 | 14/47 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.1 | 0.085 | 22/47 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.085 | 8/48 (SW480, LoVo, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.095 | 16/47 (NCI-H1573, A549, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (BT-474 0.0764×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.437×; ⚠ cell-cycle shift, explains ~0% of this change); [[Menadione (drug)]] 5 µM in 1 line (AN3 CA 0.0853×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 19.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +9.4) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[A498 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 30.0 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0853× (z -9.2) |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0764× (z -11.4) |
| [[A-172 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL55]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[CCDC167]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TMEM208]] | +0.65 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[MRPL43]] | +0.65 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SCNM1]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 | STRING 521 |
| [[TMEM11]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[RWDD1]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SEC61B]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIEZO1]] | -0.61 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[SFPQ]] | -0.58 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[HMGN1]] | -0.57 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[RBM12]] | -0.56 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.56 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[YWHAZ]] | -0.55 | -0.32 / -0.62 | both halves | 2e-04 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[YWHAE]] | -0.55 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[PRRC2B]] | -0.55 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[MYH9]] | -0.54 | -0.40 / -0.61 | both halves | 5e-05 | pathway: Affinity selection of immunoglobulins |
| [[WDR1]] | -0.54 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[SRSF1]] | -0.53 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[CDC42]] | -0.53 | -0.34 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.4, -12.7); signed map (-46.3, 18.2). **Vector** length 69.0, 13.4% of its response variance represented; |z| ≥ 3 in 603 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.2 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.3 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | +1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:97,435,909-97,446,017 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hCsl4p, Csl4p, CSL4, Ski4p, SKI4, CGI-108, p13 |
| Gene groups (HGNC) | Exosome complex |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3B2](https://www.uniprot.org/uniprotkb/Q9Y3B2) (Exosome complex component CSL4):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [51013](https://www.ncbi.nlm.nih.gov/gene/51013):

> This gene encodes a core component of the exosome. The mammalian exosome is required for rapid degradation of AU rich element-containing RNAs but not for poly(A) shortening. The association of this protein with the exosome is mediated by protein-protein interactions with ribosomal RNA-processing protein 42 and ribosomal RNA-processing protein 46. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:17286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17286) · Entrez [51013](https://www.ncbi.nlm.nih.gov/gene/51013) · UniProt [Q9Y3B2](https://www.uniprot.org/uniprotkb/Q9Y3B2) · Ensembl [ENSG00000171311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171311)

## Data

Gene col 10090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10090); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10090]; `tensor/DDL_lfc|DDL_z.npy` [10090]; `embed/gene_vectors.npy` [10090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10090 or target_col == 10090). Every well: [[EXOSC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
