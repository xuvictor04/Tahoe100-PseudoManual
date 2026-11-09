---
symbol: "MRPL13"
type: "gene"
col: 10220
ensembl_id: "ENSG00000172172"
name: "mitochondrial ribosomal protein L13"
location: "8q24.12"
module: 57
arm: "+"
pooled_cpm: 39.66
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# MRPL13

*mitochondrial ribosomal protein L13* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +9.7, q 2e-19, up in 39 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.37× (z +5.9, q 6e-07, up in 33 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bimatoprost (drug)]] 0.5 µM in 1 line (CHP-212 0.0732×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPC]] (+0.61, fdr 7e-06), [[MRPS14]] (+0.60, fdr 1e-05), [[CWF19L1]] (+0.60, fdr 1e-05); moves opposite to [[MIR23AHG]] (-0.54, fdr 5e-05), [[NR4A1]] (-0.51, fdr 2e-05), [[SMG1P3]] (-0.50, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.00×** | +9.7 | 2e-19 | 39/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.74×** | +7.4 | 3e-11 | 27/37 (Hs 766T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.61×** | +6.2 | 1e-07 | 27/42 (KATO III, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +5.9 | 6e-07 | 33/48 (J82, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.54×** | +5.8 | 7e-07 | 31/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.49×** | +5.4 | 7e-06 | 26/47 (SNU-423, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.42×** | +4.9 | 6e-05 | 30/48 (BT-474, A498, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.30×** | +4.9 | 6e-05 | 30/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.40×** | +4.7 | 2e-04 | 30/48 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.003 | 24/48 (SW480, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.8 | 0.006 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.31×** | +3.8 | 0.007 | 25/48 (BT-474, SHP-77, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.32×** | +3.7 | 0.008 | 24/46 (A-427, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.30×** | +3.7 | 0.008 | 26/46 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.013 | 21/48 (HOP62, HEC-1-A, …) | top dose only | position effect removed |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.070 | 17/48 (SW480, Hs 766T, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.071 | 16/48 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10220.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bimatoprost (drug)]] 0.5 µM in 1 line (CHP-212 0.0732×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.773× | -3.6 | 0.19 | 24/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 68.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0732× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 31.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 86.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SW480 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 89.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPC]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MRPS14]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 998 |
| [[CWF19L1]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[LSM3]] ⚠ | +0.60 | +0.63 / +0.59 | both halves | 7e-06 | STRING 428; ⚠ in the vector space only through flagged drug-doses |
| [[MIGA1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[VIPAS39]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ALG5]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TSNAX]] | +0.55 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[PARL]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[C2orf49]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[VPS37A]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[CDC23]] | +0.53 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[JKAMP]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR23AHG]] | -0.54 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[NR4A1]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SMG1P3]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PABPC4]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[JUN]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[JUNB]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CEACAM19]] | -0.46 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[IER2]] | -0.45 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRPL13's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.348). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.9, -6.9); signed map (-32.9, -24.8). **Vector** length 69.8, 15.9% of its response variance represented; |z| ≥ 3 in 604 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.5 | +5.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.7 | +3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.8 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.4 | +0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.4 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:120,380,761-120,445,402 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L13, RPL13, L13mt, RPML13, L13A, uL13m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9BYD1](https://www.uniprot.org/uniprotkb/Q9BYD1) carries no function annotation.

**Summary**, from NCBI Gene [28998](https://www.ncbi.nlm.nih.gov/gene/28998):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14278) · Entrez [28998](https://www.ncbi.nlm.nih.gov/gene/28998) · UniProt [Q9BYD1](https://www.uniprot.org/uniprotkb/Q9BYD1) · Ensembl [ENSG00000172172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172172)

## Data

Gene col 10220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10220); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10220]; `tensor/DDL_lfc|DDL_z.npy` [10220]; `embed/gene_vectors.npy` [10220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10220 or target_col == 10220). Every well: [[MRPL13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
