---
symbol: "HERC2P3"
type: "gene"
col: 11090
ensembl_id: "ENSG00000180229"
name: "HERC2 pseudogene 3"
location: "15q11.1-q11.2"
module: 36
arm: "+"
pooled_cpm: 2.53
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# HERC2P3

*HERC2 pseudogene 3* — 15q11.1-q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.64× (z +10.7, q 5e-24, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.94× (z +7.6, q 7e-12, up in 16 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.597× (z -5.7, q 7e-06, down in 9 of 37 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.668× (z -4.6, q 0.001, down in 17 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.05 µM in 1 line (HOP62 0.0636×); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.141×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERC2P9]] (+0.90, fdr 7e-06), [[HERC2P2]] (+0.89, fdr 7e-06), [[HERC2]] (+0.78, fdr 7e-06); moves opposite to [[ATP23]] (-0.71, fdr 1e-05), [[SGO1-AS1]] (-0.67, fdr 1e-05), [[FAM200B]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NFATC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +10.7 | 5e-24 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +7.6 | 7e-12 | 16/41 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +7.6 | 7e-12 | 20/44 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.2 | 8e-11 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.92×** | +7.1 | 2e-10 | 16/37 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +6.3 | 2e-08 | 15/43 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +6.1 | 6e-08 | 15/42 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +6.1 | 8e-08 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +5.5 | 3e-06 | 12/39 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.003 | 3/22 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.0 | 0.003 | 2/6 (PANC-1, RKO) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.9 | 0.004 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.7 | 0.011 | 1/19 (A498) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.37×** | +3.5 | 0.018 | 1/9 (SW480) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.020 | 6/37 (NCI-H1573, LS 180, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.020 | 1/45 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.040 | 6/30 (SHP-77, LS 180, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.048 | 2/41 (HOP62, NCI-H460) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.065 | 4/28 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.075 | 3/22 (HT-29, SW 900, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +2.9 | 0.095 | 2/37 (RKO, NCI-H2030) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11090.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.05 µM in 1 line (HOP62 0.0636×); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.141×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.597×** | -5.7 | 7e-06 | 9/37 (PANC-1, HS-578T, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -4.6 | 0.001 | 17/43 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.731×** | -3.6 | 0.061 | 7/37 (HT-29, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.743×** | -3.4 | 0.089 | 13/45 (SW 900, SW1417, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.751× | -3.3 | 0.11 | 5/40 (NCI-H2347, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Hesperidin (drug)]] 0.05 µM |  | 0.741× | -3.2 | 0.14 | 7/39 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | 0.753× | -3.0 | 0.21 | 6/41 (SW1417, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.60 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.17 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0636× (z -11.4) |
| [[A-172 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.711 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.726 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.752 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.998 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.673 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.987 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P9]] | +0.90 | +0.84 / +0.82 | both halves | 7e-06 |  |
| [[HERC2P2]] | +0.89 | +0.81 / +0.86 | both halves | 7e-06 |  |
| [[HERC2]] | +0.78 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[ZNF496]] | +0.69 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[HSF1]] | +0.67 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | +0.66 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[PLAA]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[UFD1]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ERI3]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[ELAC2]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP23]] | -0.71 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.67 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[FAM200B]] | -0.66 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.64 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[S100A3]] | -0.63 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ZC3H6]] | -0.62 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[TSPAN31]] | -0.62 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[SLC39A1]] | -0.61 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[HHLA3]] | -0.61 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[APLF]] | -0.61 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[H2AJ]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC2]] | B | NFATC2 activity lowers HERC2P3's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.44× higher at baseline in the lines without NFATC2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[H2AJ]] | B | H2AJ activity lowers HERC2P3's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.50× higher at baseline in the lines without H2AJ | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-6.9, -31.1); signed map (-15.9, -51.8). **Vector** length 36.7, 3.34% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.2 | +7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.0 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +5.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.5 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.7 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.7 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.4 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.9 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | HERC2 pseudogene 3 |
| Locus type | pseudogene |
| Location | 15q11.1-q11.2 — chr15:20,431,093-20,505,462 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | D15F37S4, LOC283755 |
| Matched by | ensembl_id |

UniProt [Q9BVR0](https://www.uniprot.org/uniprotkb/Q9BVR0) carries no function annotation.

**Summary**, from NCBI Gene [283755](https://www.ncbi.nlm.nih.gov/gene/283755):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in protein ubiquitination. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4871) · Entrez [283755](https://www.ncbi.nlm.nih.gov/gene/283755) · UniProt [Q9BVR0](https://www.uniprot.org/uniprotkb/Q9BVR0) · Ensembl [ENSG00000180229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180229)

## Data

Gene col 11090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11090); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11090]; `tensor/DDL_lfc|DDL_z.npy` [11090]; `embed/gene_vectors.npy` [11090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11090 or target_col == 11090). Every well: [[HERC2P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC2P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
