---
symbol: "WASHC1"
type: "gene"
col: 11185
ensembl_id: "ENSG00000181404"
name: "WASH complex subunit 1"
location: "9p24.3"
module: 29
arm: "-"
pooled_cpm: 2.88
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# WASHC1

*WASH complex subunit 1* — 9p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +11.2, q 3e-26, up in 30 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0510×); [[Gallic acid (hydrate) (drug)]] 0.05 µM in 1 line (HT-29 0.0555×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.79, fdr 7e-06), [[SNHG11]] (+0.78, fdr 7e-06), [[CDK3]] (+0.76, fdr 7e-06); moves opposite to [[PPT1]] (-0.74, fdr 7e-06), [[RBBP7]] (-0.71, fdr 7e-06), [[TMX1]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +11.2 | 3e-26 | 30/36 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.80×** | +8.3 | 3e-14 | 28/34 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +7.6 | 7e-12 | 1/3 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +6.9 | 9e-10 | 25/40 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +5.2 | 3e-05 | 15/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.003 | 12/32 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.40×** | +4.0 | 0.006 | 5/25 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.7 | 0.015 | 5/15 (LoVo, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +3.6 | 0.018 | 3/14 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.12×** | +3.4 | 0.037 | 3/30 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.043 | 4/28 (NCI-H460, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.01×** | +3.2 | 0.075 | 4/17 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.075 | 4/42 (A-172, HS-578T, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.95×** | +3.0 | 0.099 | 2/32 (HEC-1-A, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11185.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0510×); [[Gallic acid (hydrate) (drug)]] 0.05 µM in 1 line (HT-29 0.0555×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.663× | -3.1 | 0.60 | 8/46 (NCI-H661, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.689× | -3.1 | 0.60 | 11/43 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.08 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0510× (z -9.8) |
| [[HT-29 (line)]] | alt | 2.64 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.05 µM 0.0555× (z -8.5) |
| [[A-172 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.79 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.78 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[CDK3]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[EIF4EBP3]] | +0.75 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[MED18]] | +0.72 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[FBXL6]] | +0.72 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[STK16]] | +0.71 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ZNF579]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[GFER]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[CIRBP]] | +0.70 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.70 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[ATF4]] | +0.69 | +0.67 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | -0.74 | -0.72 / -0.74 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.71 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[TMX1]] | -0.68 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[BANF1]] | -0.68 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ADAM15]] | -0.67 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.67 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[PGAM1]] | -0.66 | -0.66 / -0.70 | both halves | 7e-06 |  |
| [[TMEM30A]] | -0.66 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[DCAF16]] | -0.66 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.65 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ICMT]] | -0.64 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[TGOLN2]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 | STRING 414 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-36.4, -15.1); signed map (1.4, -11.7). **Vector** length 47.1, 6.31% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +3.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | WASH complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.3 — chr9:14,475-73,865 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00038; previously FAM39E, WASH1 |
| Gene groups (HGNC) | Wiskott-Aldrich Syndrome protein family; WASH complex; SSU processome |
| Matched by | ensembl_id |

**Function**, from UniProt [A8K0Z3](https://www.uniprot.org/uniprotkb/A8K0Z3) (WASH complex subunit 1):

> Acts as a component of the WASH core complex that functions as a nucleation-promoting factor (NPF) at the surface of endosomes, where it recruits and activates the Arp2/3 complex to induce actin polymerization, playing a key role in the fission of tubules that serve as transport intermediates during endosome sorting. Involved in endocytic trafficking of EGF (By similarity). Involved in transferrin receptor recycling. Regulates the trafficking of endosomal alpha5beta1 integrin to the plasma …

**Summary**, from NCBI Gene [100287171](https://www.ncbi.nlm.nih.gov/gene/100287171):

> Enables alpha-tubulin binding activity and ubiquitin protein ligase binding activity. Involved in several processes, including Arp2/3 complex-mediated actin nucleation; endosomal transport; and positive regulation of pseudopodium assembly. Located in several cellular components, including endosome; exocyst; and lamellipodium. Part of WASH complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24361) · Entrez [100287171](https://www.ncbi.nlm.nih.gov/gene/100287171) · UniProt [A8K0Z3](https://www.uniprot.org/uniprotkb/A8K0Z3) · Ensembl [ENSG00000181404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181404)

## Data

Gene col 11185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11185); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11185]; `tensor/DDL_lfc|DDL_z.npy` [11185]; `embed/gene_vectors.npy` [11185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11185 or target_col == 11185). Every well: [[WASHC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASHC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
