---
symbol: "TIMM29"
type: "gene"
col: 6622
ensembl_id: "ENSG00000142444"
name: "translocase of inner mitochondrial membrane 29"
location: "19p13.2"
module: 119
arm: "+"
pooled_cpm: 7.6
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# TIMM29

*translocase of inner mitochondrial membrane 29* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.64× (z +10.5, q 3e-23, up in 34 of 38 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.98× (z +7.7, q 3e-12, up in 39 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 0.134×, A-427 0.143×; ⚠ cell-cycle shift, would explain all of this change); [[Ligustrazine (drug)]] 5 µM in 1 line (RPMI-7951 0.0630×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0879×); [[Pexidartinib (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0502×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCBP2AS2]] (+0.76, fdr 1e-05), [[TTI2]] (+0.74, fdr 7e-06), [[ALKBH4]] (+0.73, fdr 7e-06); moves opposite to [[IPO5]] (-0.66, fdr 1e-05), [[LRPPRC]] (-0.63, fdr 1e-05), [[MTHFD1]] (-0.63, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +10.5 | 3e-23 | 34/38 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +7.7 | 3e-12 | 39/47 (NCI-H23, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.5 | 1e-11 | 22/44 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +7.1 | 2e-10 | 32/47 (LoVo, HS-578T, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +5.8 | 6e-07 | 24/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.57×** | +5.1 | 4e-05 | 23/47 (LoVo, HEC-1-A, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.4 | 6e-04 | 16/48 (NCI-H2347, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.48×** | +4.4 | 6e-04 | 15/38 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.003 | 19/43 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.0 | 0.003 | 16/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.25×** | +3.6 | 0.019 | 12/42 (RKO, C32, …) | all doses, flat | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.023 | 11/40 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +3.3 | 0.040 | 8/48 (Hs 766T, HOP62, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.083 | 8/44 (A498, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 0.134×, A-427 0.143×; ⚠ cell-cycle shift, would explain all of this change); [[Ligustrazine (drug)]] 5 µM in 1 line (RPMI-7951 0.0630×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0879×); [[Pexidartinib (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0502×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 8.48 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 6.86 | 0 | 1 | — | [[Pexidartinib (hydrochloride) (drug)]] 5 µM 0.0502× (z -9.8) |
| [[J82 (line)]] | alt | 7.44 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[NCI-H1573 (line)]] | alt | 4.70 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0879× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 8.64 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0630× (z -10.3) |
| [[SNU-423 (line)]] | alt | 7.95 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP2AS2]] | +0.76 | +0.57 / +0.81 | both halves | 1e-05 |  |
| [[TTI2]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ZNF707]] | +0.71 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[TEFM]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.70 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[ADPRS]] | +0.70 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.70 | +0.51 / +0.77 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C1orf35]] | +0.69 | +0.45 / +0.78 | both halves | 3e-05 |  |
| [[TRIM4]] | +0.68 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[TTF1]] | +0.67 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[C16orf91]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ZNF500]] | +0.66 | +0.47 / +0.71 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.66 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.63 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.63 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[STK26]] | -0.62 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[IPO7]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.61 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[NONO]] | -0.60 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[STT3B]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.58 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[PAICS]] | -0.58 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[TFRC]] | -0.57 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.57 | -0.45 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.0, -5.9); signed map (-8.9, -11.4). **Vector** length 51.4, 6.96% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | -2.8 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.8 |
|  | [[Volasertib (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Folic acid (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,928,811-10,933,535 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIM29; previously C19orf52 |
| Gene groups (HGNC) | TIM22 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSF4](https://www.uniprot.org/uniprotkb/Q9BSF4) (Mitochondrial import inner membrane translocase subunit Tim29):

> Component of the TIM22 complex, a complex that mediates the import and insertion of multi-pass transmembrane proteins into the mitochondrial inner membrane. The TIM22 complex forms a twin-pore translocase that uses the membrane potential as the external driving force. Required for the stability of the TIM22 complex and functions in the assembly of the TIMM22 protein into the TIM22 complex. May facilitate cooperation between TIM22 and TOM complexes by interacting with TOMM40.

**Summary**, from NCBI Gene [90580](https://www.ncbi.nlm.nih.gov/gene/90580):

> Enables protein transporter activity. Involved in protein insertion into mitochondrial inner membrane. Located in mitochondrial inner membrane and mitochondrial intermembrane space. Part of TIM22 mitochondrial import inner membrane insertion complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25152) · Entrez [90580](https://www.ncbi.nlm.nih.gov/gene/90580) · UniProt [Q9BSF4](https://www.uniprot.org/uniprotkb/Q9BSF4) · Ensembl [ENSG00000142444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142444)

## Data

Gene col 6622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6622); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6622]; `tensor/DDL_lfc|DDL_z.npy` [6622]; `embed/gene_vectors.npy` [6622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6622 or target_col == 6622). Every well: [[TIMM29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
