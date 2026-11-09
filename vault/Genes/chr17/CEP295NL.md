---
symbol: "CEP295NL"
type: "gene"
col: 10925
ensembl_id: "ENSG00000178404"
name: "CEP295 N-terminal like"
location: "17q25.3"
module: 2
arm: "+"
pooled_cpm: 2.24
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CEP295NL

*CEP295 N-terminal like* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +4.9, q 5e-04, up in 17 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.410× (z -6.0, q 9e-07, down in 23 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 5 µM in 1 line (HT-29 0.0723×); [[Pioglitazone (drug)]] 0.5 µM in 1 line (SW1417 0.0704×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMP2]] (+0.71, fdr 7e-06, ⚠ read-through risk), [[FCHSD1]] (+0.59, fdr 3e-05), [[BMP8B]] (+0.57, fdr 1e-05), [[BAIAP3]] (+0.55, fdr 3e-05); moves opposite to [[TBCK]] (-0.61, fdr 1e-05), [[MAP2K5]] (-0.59, fdr 1e-05), [[GMDS-DT]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SCN5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +4.9 | 5e-04 | 17/41 (HOP62, KATO III, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +3.9 | 0.024 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +3.6 | 0.050 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +3.2 | 0.20 | 3/45 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.55× | +3.0 | 0.27 | 11/44 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10925.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 5 µM in 1 line (HT-29 0.0723×); [[Pioglitazone (drug)]] 0.5 µM in 1 line (SW1417 0.0704×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.410×** | -6.0 | 9e-07 | 23/36 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.440×** | -5.8 | 2e-06 | 21/40 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.573×** | -3.9 | 0.020 | 18/44 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.615×** | -3.4 | 0.084 | 11/20 (A549, SW480, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | 0.622× | -3.1 | 0.24 | 10/38 (SHP-77, SW 900, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 2.35 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 5 µM 0.0723× (z -9.3) |
| [[SW1417 (line)]] | alt | 5.15 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0704× (z -8.7) |
| [[A-172 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.814 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.924 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.632 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.809 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.825 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.841 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.835 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMP2]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of TIMP2 on the same strand (can correlate by spillover, not regulation) |
| [[FCHSD1]] | +0.59 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[BMP8B]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[RTN4R]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[ABHD17A]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[USP35]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[UNC5A]] | +0.53 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[JMJD7]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[RIMS3]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TNK2]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[MICE]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ESYT3]] | +0.51 | +0.26 / +0.49 | both halves | 4e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[MAP2K5]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[GMDS-DT]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[VPS13B]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ASH1L]] | -0.54 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[PRH1]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[FBXL17]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ATG10]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[AFG1L]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RPP38]] | -0.51 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[SCAF11]] | -0.51 | -0.31 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCN5A]] | B | SCN5A activity raises CEP295NL's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 1.46× lower at baseline in the lines without SCN5A | 0.034 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9 |
| [[TIMP2]] | C | TIMP2 activity raises CEP295NL's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without TIMP2 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-24.3, 29.9); signed map (-24.7, 32.5). **Vector** length 46.7, 5.58% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.5 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.9 | +2.0 |
|  | [[Posaconazole (drug)]] 5 µM |  | +0.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +0.8 | +0.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.6 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Thymol (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | CEP295 N-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,890,579-78,903,217 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DDC8; previously KIAA1731NL |
| Matched by | ensembl_id |

UniProt [Q96MC4](https://www.uniprot.org/uniprotkb/Q96MC4) carries no function annotation.

**Summary**, from NCBI Gene [100653515](https://www.ncbi.nlm.nih.gov/gene/100653515):

> Predicted to be involved in regulation of centriole replication. Predicted to be located in motile cilium. Predicted to be active in centriole; centrosome; and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:44659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44659) · Entrez [100653515](https://www.ncbi.nlm.nih.gov/gene/100653515) · UniProt [Q96MC4](https://www.uniprot.org/uniprotkb/Q96MC4) · Ensembl [ENSG00000178404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178404)

## Data

Gene col 10925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10925); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10925]; `tensor/DDL_lfc|DDL_z.npy` [10925]; `embed/gene_vectors.npy` [10925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10925 or target_col == 10925). Every well: [[CEP295NL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP295NL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
