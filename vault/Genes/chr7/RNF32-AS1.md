---
symbol: "RNF32-AS1"
type: "gene"
col: 13429
ensembl_id: "ENSG00000224903"
name: "RNF32 antisense RNA 1"
location: "7q36.3"
module: 47
arm: "+"
pooled_cpm: 3.7
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# RNF32-AS1

*RNF32 antisense RNA 1* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.21× (z +5.1, q 1e-04, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.308× (z -4.0, q 0.035, down in 21 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.0784×, HEC-1-A 0.0809×; ⚠ toxic); [[Decitabine (drug)]] 0.5 µM in 1 line (NCI-H23 0.0602×); [[Pemetrexed (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0739×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA6A-AS1]] (+0.74, fdr 7e-06), [[TMEM236]] (+0.71, fdr 7e-06), [[CFAP161]] (+0.70, fdr 7e-06); moves opposite to [[SPATA7]] (-0.73, fdr 7e-06), [[MALSU1]] (-0.67, fdr 7e-06), [[PEX3]] (-0.67, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[APPAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13429.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +5.1 | 1e-04 | 21/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +4.7 | 7e-04 | 3/7 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.046 | 6/45 (A498, HS-578T, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.046 | 18/42 (C32, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.046 | 11/38 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +3.4 | 0.054 | 6/19 (AsPC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +3.4 | 0.054 | 3/48 (LoVo, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +3.3 | 0.056 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.056 | 11/36 (hTERT-HPNE, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.66×** | +3.3 | 0.056 | 10/47 (A498, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13429.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.0784×, HEC-1-A 0.0809×; ⚠ toxic); [[Decitabine (drug)]] 0.5 µM in 1 line (NCI-H23 0.0602×); [[Pemetrexed (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0739×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -4.0 | 0.035 | 21/42 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.660×** | -3.8 | 0.039 | 20/44 (Hs 766T, hTERT-HPNE, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.65 | 0 | 2 (1 ⚠) | — | [[Pemetrexed (drug)]] 0.05 µM 0.0739× (z -9.2) |
| [[A-427 (line)]] | wt | 5.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0835× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[LoVo (line)]] | wt | 8.62 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0784× (z -9.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 9.18 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0602× (z -11.2) |
| [[A-172 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA6A-AS1]] | +0.74 | +0.76 / +0.71 | both halves | 7e-06 | same gene group |
| [[TMEM236]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[CFAP161]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PSMD6-AS1]] | +0.69 | +0.73 / +0.70 | both halves | 7e-06 | same gene group |
| [[SLC2A9]] | +0.69 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[LINC00641]] | +0.68 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[ZDHHC11]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SH3BP5-AS1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | same gene group |
| [[SSUH2]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[DNAH1]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[MPP4]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[LINC00907]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA7]] | -0.73 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[MALSU1]] | -0.67 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[PEX3]] | -0.67 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[CCZ1]] | -0.66 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.66 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[CCZ1B]] | -0.64 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[ZNF14]] | -0.64 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[SNAPC3]] | -0.63 | -0.73 / -0.49 | both halves | 1e-05 |  |
| [[MTF2]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[HEATR6]] | -0.60 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.60 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SLC35A1]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APPAT]] | B | APPAT activity raises RNF32-AS1's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without APPAT | 0.051 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NEK10]] | B | NEK10 activity raises RNF32-AS1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without NEK10 | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.8, -10.5); signed map (19.1, 6.3). **Vector** length 62.0, 9.29% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.6 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.5 | -1.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RNF32 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q36.3 — chr7:156,654,185-156,659,582 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40798) · Entrez [101927858](https://www.ncbi.nlm.nih.gov/gene/101927858) · Ensembl [ENSG00000224903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224903)

## Data

Gene col 13429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13429); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13429]; `tensor/DDL_lfc|DDL_z.npy` [13429]; `embed/gene_vectors.npy` [13429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13429 or target_col == 13429). Every well: [[RNF32-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF32-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
