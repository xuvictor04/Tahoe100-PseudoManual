---
symbol: "NEURL4"
type: "gene"
col: 13242
ensembl_id: "ENSG00000215041"
name: "neuralized E3 ubiquitin protein ligase 4"
location: "17p13.1"
module: 2
arm: "+"
pooled_cpm: 5.99
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NEURL4

*neuralized E3 ubiquitin protein ligase 4* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +12.8, q 1e-34, up in 28 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib (drug)]] 0.05 µM: 0.714× (z -3.8, q 0.077, down in 11 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.0952×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (A-172 0.115×; ⚠ transcription drop); [[Torkinib (drug)]] 5 µM in 1 line (SW480 0.0556×; ⚠ toxic); [[Eplerenone (drug)]] 5 µM in 1 line (BT-474 0.0489×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR24]] (+0.62, fdr 1e-05), [[SART1]] (+0.60, fdr 1e-05), [[CTBP1]] (+0.59, fdr 1e-05); moves opposite to [[TXN]] (-0.48, fdr 5e-05), [[SDAD1P1]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +12.8 | 1e-34 | 28/40 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.8 | 2e-06 | 14/39 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +4.5 | 0.001 | 11/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.014 | 12/45 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +3.8 | 0.017 | 7/44 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.022 | 7/41 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.6 | 0.022 | 10/34 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +3.6 | 0.022 | 10/41 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.025 | 10/47 (CFPAC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.030 | 6/43 (NCI-H1792, SW 900, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.050 | 7/47 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.1 | 0.096 | 6/31 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13242.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.0952×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (A-172 0.115×; ⚠ transcription drop); [[Torkinib (drug)]] 5 µM in 1 line (SW480 0.0556×; ⚠ toxic); [[Eplerenone (drug)]] 5 µM in 1 line (BT-474 0.0489×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib (drug)]] 0.05 µM |  | **0.714×** | -3.8 | 0.077 | 11/44 (NCI-H460, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Voriconazole (drug)]] 0.5 µM |  | 0.745× | -3.5 | 0.12 | 9/47 (RKO, A-427, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.755× | -3.4 | 0.14 | 9/47 (A-172, SHP-77, …) | inconsistent across doses |  |
| [[Relugolix (drug)]] 0.5 µM |  | 0.742× | -3.2 | 0.18 | 4/47 (SW 1271, AN3 CA, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.772× | -3.1 | 0.21 | 4/47 (AN3 CA, A498, …) | inconsistent across doses |  |
| [[Voriconazole (drug)]] 5 µM |  | 0.776× | -3.0 | 0.22 | 7/47 (A-427, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.60 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0952× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.81 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.115× (z -10.1) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 4.15 | 0 | 1 | — | [[Eplerenone (drug)]] 5 µM 0.0489× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 9.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 5.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.0) | — |
| [[A-427 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR24]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SART1]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[CTBP1]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[AAAS]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[RPS6KB2]] | +0.58 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ZNF598]] | +0.58 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SF3A2]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PARP6]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[DPH7]] | +0.57 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DXO]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZNF865]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.48 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[SDAD1P1]] | -0.47 | -0.39 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.363). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-34.7, -4.1); signed map (-12.4, -24.8). **Vector** length 55.3, 7.36% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +12.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +0.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.2 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.8 | -3.4 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | neuralized E3 ubiquitin protein ligase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,315,628-7,329,393 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1787 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JN8](https://www.uniprot.org/uniprotkb/Q96JN8) (Neuralized-like protein 4):

> Promotes CCP110 ubiquitination and proteasome-dependent degradation. By counteracting accumulation of CP110, maintains normal centriolar homeostasis and preventing formation of ectopic microtubular organizing centers.

**Summary**, from NCBI Gene [84461](https://www.ncbi.nlm.nih.gov/gene/84461):

> The protein encoded by this gene is predicted and it includes two isoforms resulting from two alternatively spliced transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:34410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34410) · Entrez [84461](https://www.ncbi.nlm.nih.gov/gene/84461) · UniProt [Q96JN8](https://www.uniprot.org/uniprotkb/Q96JN8) · Ensembl [ENSG00000215041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215041)

## Data

Gene col 13242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13242); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13242]; `tensor/DDL_lfc|DDL_z.npy` [13242]; `embed/gene_vectors.npy` [13242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13242 or target_col == 13242). Every well: [[NEURL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEURL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
