---
symbol: "BTBD1"
type: "gene"
col: 759
ensembl_id: "ENSG00000064726"
name: "BTB domain containing 1"
location: "15q25.2"
module: 25
arm: "+"
pooled_cpm: 64.53
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# BTBD1

*BTB domain containing 1* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.50× (z +6.5, q 5e-08, up in 28 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.47× (z +6.3, q 6e-08, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.197×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.353×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW 1271 0.0885×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.156×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPRIN1]] (+0.73, fdr 7e-06), [[ERLIN2]] (+0.69, fdr 6e-05), [[IPO5]] (+0.69, fdr 7e-06); moves opposite to [[FAM53C]] (-0.68, fdr 1e-05), [[INAFM1]] (-0.67, fdr 1e-05), [[RPL36AL]] (-0.66, fdr 4e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[RASSF7]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.5 | 5e-08 | 28/44 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.3 | 6e-08 | 40/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +6.3 | 6e-08 | 40/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +5.8 | 9e-07 | 33/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 7e-06 | 34/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.4 | 8e-06 | 28/49 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +5.1 | 3e-05 | 21/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 3e-05 | 27/48 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.6 | 2e-04 | 25/45 (A549, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.5 | 3e-04 | 28/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 7e-04 | 27/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 25/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | **1.21×** | +3.1 | 0.080 | 21/47 (LoVo, LS 180, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.084 | 16/47 (A549, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.197×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.353×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW 1271 0.0885×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.156×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 82.8 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.18× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~3% of this change | — |
| [[SW 1271 (line)]] | alt | 86.7 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0885× (z -9.8) |
| [[SW480 (line)]] | alt | 83.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 51.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 58.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.156× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 63.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -15.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.122× (z -8.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 95.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPRIN1]] | +0.73 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[ERLIN2]] | +0.69 | +0.38 / +0.75 | both halves | 6e-05 |  |
| [[IPO5]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[DARS2]] | +0.69 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[TMEM33]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[ATIC]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SLC25A24]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GUF1]] | +0.66 | +0.41 / +0.71 | both halves | 4e-05 |  |
| [[LIN7C]] | +0.66 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[DR1]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | +0.66 | +0.40 / +0.77 | both halves | 4e-05 |  |
| [[DHFR]] | +0.65 | +0.34 / +0.72 | both halves | 1e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53C]] | -0.68 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.67 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.66 | -0.42 / -0.70 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RASSF7]] | -0.66 | -0.43 / -0.74 | both halves | 3e-05 |  |
| [[LAMTOR5]] | -0.66 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[RNF181]] | -0.65 | -0.44 / -0.69 | both halves | 3e-05 |  |
| [[SIRT2]] | -0.64 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.64 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[ZFAND2B]] | -0.64 | -0.46 / -0.73 | both halves | 3e-05 |  |
| [[PMM1]] | -0.64 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.63 | -0.40 / -0.70 | both halves | 5e-05 |  |
| [[TRAPPC2B]] | -0.63 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[TULP3]] | -0.63 | -0.53 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.3, -22.5); signed map (-14.5, -39.0). **Vector** length 103, 26.7% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +5.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +2.3 | +2.7 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.4 | -1.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:83,016,423-83,067,252 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0C5](https://www.uniprot.org/uniprotkb/Q9H0C5) (BTB/POZ domain-containing protein 1):

> Probable substrate-specific adapter of an E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Seems to regulate expression levels and/or subnuclear distribution of TOP1, via an unknown mechanism (By similarity). May play a role in mesenchymal differentiation where it promotes myogenic differentiation and suppresses adipogenesis (By similarity).

**Summary**, from NCBI Gene [53339](https://www.ncbi.nlm.nih.gov/gene/53339):

> The C-terminus of the protein encoded by this gene binds topoisomerase I. The N-terminus contains a proline-rich region and a BTB/POZ domain (broad-complex, Tramtrack and bric a brac/Pox virus and Zinc finger), both of which are typically involved in protein-protein interactions. Subcellularly, the protein localizes to cytoplasmic bodies. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1120](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1120) · Entrez [53339](https://www.ncbi.nlm.nih.gov/gene/53339) · UniProt [Q9H0C5](https://www.uniprot.org/uniprotkb/Q9H0C5) · Ensembl [ENSG00000064726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064726)

## Data

Gene col 759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 759); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 759]; `tensor/DDL_lfc|DDL_z.npy` [759]; `embed/gene_vectors.npy` [759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 759 or target_col == 759). Every well: [[BTBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
