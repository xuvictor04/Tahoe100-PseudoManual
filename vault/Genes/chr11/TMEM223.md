---
symbol: "TMEM223"
type: "gene"
col: 9671
ensembl_id: "ENSG00000168569"
name: "transmembrane protein 223"
location: "11q12.3"
module: 89
arm: "+"
pooled_cpm: 8.76
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# TMEM223

*transmembrane protein 223* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.47× (z +8.5, q 1e-14, up in 37 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 11.3×, LOX-IMVI 5.95×, A498 3.91×, LoVo 3.69×, …; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2347 7.72×, LOX-IMVI 5.05×, BT-474 7.53×); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 4.44×, HOP62 5.22×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.662× (z -3.9, q 0.058, down in 19 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.189×).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRT3-AS1]] (+0.62, fdr 1e-05), [[C2orf49-DT]] (+0.57, fdr 1e-05), [[LINC01618]] (+0.57, fdr 2e-05); moves opposite to [[DCTN1]] (-0.51, fdr 1e-04), [[CTC1]] (-0.47, fdr 9e-05), [[CDC16]] (-0.47, fdr 4e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9671.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 11.3×, LOX-IMVI 5.95×, A498 3.91×, LoVo 3.69×, …; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2347 7.72×, LOX-IMVI 5.05×, BT-474 7.53×); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 4.44×, HOP62 5.22×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +8.5 | 1e-14 | 37/46 (SW480, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +7.6 | 6e-12 | 31/45 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.74×** | +4.8 | 3e-04 | 17/27 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.58×** | +4.3 | 0.003 | 20/40 (SW 900, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.5 | 0.057 | 13/43 (HS-578T, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.44×** | +3.4 | 0.062 | 13/34 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.29×** | +3.4 | 0.064 | 12/48 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.3 | 0.072 | 14/38 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Carbamazepine (drug)]] 5 µM |  | 1.40× | +3.1 | 0.11 | 9/46 (hTERT-HPNE, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9671.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.189×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -3.9 | 0.058 | 19/44 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.720× | -3.1 | 0.56 | 6/47 (A-172, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 8.16 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +10.2) | — |
| [[A498 (line)]] | wt | 6.43 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 4.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.53× (z +8.9) | — |
| [[C32 (line)]] | wt | 6.43 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 8.37 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.22× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 7.58 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 6.90 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 4.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.72× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 9.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -9.4) |
| [[SW480 (line)]] | alt | 9.35 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.44× (z +9.1) | — |
| [[A-172 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 17 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRT3-AS1]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[C2orf49-DT]] | +0.57 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[LINC01618]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[POLG2]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CDK5R1]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PRR7-AS1]] | +0.56 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ENDOG]] | +0.55 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[NAA60]] | +0.55 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[DENND6A-AS1]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[PYY]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[TMEM79]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[KIAA0753]] | +0.54 | +0.38 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN1]] | -0.51 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[CTC1]] | -0.47 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[CDC16]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[RNF141]] | -0.46 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[TMTC3]] | -0.46 | -0.21 / -0.52 | both halves | 7e-04 |  |
| [[FYCO1]] | -0.46 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[OCRL]] | -0.46 | -0.13 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[DYNC1LI2]] | -0.45 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[EFR3A]] | -0.45 | -0.17 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[LPGAT1]] | -0.45 | -0.21 / -0.60 | both halves | 7e-04 |  |
| [[SGPL1]] | -0.45 | -0.14 / -0.61 | ⚠ one half (not replicated) | 0.002 |  |
| [[SF1]] | -0.45 | -0.09 / -0.67 | ⚠ one half (not replicated) | 0.003 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.327). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, -7.5); signed map (11.3, 18.3). **Vector** length 58.6, 9.85% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Omeprazole (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 223 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,771,629-62,792,006 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3196, Mrx15 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [A0PJW6](https://www.uniprot.org/uniprotkb/A0PJW6) (Transmembrane protein 223):

> Mitochondrial ribosome-associated protein involved in the first steps of cytochrome c oxidase complex (complex IV) biogenesis. Stimulates the translation of MT-CO1 mRNA and is a constituent of early MT-CO1 assembly intermediates.

**Summary**, from NCBI Gene [79064](https://www.ncbi.nlm.nih.gov/gene/79064):

> Enables mitochondrial ribosome binding activity. Involved in mitochondrial respiratory chain complex IV assembly. Located in mitochondrion. Is active in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28464) · Entrez [79064](https://www.ncbi.nlm.nih.gov/gene/79064) · UniProt [A0PJW6](https://www.uniprot.org/uniprotkb/A0PJW6) · Ensembl [ENSG00000168569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168569)

## Data

Gene col 9671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9671); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9671]; `tensor/DDL_lfc|DDL_z.npy` [9671]; `embed/gene_vectors.npy` [9671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9671 or target_col == 9671). Every well: [[TMEM223 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM223.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
