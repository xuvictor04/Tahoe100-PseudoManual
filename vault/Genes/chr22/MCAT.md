---
symbol: "MCAT"
type: "gene"
col: 1915
ensembl_id: "ENSG00000100294"
name: "malonyl-CoA-acyl carrier protein transacylase"
location: "22q13.2"
module: 33
arm: "+"
pooled_cpm: 3.76
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MCAT

*malonyl-CoA-acyl carrier protein transacylase* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +8.7, q 3e-15, up in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.24× (z +8.3, q 3e-14, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.796× (z -3.8, q 0.087, down in 15 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0587×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHODH]] (+0.73, fdr 7e-06), [[TMEM177]] (+0.69, fdr 7e-06), [[MRPL4]] (+0.68, fdr 1e-05); moves opposite to [[GNAS]] (-0.62, fdr 1e-05), [[ERO1B]] (-0.57, fdr 2e-05), [[LSMEM1]] (-0.56, fdr 8e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.12×** | +8.7 | 3e-15 | 30/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +8.3 | 3e-14 | 28/45 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.94×** | +7.7 | 4e-12 | 27/46 (SW480, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.4 | 2e-11 | 10/19 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +5.5 | 4e-06 | 7/45 (A498, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 8e-04 | 10/36 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.49×** | +4.4 | 8e-04 | 0/6 | all doses, flat | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +4.3 | 0.001 | 4/21 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.46×** | +4.0 | 0.003 | 1/8 (SW480) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.0 | 0.003 | 6/22 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +4.0 | 0.003 | 4/39 (LoVo, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.009 | 8/36 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.5 | 0.018 | 10/31 (C32, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +3.4 | 0.030 | 7/45 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.22×** | +3.3 | 0.042 | 8/38 (NCI-H1573, A498, …) | all doses, stronger at high dose | composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **1.67×** | +3.1 | 0.061 | 1/23 (LoVo) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1915.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0587×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.796×** | -3.8 | 0.087 | 15/46 (AsPC-1, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.05 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0587× (z -8.7) |
| [[A-172 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHODH]] | +0.73 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TMEM177]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MRPL4]] | +0.68 | +0.57 / +0.62 | both halves | 1e-05 | STRING 663 |
| [[NLE1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[COG2]] | +0.66 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[LCLAT1]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[NUFIP1]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RRP1]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MRPS23]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 | STRING 882 |
| [[METTL2A]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[DIS3L2]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[DCTPP1]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ERO1B]] | -0.57 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[LSMEM1]] | -0.56 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[LRP2BP]] | -0.56 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[MORF4L2]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[MAP1LC3B]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[LINC00910]] | -0.54 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.2, -41.6); signed map (-9.1, -51.8). **Vector** length 45.7, 5.18% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.0 | +8.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.9 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +7.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +1.9 | +7.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | malonyl-CoA-acyl carrier protein transacylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:43,132,209-43,143,398 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MT, MCT, fabD, FASN2C, NET62, MCT1 |
| Gene groups (HGNC) | Acyltransferases |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVS2](https://www.uniprot.org/uniprotkb/Q8IVS2) (Malonyl-CoA-acyl carrier protein transacylase, mitochondrial):

> Catalyzes the transfer of a malonyl moiety from malonyl-CoA to the free thiol group of the phosphopantetheine arm of the mitochondrial ACP protein (NDUFAB1). This suggests the existence of the biosynthesis of fatty acids in mitochondria. Also acts as a mitochondrial small ribosomal subunit (mt-SSU) assembly factor.

**Summary**, from NCBI Gene [27349](https://www.ncbi.nlm.nih.gov/gene/27349):

> The protein encoded by this gene is found exclusively in the mitochondrion, where it catalyzes the transfer of a malonyl group from malonyl-CoA to the mitochondrial acyl carrier protein. The encoded protein may be part of a fatty acid synthase complex that is more like the type II prokaryotic and plastid complexes rather than the type I human cytosolic complex. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:29622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29622) · Entrez [27349](https://www.ncbi.nlm.nih.gov/gene/27349) · UniProt [Q8IVS2](https://www.uniprot.org/uniprotkb/Q8IVS2) · Ensembl [ENSG00000100294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100294)

## Data

Gene col 1915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1915); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1915]; `tensor/DDL_lfc|DDL_z.npy` [1915]; `embed/gene_vectors.npy` [1915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1915 or target_col == 1915). Every well: [[MCAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
