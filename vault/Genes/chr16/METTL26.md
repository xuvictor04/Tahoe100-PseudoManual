---
symbol: "METTL26"
type: "gene"
col: 5110
ensembl_id: "ENSG00000130731"
name: "methyltransferase like 26"
location: "16p13.3"
module: 3
arm: "+"
pooled_cpm: 17.03
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# METTL26

*methyltransferase like 26* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.80× (z +7.6, q 2e-11, up in 33 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 5.80×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.273× (z -13.6, q 2e-39, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM256]] (+0.82, fdr 7e-06), [[YIF1B]] (+0.74, fdr 4e-05), [[MRPL55]] (+0.73, fdr 7e-06); moves opposite to [[ANKRD18A]] (-0.63, fdr 5e-04), [[GALNT7-DT]] (-0.63, fdr 1.00, ⚠ one half only (not replicated)), [[ARSB]] (-0.62, fdr 3e-04), [[EPM2A]] (-0.60, fdr 5e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FGF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5110.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 5.80×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +7.6 | 2e-11 | 33/37 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +6.5 | 2e-08 | 24/29 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | 1.54× | +3.2 | 0.23 | 21/43 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.273×** | -13.6 | 2e-39 | 44/46 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.328×** | -8.3 | 4e-14 | 44/46 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.383×** | -7.1 | 2e-10 | 42/47 (HT-29, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.439×** | -6.1 | 2e-07 | 41/47 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -5.1 | 4e-05 | 30/45 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.525×** | -4.8 | 2e-04 | 36/45 (HOP62, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.553×** | -4.4 | 0.001 | 30/45 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -4.1 | 0.003 | 28/45 (NCI-H1792, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.584×** | -4.0 | 0.005 | 26/45 (BT-474, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -3.4 | 0.032 | 25/46 (SK-MEL-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.624×** | -3.4 | 0.032 | 22/45 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0831× (z -13.2) |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -12.4) |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.4) |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -13.6) |
| [[PANC-1 (line)]] | alt | 28.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.7) |
| [[SW480 (line)]] | alt | 9.24 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.6) |
| [[A-172 (line)]] | wt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.2) |
| [[A498 (line)]] | wt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -10.3) |
| [[A549 (line)]] | wt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -11.9) |
| [[BT-474 (line)]] | alt | 9.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0697× (z -10.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.4) |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -10.1) |
| [[HOP62 (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.1) |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -8.5) |
| [[J82 (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.2) |
| [[KATO III (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.4) |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.5) |
| [[A-427 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 11 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM256]] | +0.82 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[YIF1B]] | +0.74 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[MRPL55]] | +0.73 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[POLR2I]] | +0.71 | +0.43 / +0.68 | both halves | 4e-05 |  |
| [[STUB1]] | +0.71 | +0.35 / +0.55 | both halves | 1e-04 | ⚠ same locus (43.9 kb: neighbours can correlate without regulation) |
| [[ARL3]] | +0.70 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[TRPT1]] | +0.69 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.69 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[ANAPC11]] | +0.69 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RRAS]] | +0.69 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[HEATR5B]] | +0.68 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[KIAA1328]] | +0.68 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[SSNA1]] | +0.66 | +0.25 / +0.67 | both halves | 4e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18A]] | -0.63 | -0.58 / -0.23 | both halves | 5e-04 |  |
| [[GALNT7-DT]] | -0.63 | -0.61 / +0.02 | ⚠ one half (not replicated) | 1.00 |  |
| [[ARSB]] | -0.62 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[ST7L]] | -0.62 | -0.66 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[ANKRD18B]] | -0.61 | -0.50 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[IQCH-AS1]] | -0.61 | -0.66 / -0.04 | ⚠ one half (not replicated) | 0.005 |  |
| [[FBXL19-AS1]] | -0.61 | -0.53 / -0.01 | ⚠ one half (not replicated) | 0.008 |  |
| [[EPM2A]] | -0.60 | -0.44 / -0.24 | both halves | 5e-04 |  |
| [[GABPB1-AS1]] | -0.60 | -0.57 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[ZFP91]] | -0.60 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[CRPPA]] | -0.60 | -0.44 / -0.21 | both halves | 7e-04 |  |
| [[WARS2-AS1]] | -0.60 | -0.64 / +0.02 | ⚠ one half (not replicated) | 1.00 |  |
| [[RCC2]] | -0.59 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[FGF2]] | -0.59 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF2]] | B | FGF2 activity raises METTL26's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 1.46× lower at baseline in the lines without FGF2 | 0.047 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[CRPPA]] | B | CRPPA activity raises METTL26's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without CRPPA | 0.060 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[LINC02977]] | B | LINC02977 activity raises METTL26's level | lines that do not express LINC02977 (8) vs lines expressing it (42) | 1.48× lower at baseline in the lines without LINC02977 | 0.083 | ⚠ within organs, on part of the lines; also absent: SUSD1, FAM83G; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.7, -14.4); signed map (-32.9, 15.4). **Vector** length 65.3, 15.9% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +0.9 | +0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +0.8 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.8 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -13.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase like 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:634,427-636,366 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13114; previously C16orf13 |
| Gene groups (HGNC) | 7BS orphan methyltransferases |
| Matched by | ensembl_id |

UniProt [Q96S19](https://www.uniprot.org/uniprotkb/Q96S19) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:14141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14141) · Entrez [84326](https://www.ncbi.nlm.nih.gov/gene/84326) · UniProt [Q96S19](https://www.uniprot.org/uniprotkb/Q96S19) · Ensembl [ENSG00000130731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130731)

## Data

Gene col 5110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5110); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5110]; `tensor/DDL_lfc|DDL_z.npy` [5110]; `embed/gene_vectors.npy` [5110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5110 or target_col == 5110). Every well: [[METTL26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
