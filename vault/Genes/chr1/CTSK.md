---
symbol: "CTSK"
type: "gene"
col: 6733
ensembl_id: "ENSG00000143387"
name: "cathepsin K"
location: "1q21.3"
module: 37
arm: "+"
pooled_cpm: 12.99
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CTSK

*cathepsin K* — 1q21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.565× (z -6.8, q 4e-09, down in 27 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.610× (z -5.9, q 9e-07, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BNIPL]] (+0.56, fdr 2e-05), [[EFCAB12]] (+0.51, fdr 2e-05), [[GET1-SH3BGR]] (+0.51, fdr 3e-05); moves opposite to [[TIMM8B]] (-0.51, fdr 2e-05), [[LRRC61]] (-0.42, fdr 2e-04), [[SINHCAF]] (-0.42, fdr 3e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APH1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.565×** | -6.8 | 4e-09 | 27/45 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -5.9 | 9e-07 | 26/46 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.435×** | -5.2 | 4e-05 | 24/48 (NCI-H23, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.634×** | -5.1 | 4e-05 | 24/46 (A498, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -5.1 | 4e-05 | 26/45 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.668×** | -4.8 | 1e-04 | 22/44 (H4, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.672×** | -4.8 | 2e-04 | 21/46 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.659×** | -4.7 | 2e-04 | 23/44 (hTERT-HPNE, HEC-1-A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.692×** | -4.1 | 0.002 | 21/46 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.793×** | -3.9 | 0.005 | 22/47 (SW 900, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **0.714×** | -3.8 | 0.008 | 17/40 (NCI-H1792, A549, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.555×** | -3.7 | 0.011 | 18/43 (Hs 766T, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -3.6 | 0.015 | 15/43 (LS 180, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -3.5 | 0.015 | 12/46 (A549, SW480, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.730×** | -3.5 | 0.015 | 19/45 (C32, SNU-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.735×** | -3.4 | 0.023 | 17/43 (SNU-1, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -3.0 | 0.068 | 14/48 (Hs 766T, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 25.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0602× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.224× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 5.40 | 0 | 2 (2 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0719× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 13.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -10.2) |
| [[A498 (line)]] | wt | 8.97 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -11.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A549 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[C32 (line)]] | wt | 9.14 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0970× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 1 | — | [[Radotinib (drug)]] 5 µM 0.107× (z -10.7) |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0666× (z -8.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -9.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0750× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 9.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BNIPL]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[EFCAB12]] | +0.51 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[GET1-SH3BGR]] | +0.51 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[RBM44]] | +0.49 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[SLC22A13]] | +0.48 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[TNXB]] | +0.48 | +0.58 / +0.40 | both halves | 5e-05 | pathway: Extracellular matrix organization |
| [[CLEC4A]] | +0.48 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[TMED6]] | +0.48 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[IL20RB]] | +0.48 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[SH3BP5-AS1]] | +0.47 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ASIC4]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[RFPL3S]] | +0.46 | +0.33 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM8B]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[LRRC61]] | -0.42 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[SINHCAF]] | -0.42 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[RAD51B]] | -0.42 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[KIF26B]] | -0.41 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[BCL2]] | -0.40 | -0.46 / -0.34 | both halves | 1e-04 | STRING 928 |
| [[ZNF462]] | -0.40 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[FJX1]] | -0.40 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[MRTO4]] | -0.40 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[MAP3K1]] | -0.40 | -0.36 / -0.37 | both halves | 1e-04 | pathway: Toll-like Receptor Cascades |
| [[SPATS2L]] | -0.39 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[SPHK1]] | -0.39 | -0.27 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APH1B]] | B | APH1B activity raises CTSK's level | lines that do not express APH1B (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without APH1B | 0.082 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.396). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, -21.5); signed map (9.8, 6.5). **Vector** length 59.3, 8.72% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.4 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | -0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.0 | +0.3 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.6 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.5 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,794,880-150,809,577 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKND; previously CTSO2, CTSO, PYCD |
| Gene groups (HGNC) | Cathepsins; Elastases; Cysteine endopeptidases |
| Hallmark sets | COAGULATION |
| Reactome | 14 pathways, smallest: RUNX1 regulates transcription of genes involved in differentiation of keratinocytes; Trafficking and processing of endosomal TLR; Activation of Matrix Metalloproteinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P43235](https://www.uniprot.org/uniprotkb/P43235) (Cathepsin K):

> Thiol protease involved in osteoclastic bone resorption and may participate partially in the disorder of bone remodeling. Displays potent endoprotease activity against fibrinogen at acid pH. May play an important role in extracellular matrix degradation. Involved in the release of thyroid hormone thyroxine (T4) by limited proteolysis of TG/thyroglobulin in the thyroid follicle lumen.

**Summary**, from NCBI Gene [1513](https://www.ncbi.nlm.nih.gov/gene/1513):

> The protein encoded by this gene is a lysosomal cysteine proteinase involved in bone remodeling and resorption. This protein, which is a member of the peptidase C1 protein family, is predominantly expressed in osteoclasts. However, the encoded protein is also expressed in a significant fraction of human breast cancers, where it could contribute to tumor invasiveness. Mutations in this gene are the cause of pycnodysostosis, an autosomal recessive disease characterized by osteosclerosis and short …

**Accessions** — [HGNC:2536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2536) · Entrez [1513](https://www.ncbi.nlm.nih.gov/gene/1513) · UniProt [P43235](https://www.uniprot.org/uniprotkb/P43235) · Ensembl [ENSG00000143387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143387)

## Data

Gene col 6733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6733); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6733]; `tensor/DDL_lfc|DDL_z.npy` [6733]; `embed/gene_vectors.npy` [6733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6733 or target_col == 6733). Every well: [[CTSK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
