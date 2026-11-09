---
symbol: "GMFG"
type: "gene"
col: 5117
ensembl_id: "ENSG00000130755"
name: "glia maturation factor gamma"
location: "19q13.2"
module: 21
arm: "+"
pooled_cpm: 2.5
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# GMFG

*glia maturation factor gamma* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.04× (z +12.6, q 2e-33, up in 22 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RN7SL2]] (+0.70, fdr 2e-05), [[LINC00674]] (+0.70, fdr 8e-06), [[DCTN6-DT]] (+0.70, fdr 1e-05); moves opposite to [[EIF4G1]] (-0.56, fdr 5e-05), [[EIF2S1]] (-0.55, fdr 3e-05), [[XRCC5]] (-0.54, fdr 7e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.04×** | +12.6 | 2e-33 | 22/25 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.25×** | +9.1 | 2e-17 | 8/11 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.07×** | +8.6 | 2e-15 | 5/5 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.68×** | +6.6 | 5e-09 | 4/6 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.91×** | +5.7 | 2e-06 | 9/14 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.81×** | +4.6 | 3e-04 | 11/29 (PANC-1, LoVo, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +4.6 | 3e-04 | 21/43 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +4.5 | 5e-04 | 15/25 (PANC-1, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +4.4 | 6e-04 | 17/39 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +4.1 | 0.002 | 12/38 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.05×** | +4.0 | 0.004 | 11/34 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.02×** | +3.9 | 0.005 | 5/23 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +3.7 | 0.010 | 10/40 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.94×** | +3.6 | 0.011 | 11/32 (HOP62, LoVo, …) | inconsistent across doses | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.4 | 0.030 | 11/20 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.48×** | +3.3 | 0.033 | 2/15 (PANC-1, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.30×** | +3.0 | 0.068 | 5/19 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.072 | 3/40 (PANC-1, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **2.26×** | +3.0 | 0.076 | 3/20 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.678× | -3.0 | 0.81 | 11/44 (KATO III, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.31 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +19.0) | — |
| [[A549 (line)]] | wt | 2.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +8.8) | — |
| [[A-172 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.876 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.634 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.729 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.984 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.811 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.880 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RN7SL2]] | +0.70 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[LINC00674]] | +0.70 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[DCTN6-DT]] | +0.70 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.67 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[LRRC37A16P]] | +0.67 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[EFCAB14-AS1]] | +0.65 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[KIZ-AS1]] ⚠ | +0.65 | +0.48 / +0.66 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TBC1D22A-DT]] | +0.64 | +0.41 / +0.71 | both halves | 4e-05 |  |
| [[SNHG9]] | +0.63 | +0.37 / +0.73 | both halves | 8e-05 |  |
| [[RN7SL1]] | +0.63 | +0.43 / +0.73 | both halves | 3e-05 |  |
| [[ADGRL3-AS1]] | +0.62 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[MHENCR]] | +0.62 | +0.35 / +0.70 | both halves | 1e-04 |  |
| [[CSKMT]] | +0.62 | +0.42 / +0.72 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.56 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[EIF2S1]] | -0.55 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.54 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[PSME3]] | -0.54 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[PTPN11]] | -0.54 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[ANAPC7]] | -0.54 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[ZNF770]] | -0.53 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[ABCE1]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[PRKDC]] | -0.52 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.7, 29.9); signed map (-28.9, 6.6). **Vector** length 54.9, 10.4% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.6 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | glia maturation factor gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,328,353-39,342,372 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glia maturation factor family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [O60234](https://www.uniprot.org/uniprotkb/O60234) carries no function annotation.

**Summary**, from NCBI Gene [9535](https://www.ncbi.nlm.nih.gov/gene/9535):

> Predicted to enable Arp2/3 complex binding activity. Predicted to be involved in actin filament debranching and negative regulation of Arp2/3 complex-mediated actin nucleation. Predicted to be located in extracellular region; ficolin-1-rich granule lumen; and secretory granule lumen. Predicted to be active in cortical actin cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4374) · Entrez [9535](https://www.ncbi.nlm.nih.gov/gene/9535) · UniProt [O60234](https://www.uniprot.org/uniprotkb/O60234) · Ensembl [ENSG00000130755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130755)

## Data

Gene col 5117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5117); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5117]; `tensor/DDL_lfc|DDL_z.npy` [5117]; `embed/gene_vectors.npy` [5117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5117 or target_col == 5117). Every well: [[GMFG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMFG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
