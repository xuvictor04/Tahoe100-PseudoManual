---
symbol: "STARD3"
type: "gene"
col: 5240
ensembl_id: "ENSG00000131748"
name: "StAR related lipid transfer domain containing 3"
location: "17q12"
module: 142
arm: "+"
pooled_cpm: 29.42
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# STARD3

*StAR related lipid transfer domain containing 3* — 17q12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 0.05 µM in 1 line (BT-474 1.88×; ⚠ cell-cycle shift, explains ~5% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.663× (z -10.7, q 1e-23, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB16-AS1]] (+0.72, fdr 7e-06), [[PGS1]] (+0.69, fdr 7e-06), [[RNF121]] (+0.67, fdr 7e-06); moves opposite to [[DZIP3]] (-0.65, fdr 1e-05), [[ANKRD31]] (-0.61, fdr 4e-05), [[SYNE1]] (-0.61, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DSP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5240.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 0.05 µM in 1 line (BT-474 1.88×; ⚠ cell-cycle shift, explains ~5% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +3.4 | 0.22 | 15/48 (BT-474, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | 1.20× | +3.2 | 0.22 | 15/45 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.19× | +3.2 | 0.22 | 12/47 (BT-474, SW480, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.22 | 12/46 (hTERT-HPNE, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.27 | 6/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.663×** | -10.7 | 1e-23 | 38/47 (A-427, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -7.7 | 4e-12 | 34/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.659×** | -7.3 | 4e-11 | 35/47 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.706×** | -6.4 | 3e-08 | 30/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.730×** | -5.3 | 1e-05 | 20/39 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.776×** | -4.4 | 8e-04 | 16/47 (SW 900, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Binimetinib (drug)]] 5 µM |  | 0.847× | -3.8 | 0.014 | 12/48 (C32, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.819×** | -3.6 | 0.019 | 19/44 (A-427, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.5 | 0.027 | 1/48 (SW 1271) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.831×** | -3.4 | 0.042 | 13/48 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.1 | 0.11 | 8/48 (NCI-H1573, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.875× | -3.1 | 0.11 | 14/48 (A-427, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.9) |
| [[BT-474 (line)]] | alt | 279 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 1.88× (z +9.1) ⚠ cell-cycle shift, explains ~5% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 22.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -8.9) |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.9) |
| [[C-33 A (line)]] | alt | 23.6 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.193× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.5) |
| [[COLO 205 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.3) |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.127× (z -9.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -8.5) |
| [[A-172 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB16-AS1]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[PGS1]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[RNF121]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[GBA2]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.66 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[GPR89A]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CCT6P3-1]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[C1orf52]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.64 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[CSK]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MARK4]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CERS5]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZIP3]] | -0.65 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[ANKRD31]] | -0.61 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[SYNE1]] | -0.61 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[LGALS3]] | -0.61 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[ZNF474]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ATF3]] | -0.59 | -0.58 / -0.60 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[RASEF]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[DARS1]] | -0.59 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[CPEB2]] | -0.58 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[BMI1]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[LINC00882]] | -0.57 | -0.57 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSP]] | B | DSP activity raises STARD3's level | lines that do not express DSP (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without DSP | 0.040 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.2, -2.2); signed map (-44.8, 1.8). **Vector** length 83.0, 15.5% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +3.2 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +3.2 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +3.0 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.6 | +3.0 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | +1.5 | +1.8 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.1 | -5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | StAR related lipid transfer domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,637,090-39,664,201 (+) |
| Ensembl biotype | protein_coding |
| Also known as | es64, MLN64 |
| Gene groups (HGNC) | StAR related lipid transfer domain containing |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 4 pathways, smallest: Pregnenolone biosynthesis; Metabolism of steroid hormones; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14849](https://www.uniprot.org/uniprotkb/Q14849) (StAR-related lipid transfer protein 3):

> Sterol-binding protein that mediates cholesterol transport from the endoplasmic reticulum to endosomes. The sterol transport mechanism is triggered by phosphorylation of FFAT motif that leads to membrane tethering between the endoplasmic reticulum and late endosomes via interaction with VAPA and VAPB. Acts as a lipid transfer protein that redirects sterol to the endosome at the expense of the cell membrane and favors membrane formation inside endosomes. May also mediate cholesterol transport …

**Summary**, from NCBI Gene [10948](https://www.ncbi.nlm.nih.gov/gene/10948):

> This gene encodes a member of a subfamily of lipid trafficking proteins that are characterized by a C-terminal steroidogenic acute regulatory domain and an N-terminal metastatic lymph node 64 domain. The encoded protein localizes to the membranes of late endosomes and may be involved in exporting cholesterol. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:17579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17579) · Entrez [10948](https://www.ncbi.nlm.nih.gov/gene/10948) · UniProt [Q14849](https://www.uniprot.org/uniprotkb/Q14849) · Ensembl [ENSG00000131748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131748)

## Data

Gene col 5240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5240); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5240]; `tensor/DDL_lfc|DDL_z.npy` [5240]; `embed/gene_vectors.npy` [5240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5240 or target_col == 5240). Every well: [[STARD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
