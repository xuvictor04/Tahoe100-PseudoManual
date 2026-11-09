---
symbol: "LRRC61"
type: "gene"
col: 4805
ensembl_id: "ENSG00000127399"
name: "leucine rich repeat containing 61"
location: "7q36.1"
module: 7
arm: "+"
pooled_cpm: 6.02
n_lines_expressing: 34
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# LRRC61

*leucine rich repeat containing 61* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.66× (z +11.2, q 3e-26, up in 31 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 3.96×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.363× (z -11.6, q 3e-28, down in 27 of 32 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR3C]] (+0.61, fdr 1e-05, ⚠ same locus), [[C10orf95-AS1]] (+0.61, fdr 4e-05), [[SPR]] (+0.57, fdr 9e-05), [[TGFBRAP1]] (+0.57, fdr 5e-05); moves opposite to [[LGALS1]] (-0.51, fdr 0.001, ⚠ one half only (not replicated)), [[ODF2]] (-0.51, fdr 5e-05), [[MYADM]] (-0.50, fdr 0.001, ⚠ not reproduced), [[SPAG9]] (-0.50, fdr 3e-04), [[NKTR]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SULT1A1]] → it (grade B ⚠); 5 go from it, the strongest it → [[UACA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4805.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 3.96×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.66×** | +11.2 | 3e-26 | 31/32 (SW480, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.1 | 1e-04 | 7/21 (LS 180, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.1 | 0.008 | 5/10 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.058 | 5/24 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.22× | +3.2 | 0.18 | 6/32 (KATO III, NCI-H2347, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.363×** | -11.6 | 3e-28 | 27/32 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.391×** | -10.7 | 2e-24 | 24/32 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -9.8 | 2e-20 | 23/30 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.466×** | -8.7 | 4e-16 | 25/32 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.708×** | -3.9 | 0.009 | 11/32 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.742×** | -3.4 | 0.057 | 11/32 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.567×** | -3.4 | 0.057 | 7/27 (LS 180, A498, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.754×** | -3.2 | 0.086 | 9/29 (Panc 03.27, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.758×** | -3.2 | 0.099 | 11/32 (SW1417, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.3 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.96× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.213× (z -11.4) |
| [[RKO (line)]] | wt | 15.4 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0892× (z -11.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.4) |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0829× (z -8.8) |
| [[SW48 (line)]] | wt | 21.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.163× (z -8.6) |
| [[A-172 (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR3C]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 | STRING 607; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[C10orf95-AS1]] | +0.61 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[SPR]] | +0.57 | +0.50 / +0.37 | both halves | 9e-05 |  |
| [[TGFBRAP1]] | +0.57 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[SPRYD4]] | +0.55 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[LINC01357]] | +0.54 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[MRM1]] | +0.54 | +0.39 / +0.37 | both halves | 8e-05 |  |
| [[C14orf93]] | +0.54 | +0.39 / +0.33 | both halves | 1e-04 |  |
| [[CCNT2]] | +0.54 | +0.24 / +0.45 | both halves | 5e-04 |  |
| [[TIMM8B]] | +0.54 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[MRPL20-AS1]] | +0.53 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[YTHDF2]] | +0.52 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[SMAD1]] | +0.52 | +0.47 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS1]] | -0.51 | -0.53 / -0.14 | ⚠ one half (not replicated) | 0.001 |  |
| [[ODF2]] | -0.51 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[MYADM]] | -0.50 | -0.48 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[GNAI2]] | -0.50 | -0.37 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[SPAG9]] | -0.50 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[NKTR]] | -0.50 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[SYAP1]] | -0.50 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[CDKL5]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[GCAT]] | -0.49 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[DIS3]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MYO1E]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[PI4KA]] | -0.48 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[ARG2]] | -0.47 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[IQGAP1]] | -0.47 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[SLC2A13]] | -0.47 | -0.25 / -0.31 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SULT1A1]] | B | SULT1A1 activity raises LRRC61's level | lines that do not express SULT1A1 (16) vs lines expressing it (34) | 2.37× lower at baseline in the lines without SULT1A1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, KRT18, MARVELD2 |
| [[HDAC6]] | B | HDAC6 activity raises LRRC61's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[UACA]] | B | UACA activity lowers LRRC61's level | lines that do not express UACA (5) vs lines expressing it (45) | 2.59× higher at baseline in the lines without UACA | 0.087 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, PNCK, SPTBN5; maybe low, not absent |
| [[ACTR3C]] | C | ACTR3C activity raises LRRC61's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 4.74× lower at baseline in the lines without ACTR3C | 1e-04 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UACA]] | B | LRRC61 activity lowers UACA's level | lines that do not express LRRC61 (16) vs lines expressing it (34) | 1.91× higher at baseline in the lines without LRRC61 | 0.034 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4 |
| [[SULT1A1]] | B | LRRC61 activity raises SULT1A1's level | lines that do not express LRRC61 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without LRRC61 | 0.039 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4 |
| cells under [[Torkinib (drug)]] 5 µM | B | LRRC61 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express LRRC61 (16) vs lines expressing it (32) | the lines without LRRC61: 0.82× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4 |
| [[SPAG9]] | B | LRRC61 activity lowers SPAG9's level | lines that do not express LRRC61 (16) vs lines expressing it (34) | 1.38× higher at baseline in the lines without LRRC61 | 0.084 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4 |
| [[ACTR3C]] | C | LRRC61 activity raises ACTR3C's level | lines that do not express LRRC61 (16) vs lines expressing it (34) | 4.52× lower at baseline in the lines without LRRC61 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4; co-absent with the target |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.383). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.0, 42.9); signed map (37.0, -18.8). **Vector** length 49.2, 8.34% of its response variance represented; |z| ≥ 3 in 576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +11.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.4 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.8 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -1.8 | -11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -10.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.4 | -8.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 61 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:150,323,263-150,338,156 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3036, FLJ31392, HSPC295 |
| Matched by | ensembl_id |

UniProt [Q9BV99](https://www.uniprot.org/uniprotkb/Q9BV99) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21704) · Entrez [65999](https://www.ncbi.nlm.nih.gov/gene/65999) · UniProt [Q9BV99](https://www.uniprot.org/uniprotkb/Q9BV99) · Ensembl [ENSG00000127399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127399)

## Data

Gene col 4805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4805); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4805]; `tensor/DDL_lfc|DDL_z.npy` [4805]; `embed/gene_vectors.npy` [4805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4805 or target_col == 4805). Every well: [[LRRC61 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC61.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
