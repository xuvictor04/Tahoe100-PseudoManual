---
symbol: "YJEFN3"
type: "gene"
col: 14660
ensembl_id: "ENSG00000250067"
name: "YjeF N-terminal domain containing 3"
location: "19p13.11"
module: 181
arm: "+"
pooled_cpm: 17.07
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# YJEFN3

*YjeF N-terminal domain containing 3* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.24× (z +6.5, q 4e-08, up in 34 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +6.4, q 4e-08, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.533× (z -5.6, q 1e-05, down in 39 of 48 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HT-29 0.138×; ⚠ toxic; transcription drop); [[Silodosin (drug)]] 5 µM in 1 line (C32 0.113×); [[Digitoxin (drug)]] 5 µM in 1 line (RPMI-7951 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLDN15]] (+0.71, fdr 1e-05), [[NLGN3]] (+0.70, fdr 8e-06), [[MC1R]] (+0.68, fdr 2e-05); moves opposite to [[SDHAF3]] (-0.57, fdr 9e-05), [[SLC25A11]] (-0.55, fdr 1e-04).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC2A9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +6.5 | 4e-08 | 34/48 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +6.4 | 4e-08 | 30/46 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.2 | 9e-08 | 38/47 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.9 | 2e-04 | 14/27 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +4.4 | 1e-03 | 31/47 (SHP-77, NCI-H23, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.009 | 23/48 (A-172, NCI-H2347, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.7 | 0.018 | 20/42 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.046 | 21/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.046 | 23/48 (LS 180, SW48, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14660.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HT-29 0.138×; ⚠ toxic; transcription drop); [[Silodosin (drug)]] 5 µM in 1 line (C32 0.113×); [[Digitoxin (drug)]] 5 µM in 1 line (RPMI-7951 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.533×** | -5.6 | 1e-05 | 39/48 (LoVo, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 13.4 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.113× (z -8.9) |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLDN15]] | +0.71 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.70 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[MC1R]] | +0.68 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[ZFHX2-AS1]] | +0.67 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[COL11A2]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[CCDC17]] | +0.66 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[CFAP53]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[SLC9A5]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.64 | +0.69 / +0.38 | both halves | 7e-05 |  |
| [[PPP1R3F]] | +0.64 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[MYH3]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CFAP70]] | +0.63 | +0.67 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.57 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[SLC25A11]] | -0.55 | -0.48 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A9]] | B | SLC2A9 activity lowers YJEFN3's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.69× higher at baseline in the lines without SLC2A9 | 0.015 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[PYROXD2]] | B | PYROXD2 activity lowers YJEFN3's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without PYROXD2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.7, -13.6); signed map (18.6, 4.2). **Vector** length 83.6, 16.8% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.3 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.6 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.6 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.3 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.3 | +0.7 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[Bexarotene (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.9 | -0.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | YjeF N-terminal domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,528,861-19,537,581 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hYjeF_N3-19p13.11, FLJ44968 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6XGL0](https://www.uniprot.org/uniprotkb/A6XGL0) (YjeF N-terminal domain-containing protein 3):

> May accelerate cholesterol efflux from endothelial cells to high-density lipoprotein (HDL) and thereby regulates angiogenesis. May orchestrate hematopoietic stem and progenitor cell emergence from the hemogenic endothelium, a type of specialized endothelium manifesting hematopoietic potential. YJEFN3-mediated cholesterol efflux activates endothelial SREBF2, the master transcription factor for cholesterol biosynthesis, which in turn transactivates NOTCH and promotes hematopoietic stem and …

**Summary**, from NCBI Gene [374887](https://www.ncbi.nlm.nih.gov/gene/374887):

> Predicted to enable NAD(P)HX epimerase activity. Predicted to be involved in several processes, including hematopoietic stem cell proliferation; membrane raft distribution; and negative regulation of angiogenesis. Predicted to be active in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24785) · Entrez [374887](https://www.ncbi.nlm.nih.gov/gene/374887) · UniProt [A6XGL0](https://www.uniprot.org/uniprotkb/A6XGL0) · Ensembl [ENSG00000250067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250067)

## Data

Gene col 14660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14660); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14660]; `tensor/DDL_lfc|DDL_z.npy` [14660]; `embed/gene_vectors.npy` [14660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14660 or target_col == 14660). Every well: [[YJEFN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YJEFN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
