---
symbol: "CLDN15"
type: "gene"
col: 2758
ensembl_id: "ENSG00000106404"
name: "claudin 15"
location: "7q22.1"
module: 39
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# CLDN15

*claudin 15* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +8.9, q 3e-16, up in 21 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW1417 0.0742×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0997×); [[Cobimetinib (drug)]] 5 µM in 1 line (SW1417 0.0886×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRK7]] (+0.76, fdr 7e-06), [[NLGN3]] (+0.74, fdr 7e-06), [[CFAP70]] (+0.73, fdr 7e-06); moves opposite to [[SDHAF3]] (-0.64, fdr 2e-05), [[TMEM106C]] (-0.61, fdr 1e-05), [[IDH2]] (-0.60, fdr 4e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TLCD4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +8.9 | 3e-16 | 21/38 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +6.5 | 3e-08 | 16/37 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.7 | 2e-06 | 2/6 (NCI-H2347, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.3 | 2e-05 | 16/44 (LoVo, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.8 | 2e-04 | 7/29 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.57×** | +4.7 | 3e-04 | 12/42 (SW480, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.5 | 5e-04 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.010 | 6/48 (LoVo, SW480, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.019 | 7/35 (HT-29, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.096 | 3/41 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2758.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW1417 0.0742×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0997×); [[Cobimetinib (drug)]] 5 µM in 1 line (SW1417 0.0886×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bexarotene (drug)]] 5 µM |  | 0.714× | -3.7 | 0.13 | 5/47 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.732× | -3.3 | 0.30 | 9/45 (HepG2/C3A, LoVo, …) | top dose only | plate-row cell shift |
| [[Silodosin (drug)]] 5 µM |  | 0.744× | -3.1 | 0.36 | 8/37 (Panc 03.27, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 4.46 | 0 | 2 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0742× (z -10.4) |
| [[A-172 (line)]] | wt | 4.49 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0968× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 4.20 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM 0.0816× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 3.39 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0997× (z -10.0) |
| [[A-427 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK7]] | +0.76 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[CFAP70]] | +0.73 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[YJEFN3]] | +0.71 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.71 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[TMEM236]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[YIPF7]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[CELF6]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[C19orf18]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.64 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TMEM106C]] | -0.61 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[IDH2]] | -0.60 | -0.62 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD4]] | B | TLCD4 activity raises CLDN15's level | lines that do not express TLCD4 (11) vs lines expressing it (39) | 1.27× lower at baseline in the lines without TLCD4 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, -13.6); signed map (18.4, 4.9). **Vector** length 48.7, 5.14% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -0.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | claudin 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,232,092-101,238,820 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Claudins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P56746](https://www.uniprot.org/uniprotkb/P56746) (Claudin-15):

> Forms paracellular channels: polymerizes in tight junction strands with cation- and water-selective channels through the strands, conveying epithelial permeability in a process known as paracellular tight junction permeability. In intestinal epithelium, allows for sodium and water fluxes from the peritoneal side to the lumen of the intestine to regulate nutrient absorption and intestinal morphogenesis (By similarity).

**Summary**, from NCBI Gene [24146](https://www.ncbi.nlm.nih.gov/gene/24146):

> This gene encodes a member of the claudin family. Claudins are integral membrane proteins and components of tight junction strands. Tight junction strands serve as a physical barrier to prevent solutes and water from passing freely through the paracellular space between epithelial or endothelial cell sheets, and also play critical roles in maintaining cell polarity and signal transductions. Alternatively spliced transcript variants encoding the same protein have been found for this gene. …

**Accessions** — [HGNC:2036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2036) · Entrez [24146](https://www.ncbi.nlm.nih.gov/gene/24146) · UniProt [P56746](https://www.uniprot.org/uniprotkb/P56746) · Ensembl [ENSG00000106404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106404)

## Data

Gene col 2758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2758); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2758]; `tensor/DDL_lfc|DDL_z.npy` [2758]; `embed/gene_vectors.npy` [2758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2758 or target_col == 2758). Every well: [[CLDN15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
