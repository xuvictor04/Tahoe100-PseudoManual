---
symbol: "SNHG22"
type: "gene"
col: 15545
ensembl_id: "ENSG00000267322"
name: "small nucleolar RNA host gene 22"
location: "18q21.1"
module: 126
arm: "+"
pooled_cpm: 11.28
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# SNHG22

*small nucleolar RNA host gene 22* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +9.6, q 4e-19, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.610× (z -3.9, q 0.054, down in 20 of 47 measured lines) ⚠ cell-cycle shift, explains ~81% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.0861×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0921×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP1G2-AS1]] (+0.75, fdr 7e-06), [[GTF3C2-AS2]] (+0.70, fdr 1e-05), [[C8orf44-SGK3]] (+0.68, fdr 1e-05); moves opposite to [[ISCA2]] (-0.61, fdr 1e-04), [[CYC1]] (-0.58, fdr 2e-04), [[MRPL14]] (-0.58, fdr 2e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARMCX6]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +9.6 | 4e-19 | 39/45 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.37×** | +9.1 | 2e-17 | 39/48 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +6.5 | 1e-08 | 14/23 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +5.9 | 6e-07 | 24/28 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.9 | 1e-04 | 25/33 (SHP-77, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +4.1 | 0.004 | 22/48 (C-33 A, NCI-H23, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.012 | 20/45 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15545.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.0861×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0921×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.610×** | -3.9 | 0.054 | 20/47 (A-427, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.648× | -3.6 | 0.10 | 22/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 8.42 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0861× (z -9.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 8.57 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0921× (z -8.8) |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1G2-AS1]] | +0.75 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[GTF3C2-AS2]] | +0.70 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[C8orf44-SGK3]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ZNF514]] | +0.68 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CERS2]] | +0.66 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[TSSK3]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MSTO1]] | +0.64 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[CCNY-AS1]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.63 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | +0.62 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[BCL2L2]] | +0.62 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[ZC3H3]] | +0.61 | +0.39 / +0.68 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 4 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | -0.61 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[CYC1]] | -0.58 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[MRPL14]] | -0.58 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[NTHL1]] | -0.58 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[NDUFA7]] | -0.56 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[ATP5MC1]] | -0.55 | -0.30 / -0.60 | both halves | 2e-04 |  |
| [[RASSF7]] | -0.55 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[ATP5PO]] ⚠ | -0.55 | -0.27 / -0.46 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCR10]] ⚠ | -0.54 | -0.27 / -0.56 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL12]] | -0.54 | -0.13 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[MRPL17]] | -0.54 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[ATP5MC3]] ⚠ | -0.54 | -0.38 / -0.55 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TXNDC17]] | -0.53 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARMCX6]] | C | ARMCX6 activity lowers SNHG22's level | lines that do not express ARMCX6 (3) vs lines expressing it (46) | 2.05× higher at baseline in the lines without ARMCX6 | 0.083 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.6, 21.9); signed map (30.3, -17.2). **Vector** length 76.9, 14.4% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +0.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -2.4 | -3.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 22 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18q21.1 — chr18:49,813,965-49,851,059 (+) |
| Ensembl biotype | lncRNA |
| Also known as | SCARNA17HG |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50285) · Entrez [103091864](https://www.ncbi.nlm.nih.gov/gene/103091864) · Ensembl [ENSG00000267322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267322)

## Data

Gene col 15545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15545); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15545]; `tensor/DDL_lfc|DDL_z.npy` [15545]; `embed/gene_vectors.npy` [15545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15545 or target_col == 15545). Every well: [[SNHG22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
