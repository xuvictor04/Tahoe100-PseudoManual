---
symbol: "LENG1"
type: "gene"
col: 2628
ensembl_id: "ENSG00000105617"
name: "leukocyte receptor cluster member 1"
location: "19q13.42"
module: 11
arm: "+"
pooled_cpm: 6.57
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# LENG1

*leukocyte receptor cluster member 1* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +10.3, q 3e-22, up in 31 of 40 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.26× (z +9.1, q 2e-17, up in 35 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Sunitinib (drug)]] 0.05 µM in 1 line (BT-474 0.0740×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.173×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cabozantinib (S-malate) (drug)]] 0.05 µM in 1 line (NCI-H23 0.0687×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF6]] (+0.73, fdr 7e-06), [[TBCC]] (+0.73, fdr 7e-06), [[CCDC174]] (+0.72, fdr 7e-06); moves opposite to [[PPT1]] (-0.62, fdr 1e-05), [[CRTAP]] (-0.62, fdr 7e-06), [[DANCR]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM132D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.01×** | +10.3 | 3e-22 | 31/40 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.35×** | +9.2 | 1e-17 | 37/46 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.26×** | +9.1 | 2e-17 | 35/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +8.7 | 4e-16 | 29/39 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +6.6 | 4e-09 | 29/46 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.4 | 1e-08 | 24/42 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +5.5 | 2e-06 | 25/44 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +4.9 | 6e-05 | 22/47 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.6 | 3e-04 | 19/45 (J82, H4, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +4.3 | 0.001 | 19/44 (SW480, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.002 | 12/45 (SK-MEL-2, LS 180, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.0 | 0.003 | 4/48 (BT-474, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.007 | 13/41 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.30×** | +3.7 | 0.007 | 5/47 (A-172, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.39×** | +3.6 | 0.010 | 13/35 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.013 | 6/47 (KATO III, HT-29, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +3.3 | 0.030 | 8/41 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.036 | 6/44 (A-427, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Sunitinib (drug)]] 0.05 µM in 1 line (BT-474 0.0740×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.173×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cabozantinib (S-malate) (drug)]] 0.05 µM in 1 line (NCI-H23 0.0687×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.89 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 6.20 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0740× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 9.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 4.04 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.05 µM 0.0687× (z -8.5) |
| [[A-172 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF6]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[TBCC]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[ZNF557]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[R3HCC1]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MED19]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[FAM32A]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ELOF1]] | +0.68 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.68 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.67 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[UTP3]] | +0.66 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[PHAX]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | -0.62 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.62 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[DANCR]] | -0.62 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[NUTF2]] | -0.61 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[STT3B]] | -0.59 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.59 | -0.51 / -0.60 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RBBP4]] | -0.58 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[SELENON]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[CTSZ]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[SMG1P1]] | -0.56 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[TMEM123]] | -0.56 | -0.58 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM132D]] | B | TMEM132D activity raises LENG1's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.19× lower at baseline in the lines without TMEM132D | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.9, 0.6); signed map (-1.3, -16.3). **Vector** length 62.5, 10.7% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.9 | +9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.1 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.2 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.1 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | leukocyte receptor cluster member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,155,161-54,159,721 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

UniProt [Q96BZ8](https://www.uniprot.org/uniprotkb/Q96BZ8) carries no function annotation.

**Summary**, from NCBI Gene [79165](https://www.ncbi.nlm.nih.gov/gene/79165):

> Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15502) · Entrez [79165](https://www.ncbi.nlm.nih.gov/gene/79165) · UniProt [Q96BZ8](https://www.uniprot.org/uniprotkb/Q96BZ8) · Ensembl [ENSG00000105617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105617)

## Data

Gene col 2628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2628); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2628]; `tensor/DDL_lfc|DDL_z.npy` [2628]; `embed/gene_vectors.npy` [2628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2628 or target_col == 2628). Every well: [[LENG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LENG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
