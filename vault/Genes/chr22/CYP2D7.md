---
symbol: "CYP2D7"
type: "gene"
col: 13002
ensembl_id: "ENSG00000205702"
name: "cytochrome P450 family 2 subfamily D member 7 (gene/pseudogene)"
location: "22q13.2"
module: 47
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CYP2D7

*cytochrome P450 family 2 subfamily D member 7 (gene/pseudogene)* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.41× (z +6.7, q 7e-09, up in 0 of 0 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +4.4, q 0.002, up in 7 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.457× (z -5.9, q 2e-06, down in 17 of 36 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.509× (z -5.3, q 2e-05, down in 21 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.5 µM in 1 line (LS 180 0.0676×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNIP2]] (+0.64, fdr 1e-05), [[LINC02728]] (+0.64, fdr 1e-05), [[JMJD7]] (+0.62, fdr 1e-05); moves opposite to [[HPF1]] (-0.56, fdr 1e-05), [[SMAD9]] (-0.54, fdr 3e-05), [[KIAA1586]] (-0.53, fdr 2e-05).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +6.7 | 7e-09 | 0/0 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.28×** | +6.7 | 7e-09 | 19/43 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.4 | 0.002 | 7/26 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +3.6 | 0.043 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.56× | +3.2 | 0.14 | 1/19 (SK-MEL-2) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.15× | +3.2 | 0.14 | 1/4 (PANC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13002.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.5 µM in 1 line (LS 180 0.0676×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.457×** | -5.9 | 2e-06 | 17/36 (NCI-H2030, A549, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.508×** | -5.4 | 2e-05 | 16/43 (PANC-1, HOP62, …) | top dose only | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.509×** | -5.3 | 2e-05 | 21/41 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.512×** | -5.3 | 2e-05 | 7/18 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.575×** | -4.4 | 0.001 | 11/42 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.677× | -3.1 | 0.19 | 9/30 (PANC-1, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 4.24 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0676× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.758 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.669 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNIP2]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[LINC02728]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[JMJD7]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GHRLOS]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[NPIPB11]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ARHGAP4]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[DNAH1]] | +0.57 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[FSCN2]] | +0.57 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[MKRN5P]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.55 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPF1]] | -0.56 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[SMAD9]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[KIAA1586]] | -0.53 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[SNX2]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[HCFC2]] | -0.52 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[MRPS31]] | -0.52 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[ASB8]] | -0.52 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[TRMT1L]] | -0.52 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[ATP5PO]] ⚠ | -0.51 | -0.41 / -0.53 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RAB30]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SNAPIN]] | -0.51 | -0.40 / -0.61 | both halves | 4e-05 |  |
| [[NR2F2]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SECISBP2L]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.1, -15.6); signed map (-8.9, -37.0). **Vector** length 42.6, 4.67% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +1.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.0 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.9 | +2.7 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +0.8 | +1.5 |
|  | [[Ivermectin (drug)]] 0.5 µM |  | +0.8 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.1 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 2 subfamily D member 7 (gene/pseudogene) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,140,203-42,149,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CYP2D, CYP2D@, CYP2D7P1, CYP2D7P |
| Gene groups (HGNC) | Cytochrome P450 family 2 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A087X1C5](https://www.uniprot.org/uniprotkb/A0A087X1C5) (Cytochrome P450 2D7):

> May be responsible for the metabolism of many drugs and environmental chemicals that it oxidizes. It may be involved in the metabolism of codeine to morphine. However, another study could not confirm it.

**Summary**, from NCBI Gene [1564](https://www.ncbi.nlm.nih.gov/gene/1564):

> This gene is a member of the cytochrome P450 gene superfamily. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This gene is a segregating pseudogene, where some individuals may have an allele that encodes a functional enzyme, while other individuals have an allele encoding a protein that is predicted to be non-functional. In this case, the functional allele is thought to be rare. …

**Accessions** — [HGNC:2624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2624) · Entrez [1564](https://www.ncbi.nlm.nih.gov/gene/1564) · UniProt [A0A087X1C5](https://www.uniprot.org/uniprotkb/A0A087X1C5) · Ensembl [ENSG00000205702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205702)

## Data

Gene col 13002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13002); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13002]; `tensor/DDL_lfc|DDL_z.npy` [13002]; `embed/gene_vectors.npy` [13002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13002 or target_col == 13002). Every well: [[CYP2D7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP2D7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
