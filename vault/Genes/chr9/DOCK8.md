---
symbol: "DOCK8"
type: "gene"
col: 2824
ensembl_id: "ENSG00000107099"
name: "dedicator of cytokinesis 8"
location: "9p24.3"
module: 62
arm: "+"
pooled_cpm: 6.47
n_lines_expressing: 34
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# DOCK8

*dedicator of cytokinesis 8* — 9p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.37× (z +20.8, q 0e+00, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.626× (z -5.7, q 7e-06, down in 11 of 27 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PINCR]] (+0.67, fdr 9e-06), [[SPATA18]] (+0.67, fdr 1e-05), [[ABCA12]] (+0.66, fdr 3e-05); moves opposite to [[AFAP1]] (-0.45, fdr 0.003, ⚠ not reproduced).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +20.8 | 0e+00 | 20/23 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +14.3 | 4e-44 | 2/9 (A498, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.96×** | +11.5 | 1e-28 | 22/29 (LoVo, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +8.6 | 1e-15 | 14/28 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +8.0 | 2e-13 | 10/23 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +8.0 | 2e-13 | 1/9 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.7 | 2e-12 | 6/18 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +7.2 | 3e-11 | 11/27 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.1 | 9e-11 | 10/23 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +6.7 | 1e-09 | 11/26 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.50×** | +4.9 | 6e-05 | 10/26 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.32×** | +4.8 | 8e-05 | 9/29 (NCI-H460, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.6 | 2e-04 | 7/28 (A549, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 6/25 (hTERT-HPNE, A549, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.014 | 3/27 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.014 | 2/28 (HS-578T, SW480) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.018 | 0/24 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.033 | 3/22 (RKO, HCT15, …) | all doses, flat |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.038 | 4/28 (NCI-H2030, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.626×** | -5.7 | 7e-06 | 11/27 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.646×** | -5.3 | 3e-05 | 13/28 (RKO, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.653×** | -5.2 | 4e-05 | 14/27 (SW480, hTERT-HPNE, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.736×** | -3.7 | 0.027 | 10/28 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -3.4 | 0.065 | 9/24 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Acetohexamide (drug)]] 0.05 µM |  | **0.758×** | -3.4 | 0.067 | 1/28 (J82) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.825×** | -3.3 | 0.069 | 3/31 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.601×** | -3.2 | 0.085 | 8/25 (KATO III, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.608×** | -3.2 | 0.096 | 9/23 (hTERT-HPNE, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.774× | -3.1 | 0.10 | 17/31 (hTERT-HPNE, SW480, …) | two highest doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.1 | 0.11 | 4/32 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 63.6 | 0 | 9 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0233× (z -19.3) |
| [[LoVo (line)]] | wt | 21.9 | 3 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.4 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.155× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 29.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 3.04 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.7× (z +15.1) | — |
| [[RKO (line)]] | wt | 39.8 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -14.2) |
| [[A498 (line)]] | wt | 1.97 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 29.0× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 6.52 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0465× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0394× (z -16.8) |
| [[A549 (line)]] | wt | 12.3 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.55× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 4.56 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0608× (z -8.6) |
| [[A-172 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.974 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PINCR]] | +0.67 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[SPATA18]] | +0.67 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ABCA12]] | +0.66 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[GLS2]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NINJ2]] | +0.63 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[ZNF423]] | +0.62 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[INKA2]] | +0.61 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[EFCAB5]] | +0.59 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[ACTA2]] | +0.57 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[INSYN2A]] | +0.57 | +0.19 / +0.59 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DNAI3]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[GALNTL6]] | +0.56 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[LRATD1]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFAP1]] | -0.45 | -0.41 / -0.10 | ⚠ not reproduced | 0.003 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DOCK8's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.3% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises DOCK8's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without GRIN2C | 0.053 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, 36.7); signed map (42.9, -22.6). **Vector** length 63.6, 13.5% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +20.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.0 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +14.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +8.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | +0.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.1 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.5 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.3 — chr9:214,854-465,259 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00026, FLJ00152, ZIR8, FLJ00346 |
| Gene groups (HGNC) | Armadillo like helical domain containing; DOCK family Rho GEFs |
| Reactome | 8 pathways, smallest: RHOJ GTPase cycle; Factors involved in megakaryocyte development and platelet production; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NF50](https://www.uniprot.org/uniprotkb/Q8NF50) (Dedicator of cytokinesis protein 8):

> Guanine nucleotide exchange factor (GEF) which specifically activates small GTPase CDC42 by exchanging bound GDP for free GTP. During immune responses, required for interstitial dendritic cell (DC) migration by locally activating CDC42 at the leading edge membrane of DC (By similarity). Required for CD4(+) T-cell migration in response to chemokine stimulation by promoting CDC42 activation at T cell leading edge membrane. Is involved in NK cell cytotoxicity by controlling polarization of …

**Summary**, from NCBI Gene [81704](https://www.ncbi.nlm.nih.gov/gene/81704):

> This gene encodes a member of the DOCK180 family of guanine nucleotide exchange factors. Guanine nucleotide exchange factors interact with Rho GTPases and are components of intracellular signaling networks. Mutations in this gene result in the autosomal recessive form of the hyper-IgE syndrome. Alternatively spliced transcript variants encoding different isoforms have been described.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:19191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19191) · Entrez [81704](https://www.ncbi.nlm.nih.gov/gene/81704) · UniProt [Q8NF50](https://www.uniprot.org/uniprotkb/Q8NF50) · Ensembl [ENSG00000107099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107099)

## Data

Gene col 2824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2824); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2824]; `tensor/DDL_lfc|DDL_z.npy` [2824]; `embed/gene_vectors.npy` [2824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2824 or target_col == 2824). Every well: [[DOCK8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
