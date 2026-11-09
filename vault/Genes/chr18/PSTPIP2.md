---
symbol: "PSTPIP2"
type: "gene"
col: 7605
ensembl_id: "ENSG00000152229"
name: "proline-serine-threonine phosphatase interacting protein 2"
location: "18q21.1"
module: 62
arm: "+"
pooled_cpm: 21.29
n_lines_expressing: 30
n_dd_up: 35
n_dd_down: 13
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# PSTPIP2

*proline-serine-threonine phosphatase interacting protein 2* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +18.3, q 0e+00, up in 15 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.614× (z -8.1, q 3e-13, down in 19 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCA12]] (+0.65, fdr 7e-06), [[SPATA18]] (+0.60, fdr 1e-05), [[C1QTNF1-AS1]] (+0.59, fdr 1e-05); moves opposite to [[ASPH]] (-0.55, fdr 1e-05), [[PLP2]] (-0.47, fdr 5e-05), [[TBC1D24]] (-0.46, fdr 5e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[GRAMD2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +18.3 | 0e+00 | 15/28 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +8.7 | 8e-16 | 15/28 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +8.4 | 6e-15 | 6/19 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.51×** | +8.0 | 2e-13 | 18/28 (BT-474, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.9 | 3e-13 | 7/26 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.8 | 8e-13 | 11/28 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +7.7 | 1e-12 | 14/25 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.39×** | +7.7 | 1e-12 | 16/28 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +7.0 | 2e-10 | 17/28 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +6.9 | 3e-10 | 12/28 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.30×** | +6.2 | 3e-08 | 11/28 (LS 180, LoVo, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +5.4 | 3e-06 | 13/28 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 9e-06 | 9/27 (HEC-1-A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.24×** | +5.0 | 2e-05 | 11/28 (A498, SW 900, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 4e-05 | 9/27 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 10/28 (SW480, CFPAC-1, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.008 | 10/27 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.009 | 2/28 (HEC-1-A, A-172) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -8.1 | 3e-13 | 19/28 (LoVo, LS 180, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.631×** | -7.7 | 5e-12 | 17/28 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -7.4 | 3e-11 | 18/28 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.646×** | -7.3 | 5e-11 | 18/27 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.676×** | -6.5 | 8e-09 | 16/28 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.688×** | -6.2 | 5e-08 | 18/28 (COLO 205, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.762×** | -4.5 | 5e-04 | 15/28 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.759×** | -4.4 | 7e-04 | 13/25 (LS 180, Hs 766T, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.816×** | -3.4 | 0.041 | 13/28 (Hs 766T, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.816×** | -3.4 | 0.041 | 9/28 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.824×** | -3.2 | 0.064 | 10/28 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.830×** | -3.1 | 0.090 | 7/27 (SW480, A-172, …) | rises with dose | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.702×** | -3.1 | 0.090 | 9/27 (Hs 766T, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 107 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.299× (z -12.6) |
| [[LoVo (line)]] | wt | 91.6 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -20.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.206× (z -17.6) |
| [[Hs 766T (line)]] | wt | 132 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -16.9) |
| [[SW480 (line)]] | alt | 26.6 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.341× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 36.0 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.3) | [[Auranofin (drug)]] 5 µM 0.305× (z -10.4) |
| [[BT-474 (line)]] | alt | 61.3 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 48.4× (z +13.5) | — |
| [[J82 (line)]] | alt | 12.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 8.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 7.34 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 6.40× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.114× (z -11.1) |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0788× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 7.19 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0465× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.255× (z -11.6) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA12]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[C1QTNF1-AS1]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PINCR]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[ZMAT3]] | +0.57 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SHROOM3]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MDM2]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ANO9]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[DRAM1]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[GRAMD2B]] | +0.54 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[EBI3]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ANKRA2]] | +0.54 | +0.54 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASPH]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[PLP2]] | -0.47 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[TBC1D24]] | -0.46 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[MAP1B]] | -0.46 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[NUMBL]] | -0.45 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[UBR4]] | -0.44 | -0.38 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PSTPIP2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CAVIN2]] | B | CAVIN2 activity raises PSTPIP2's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 1.75× lower at baseline in the lines without CAVIN2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9 |
| [[NOD2]] | B | NOD2 activity raises PSTPIP2's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without NOD2 | 0.067 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[CASP10]] | C | CASP10 activity raises PSTPIP2's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.55× lower at baseline in the lines without CASP10 | 0.019 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRAMD2B]] | B | PSTPIP2 activity raises GRAMD2B's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 2.96× lower at baseline in the lines without PSTPIP2 | 0.028 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[MR1]] | B | PSTPIP2 activity raises MR1's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.51× lower at baseline in the lines without PSTPIP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[STAP2]] | B | PSTPIP2 activity raises STAP2's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without PSTPIP2 | 0.036 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[BATF]] | B | PSTPIP2 activity raises BATF's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without PSTPIP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[SULT1C2]] | B | PSTPIP2 activity raises SULT1C2's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without PSTPIP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[CAVIN2]] | B | PSTPIP2 activity raises CAVIN2's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without PSTPIP2 | 0.059 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[LINC00265]] | B | PSTPIP2 activity lowers LINC00265's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.43× higher at baseline in the lines without PSTPIP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[IKBKE]] | B | PSTPIP2 activity raises IKBKE's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without PSTPIP2 | 0.075 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[ABCA5]] | B | PSTPIP2 activity strengthens ABCA5's drug response | lines that do not express PSTPIP2 (18) vs lines expressing it (27) | the lines without PSTPIP2 respond 0.84× as strongly (z diff +0.85); strongest at Dinaciclib 5 µM: 0.59x vs 0.33x (z diff +4.1) | 0.080 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1; target measured in part of the lines; artifact flags |
| [[CASP10]] | C | PSTPIP2 activity raises CASP10's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 2.67× lower at baseline in the lines without PSTPIP2 | 0.009 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.6, 38.6); signed map (42.0, -21.7). **Vector** length 84.5, 21.3% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +18.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +7.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.9 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -8.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.7 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | proline-serine-threonine phosphatase interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:45,983,536-46,072,272 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | F-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H939](https://www.uniprot.org/uniprotkb/Q9H939) (Proline-serine-threonine phosphatase-interacting protein 2):

> Binds to F-actin. May be involved in regulation of the actin cytoskeleton (By similarity).

**Summary**, from NCBI Gene [9050](https://www.ncbi.nlm.nih.gov/gene/9050):

> Predicted to be located in cytoskeleton; cytosol; and membrane. Predicted to be active in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9581) · Entrez [9050](https://www.ncbi.nlm.nih.gov/gene/9050) · UniProt [Q9H939](https://www.uniprot.org/uniprotkb/Q9H939) · Ensembl [ENSG00000152229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152229)

## Data

Gene col 7605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7605); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7605]; `tensor/DDL_lfc|DDL_z.npy` [7605]; `embed/gene_vectors.npy` [7605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7605 or target_col == 7605). Every well: [[PSTPIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSTPIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
