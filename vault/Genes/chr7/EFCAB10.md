---
symbol: "EFCAB10"
type: "gene"
col: 11619
ensembl_id: "ENSG00000185055"
name: "EF-hand calcium binding domain 10"
location: "7q22.3"
module: 39
arm: "+"
pooled_cpm: 9.74
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# EFCAB10

*EF-hand calcium binding domain 10* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.00× (z +14.3, q 1e-43, up in 32 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +4.9, q 1e-04, up in 24 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.106×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.74, fdr 7e-06), [[BTG3-AS1]] (+0.68, fdr 2e-05), [[CFAP70]] (+0.68, fdr 1e-05); moves opposite to [[ACTR5]] (-0.58, fdr 6e-05), [[ZNF692]] (-0.57, fdr 4e-05), [[TRIM35]] (-0.56, fdr 8e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ST8SIA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.00×** | +14.3 | 1e-43 | 32/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +11.7 | 6e-29 | 19/21 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +9.0 | 4e-17 | 25/28 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.65×** | +7.4 | 2e-11 | 25/46 (LoVo, HCT15, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.9 | 1e-04 | 24/44 (SNU-423, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.8 | 2e-04 | 22/44 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 6e-04 | 21/43 (C32, HCT15, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.031 | 10/46 (CFPAC-1, HS-578T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.031 | 14/48 (SW480, SW 900, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.063 | 7/46 (HCT15, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11619.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.106×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.701× | -3.6 | 0.16 | 15/47 (LoVo, RKO, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.553× | -3.2 | 0.41 | 14/42 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.741× | -3.1 | 0.41 | 11/47 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.31× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.50× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.106× (z -8.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.67× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 8.09 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +9.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.77 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[BTG3-AS1]] | +0.68 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[CFAP70]] | +0.68 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[MFSD2B]] | +0.67 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[FAM151B]] | +0.67 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[TXK]] | +0.67 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[ALDH8A1]] | +0.66 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[LINC02955]] | +0.66 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[LRGUK]] | +0.66 | +0.79 / +0.49 | both halves | 1e-05 |  |
| [[LINC01031]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[GARIN1B]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[SLC6A13]] | +0.65 | +0.74 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR5]] | -0.58 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[ZNF692]] | -0.57 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[TRIM35]] | -0.56 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[FAM24B]] | -0.55 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[ZNF232]] | -0.55 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST8SIA5]] | B | ST8SIA5 activity raises EFCAB10's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without ST8SIA5 | 0.040 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises EFCAB10's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.27× lower at baseline in the lines without FSIP2-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[MPP4]] | C | MPP4 activity raises EFCAB10's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[IMPG2]] | C | IMPG2 activity raises EFCAB10's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.23× lower at baseline in the lines without IMPG2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.4, -11.6); signed map (20.6, 4.9). **Vector** length 61.9, 10.4% of its response variance represented; |z| ≥ 3 in 671 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.9 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.4 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:105,565,120-105,600,875 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [A6NFE3](https://www.uniprot.org/uniprotkb/A6NFE3) carries no function annotation.

**Summary**, from NCBI Gene [100130771](https://www.ncbi.nlm.nih.gov/gene/100130771):

> Predicted to enable calcium ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34531) · Entrez [100130771](https://www.ncbi.nlm.nih.gov/gene/100130771) · UniProt [A6NFE3](https://www.uniprot.org/uniprotkb/A6NFE3) · Ensembl [ENSG00000185055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185055)

## Data

Gene col 11619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11619); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11619]; `tensor/DDL_lfc|DDL_z.npy` [11619]; `embed/gene_vectors.npy` [11619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11619 or target_col == 11619). Every well: [[EFCAB10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
