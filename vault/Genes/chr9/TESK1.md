---
symbol: "TESK1"
type: "gene"
col: 2828
ensembl_id: "ENSG00000107140"
name: "testis associated actin remodelling kinase 1"
location: "9p13.3"
module: 2
arm: "+"
pooled_cpm: 4.91
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TESK1

*testis associated actin remodelling kinase 1* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.87× (z +6.8, q 6e-09, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.70× (z +5.7, q 5e-06, up in 16 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.531× (z -6.9, q 3e-09, down in 25 of 44 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.633× (z -5.2, q 6e-05, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SBF1]] (+0.72, fdr 7e-06), [[CRAT]] (+0.72, fdr 7e-06), [[PITPNM1]] (+0.68, fdr 7e-06); moves opposite to [[CRADD]] (-0.52, fdr 3e-05), [[CHD9]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.8 | 6e-09 | 4/7 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +5.7 | 5e-06 | 16/43 (SW480, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +5.3 | 2e-05 | 15/43 (LoVo, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.2 | 2e-05 | 8/25 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +4.8 | 1e-04 | 15/46 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +3.7 | 0.021 | 2/10 (SW1417, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.5 | 0.032 | 8/29 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.034 | 6/28 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.047 | 12/44 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.049 | 7/35 (PANC-1, SW480, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +3.3 | 0.054 | 9/40 (A498, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2828.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.531×** | -6.9 | 3e-09 | 25/44 (A-172, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -5.2 | 6e-05 | 20/45 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.752×** | -4.5 | 0.001 | 18/37 (HS-578T, NCI-H23, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -4.5 | 0.001 | 12/48 (NCI-H23, C-33 A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.699×** | -4.1 | 0.005 | 15/38 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.751×** | -3.3 | 0.096 | 8/44 (SK-MEL-2, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.752×** | -3.2 | 0.096 | 9/44 (hTERT-HPNE, NCI-H2030, …) | inconsistent across doses |  |
| [[Procainamide (hydrochloride) (drug)]] 5 µM |  | 0.747× | -3.2 | 0.10 | 11/43 (AsPC-1, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.762× | -3.1 | 0.13 | 17/45 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.759× | -3.0 | 0.15 | 5/43 (BT-474, SK-MEL-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.76 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0283× (z -15.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HT-29 (line)]] | alt | 3.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0568× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 7.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H23 (line)]] | alt | 9.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -9.9) ⚠ cell-cycle shift, explains ~72% of this change |
| [[Panc 03.27 (line)]] | alt | 5.91 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0942× (z -8.6) |
| [[SW1417 (line)]] | alt | 6.43 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.116× (z -8.7) |
| [[A-427 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBF1]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[CRAT]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[PITPNM1]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[LLGL1]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ATG9A]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[USP35]] | +0.65 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[MAN2B2]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[MAPK7]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[UFD1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[HECTD3]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[AKT1]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRADD]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[CHD9]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.9, -21.4); signed map (-47.8, -11.4). **Vector** length 58.8, 8.08% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.5 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.0 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.5 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.8 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -2.4 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | testis associated actin remodelling kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,605,262-35,610,041 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LIMK/TESK kinase family; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Regulation of cytoskeletal remodeling and cell spreading by IPP complex components; Cell-extracellular matrix interactions; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15569](https://www.uniprot.org/uniprotkb/Q15569) (Dual specificity testis-specific protein kinase 1):

> Dual specificity protein kinase activity catalyzing autophosphorylation and phosphorylation of exogenous substrates on both serine/threonine and tyrosine residues (By similarity). Regulates the cellular cytoskeleton by enhancing actin stress fiber formation via phosphorylation of cofilin and by preventing microtubule breakdown via inhibition of TAOK1/MARKK kinase activity (By similarity). Inhibits podocyte motility via regulation of actin cytoskeletal dynamics and phosphorylation of CFL1 (By …

**Summary**, from NCBI Gene [7016](https://www.ncbi.nlm.nih.gov/gene/7016):

> This gene product is a serine/threonine protein kinase that contains an N-terminal protein kinase domain and a C-terminal proline-rich domain. Its protein kinase domain is most closely related to those of the LIM motif-containing protein kinases (LIMKs). The encoded protein can phosphorylate myelin basic protein and histone in vitro. The testicular germ cell-specific expression and developmental pattern of expression of the mouse gene suggests that this gene plays an important role at and after …

**Accessions** — [HGNC:11731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11731) · Entrez [7016](https://www.ncbi.nlm.nih.gov/gene/7016) · UniProt [Q15569](https://www.uniprot.org/uniprotkb/Q15569) · Ensembl [ENSG00000107140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107140)

## Data

Gene col 2828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2828); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2828]; `tensor/DDL_lfc|DDL_z.npy` [2828]; `embed/gene_vectors.npy` [2828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2828 or target_col == 2828). Every well: [[TESK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TESK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
