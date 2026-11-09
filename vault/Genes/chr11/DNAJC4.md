---
symbol: "DNAJC4"
type: "gene"
col: 3099
ensembl_id: "ENSG00000110011"
name: "DnaJ heat shock protein family (Hsp40) member C4"
location: "11q13.1"
module: 24
arm: "+"
pooled_cpm: 7.59
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DNAJC4

*DnaJ heat shock protein family (Hsp40) member C4* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.87× (z +8.4, q 2e-14, up in 10 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +5.8, q 1e-06, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -6.4, q 1e-07, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG7]] (+0.72, fdr 7e-06), [[TRIM7-AS2]] (+0.72, fdr 1e-05), [[SNHG19]] (+0.71, fdr 7e-06); moves opposite to [[IPO9]] (-0.67, fdr 7e-06), [[COA7]] (-0.66, fdr 1e-05), [[CCT5]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPAG4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +8.4 | 2e-14 | 10/14 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +7.7 | 3e-12 | 26/32 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.8 | 1e-06 | 33/41 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.8 | 0.019 | 20/34 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.57× | +3.2 | 0.16 | 10/23 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.30× | +3.1 | 0.21 | 9/46 (HT-29, Hs 766T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3099.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.582×** | -6.4 | 1e-07 | 30/42 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -5.6 | 7e-06 | 29/40 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.532×** | -5.2 | 3e-05 | 29/46 (COLO 205, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -4.3 | 0.003 | 22/47 (SHP-77, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -4.1 | 0.006 | 20/46 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.649×** | -3.6 | 0.030 | 18/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -3.5 | 0.034 | 16/46 (SHP-77, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 5 µM |  | **0.749×** | -3.4 | 0.048 | 17/48 (COLO 205, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.676×** | -3.3 | 0.071 | 12/47 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.671×** | -3.2 | 0.081 | 15/44 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.691× | -3.1 | 0.11 | 13/46 (BT-474, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.695× | -3.0 | 0.12 | 13/46 (H4, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 9.93 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0581× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 5.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 9.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -8.9) |
| [[SW 900 (line)]] | alt | 7.37 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -13.0) |
| [[A-172 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | +0.72 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[TRIM7-AS2]] | +0.72 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.71 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.71 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[TRIM52-AS1]] | +0.71 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.70 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[SMIM27]] | +0.69 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[WBP1]] | +0.68 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[MIR4458HG]] | +0.67 | +0.48 / +0.76 | both halves | 2e-05 |  |
| [[TMEM258]] | +0.67 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.66 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[SNHG9]] | +0.66 | +0.36 / +0.75 | both halves | 1e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | -0.67 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[COA7]] | -0.66 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[CCT5]] | -0.65 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.63 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[FARSB]] | -0.62 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.61 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[PTPN11]] | -0.61 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[G3BP1]] | -0.60 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[SACS]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 | same gene group |
| [[CCT2]] | -0.60 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.59 | -0.55 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPAG4]] | B | SPAG4 activity raises DNAJC4's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without SPAG4 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.9, -22.6); signed map (-27.9, 8.7). **Vector** length 51.7, 8.41% of its response variance represented; |z| ≥ 3 in 630 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.1 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,230,278-64,234,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCG18; previously HSPF2 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

UniProt [Q9NNZ3](https://www.uniprot.org/uniprotkb/Q9NNZ3) carries no function annotation.

**Summary**, from NCBI Gene [3338](https://www.ncbi.nlm.nih.gov/gene/3338):

> Predicted to enable unfolded protein binding activity. Predicted to be involved in protein folding and response to unfolded protein. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5271) · Entrez [3338](https://www.ncbi.nlm.nih.gov/gene/3338) · UniProt [Q9NNZ3](https://www.uniprot.org/uniprotkb/Q9NNZ3) · Ensembl [ENSG00000110011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110011)

## Data

Gene col 3099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3099); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3099]; `tensor/DDL_lfc|DDL_z.npy` [3099]; `embed/gene_vectors.npy` [3099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3099 or target_col == 3099). Every well: [[DNAJC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
