---
symbol: "PIGP"
type: "gene"
col: 11735
ensembl_id: "ENSG00000185808"
name: "phosphatidylinositol glycan anchor biosynthesis class P"
location: "21q22.13"
module: 35
arm: "+"
pooled_cpm: 8.29
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PIGP

*phosphatidylinositol glycan anchor biosynthesis class P* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +7.2, q 3e-10, up in 25 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +6.7, q 4e-09, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.446× (z -7.2, q 4e-10, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf71]] (+0.82, fdr 7e-06), [[MDP1]] (+0.79, fdr 7e-06), [[NSMCE1-DT]] (+0.78, fdr 9e-06); moves opposite to [[GNB1L]] (-0.66, fdr 1e-05), [[TREX2]] (-0.65, fdr 1e-05), [[AP3M2]] (-0.65, fdr 8e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TCEAL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.2 | 3e-10 | 25/30 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +6.9 | 1e-09 | 14/15 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.7 | 4e-09 | 32/43 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +5.6 | 4e-06 | 28/47 (A-427, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +4.8 | 2e-04 | 13/22 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.066 | 19/38 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.066 | 11/43 (SK-MEL-2, PANC-1, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.40× | +3.1 | 0.16 | 13/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.446×** | -7.2 | 4e-10 | 36/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -6.4 | 3e-08 | 34/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.508×** | -6.0 | 3e-07 | 29/46 (HCT15, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.539×** | -5.5 | 6e-06 | 26/47 (COLO 205, LoVo, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.543×** | -5.4 | 7e-06 | 29/47 (H4, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.551×** | -5.3 | 1e-05 | 26/47 (SW480, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -5.2 | 2e-05 | 25/42 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.344×** | -5.0 | 5e-05 | 25/42 (COLO 205, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -4.9 | 5e-05 | 26/44 (MIA PaCa-2, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.652×** | -3.8 | 0.008 | 18/46 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -3.5 | 0.023 | 20/43 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.684×** | -3.4 | 0.037 | 16/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.698×** | -3.2 | 0.064 | 14/47 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.689×** | -3.1 | 0.075 | 17/45 (HCT15, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0909× (z -10.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.104× (z -9.0) |
| [[PANC-1 (line)]] | alt | 7.82 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -8.7) |
| [[H4 (line)]] | wt | 12.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0487× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0677× (z -11.8) |
| [[A-172 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf71]] | +0.82 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[MDP1]] | +0.79 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NSMCE1-DT]] | +0.78 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[ATE1OSP]] | +0.76 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.75 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.75 | +0.80 / +0.51 | both halves | 1e-05 |  |
| [[APPBP2-DT]] | +0.75 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[EIF3J-DT]] | +0.75 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[ZC2HC1C]] | +0.74 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[NUTM2E]] | +0.74 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[RAB21]] | +0.73 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[AHI1-DT]] | +0.73 | +0.74 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB1L]] | -0.66 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TREX2]] | -0.65 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.65 | -0.69 / -0.37 | both halves | 8e-05 |  |
| [[TEX2]] | -0.64 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PARP1]] | -0.63 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[BLTP2]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCEAL3]] | B | TCEAL3 activity lowers PIGP's level | lines that do not express TCEAL3 (7) vs lines expressing it (43) | 1.30× higher at baseline in the lines without TCEAL3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises PIGP's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.15× lower at baseline in the lines without PLS3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (6.6, 20.9); signed map (21.6, -12.8). **Vector** length 58.4, 9.74% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.8 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.9 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | -5.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.7 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -0.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class P |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.13 — chr21:37,062,846-37,073,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DCRC, DSRC; previously DSCR5 |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; Glycosylphosphatidylinositol-N-acetylglucosaminyltransferase complex |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P57054](https://www.uniprot.org/uniprotkb/P57054) (Phosphatidylinositol N-acetylglucosaminyltransferase subunit P):

> Part of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase (GPI-GnT) complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to phosphatidylinositol and participates in the first step of GPI biosynthesis.

**Summary**, from NCBI Gene [51227](https://www.ncbi.nlm.nih.gov/gene/51227):

> This gene encodes an enzyme involved in the first step of glycosylphosphatidylinositol (GPI)-anchor biosynthesis. The GPI-anchor is a glycolipid found on many blood cells that serves to anchor proteins to the cell surface. The encoded protein is a component of the GPI-N-acetylglucosaminyltransferase complex that catalyzes the transfer of N-acetylglucosamine (GlcNAc) from UDP-GlcNAc to phosphatidylinositol (PI). This gene is located in the Down Syndrome critical region on chromosome 21 and is a …

**Accessions** — [HGNC:3046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3046) · Entrez [51227](https://www.ncbi.nlm.nih.gov/gene/51227) · UniProt [P57054](https://www.uniprot.org/uniprotkb/P57054) · Ensembl [ENSG00000185808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185808)

## Data

Gene col 11735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11735); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11735]; `tensor/DDL_lfc|DDL_z.npy` [11735]; `embed/gene_vectors.npy` [11735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11735 or target_col == 11735). Every well: [[PIGP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
