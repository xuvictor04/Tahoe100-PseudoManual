---
symbol: "VASH2"
type: "gene"
col: 6756
ensembl_id: "ENSG00000143494"
name: "vasohibin 2"
location: "1q32.3"
module: 115
arm: "+"
pooled_cpm: 2.78
n_lines_expressing: 41
n_dd_up: 36
n_dd_down: 11
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# VASH2

*vasohibin 2* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.68× (z +21.2, q 0e+00, up in 34 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.399× (z -9.6, q 4e-19, down in 24 of 36 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AIF1L]] (+0.63, fdr 1e-05), [[FGFR4]] (+0.60, fdr 1e-05), [[CAMK2G]] (+0.58, fdr 4e-05); moves opposite to [[DNAI4]] (-0.59, fdr 7e-05), [[BDNF-AS]] (-0.56, fdr 3e-04), [[BCDIN3D]] (-0.56, fdr 7e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNMT3B]] → it (grade C ⚠); 3 go from it, the strongest it → [[RNF146]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.68×** | +21.2 | 0e+00 | 34/35 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.92×** | +20.2 | 0e+00 | 33/36 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.83×** | +18.4 | 0e+00 | 33/35 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +14.7 | 0e+00 | 23/28 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.98×** | +14.4 | 8e-45 | 32/36 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.54×** | +13.7 | 7e-41 | 26/36 (PANC-1, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.06×** | +11.1 | 1e-26 | 0/3 | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.53×** | +9.7 | 3e-20 | 17/27 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +9.5 | 1e-19 | 11/26 (J82, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.32×** | +8.8 | 1e-16 | 19/34 (NCI-H460, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **4.92×** | +8.7 | 2e-16 | 19/30 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.20×** | +7.8 | 4e-13 | 14/32 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.15×** | +7.4 | 8e-12 | 0/5 | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +6.7 | 6e-10 | 15/30 (SNU-423, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.88×** | +6.6 | 2e-09 | 14/35 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.49×** | +5.8 | 2e-07 | 11/34 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +4.7 | 7e-05 | 10/36 (A-172, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 5e-04 | 11/35 (A498, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.72×** | +4.0 | 0.002 | 4/34 (A498, RKO, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.399×** | -9.6 | 4e-19 | 24/36 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.454×** | -8.3 | 4e-14 | 17/31 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -7.4 | 3e-11 | 16/24 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.510×** | -7.1 | 2e-10 | 18/35 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.607×** | -5.2 | 2e-05 | 13/33 (AN3 CA, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -4.9 | 1e-04 | 16/35 (RKO, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.647×** | -4.6 | 4e-04 | 11/24 (A549, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.697×** | -3.8 | 0.011 | 11/36 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.790×** | -3.5 | 0.028 | 3/36 (CHP-212, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.041 | 5/36 (HCT15, A549, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.727×** | -3.3 | 0.042 | 10/35 (SW480, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.76 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 4 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0754× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 4.34 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 7.00× (z +8.6) | [[Harringtonine (drug)]] 0.05 µM 0.0594× (z -11.7) |
| [[PANC-1 (line)]] | alt | 2.42 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 15.7× (z +9.2) | — |
| [[LoVo (line)]] | wt | 3.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +8.7) | — |
| [[SW480 (line)]] | alt | 4.79 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -9.1) |
| [[A-172 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.993 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.993 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.456 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIF1L]] | +0.63 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[FGFR4]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.58 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[ZNF483]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ARHGAP44]] | +0.57 | +0.37 / +0.58 | both halves | 9e-05 |  |
| [[PCSK9]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[GSTM4]] | +0.56 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[SEMA4D]] | +0.55 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[CHRNA5]] | +0.55 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[PRR5]] | +0.55 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[TMEM97]] | +0.55 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[LHX6]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI4]] | -0.59 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[BDNF-AS]] | -0.56 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[BCDIN3D]] | -0.56 | -0.20 / -0.46 | both halves | 7e-04 |  |
| [[HEXIM2-AS1]] | -0.56 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ANKRD17-DT]] | -0.55 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[RC3H2]] | -0.54 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[ENTPD3-AS1]] | -0.54 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[RAB30-DT]] | -0.52 | -0.17 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[METTL6]] | -0.51 | -0.20 / -0.49 | both halves | 7e-04 |  |
| [[ITCH]] | -0.51 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[PHF20L1]] | -0.50 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[FBXW4]] | -0.50 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[RNF146]] | -0.49 | -0.24 / -0.45 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNMT3B]] | C | DNMT3B activity raises VASH2's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without DNMT3B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF146]] | B | VASH2 activity raises RNF146's level | lines that do not express VASH2 (9) vs lines expressing it (41) | 1.63× lower at baseline in the lines without VASH2 | 0.077 | ⚠ within organs, on part of the lines; also absent: WNT9A, STOX1, ZNF254; maybe low, not absent |
| [[CCAR1]] | B | VASH2 activity raises CCAR1's level | lines that do not express VASH2 (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without VASH2 | 0.091 | ⚠ within organs, on part of the lines; also absent: WNT9A, STOX1, ZNF254; maybe low, not absent |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | VASH2's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | VASH2's natural level across 39 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.511 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.5, 43.7); signed map (-24.0, 37.7). **Vector** length 52.2, 7.98% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +13.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.9 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +4.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +4.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +8.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.2 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | vasohibin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,950,520-212,992,037 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12505 |
| Gene groups (HGNC) | Vasohibin family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V25](https://www.uniprot.org/uniprotkb/Q86V25) (Tubulinyl-Tyr carboxypeptidase 2):

> Tyrosine carboxypeptidase that removes the C-terminal tyrosine residue of alpha-tubulin, thereby regulating microtubule dynamics and function. Critical for spindle function and accurate chromosome segregation during mitosis since microtubule detyrosination regulates mitotic spindle length and postioning. Acts as an activator of angiogenesis: expressed in infiltrating mononuclear cells in the sprouting front to promote angiogenesis. Plays a role in axon formation.

**Summary**, from NCBI Gene [79805](https://www.ncbi.nlm.nih.gov/gene/79805):

> Enables actin binding activity; metallocarboxypeptidase activity; and microtubule binding activity. Involved in axon development and proteolysis. Acts upstream of or within cell-cell fusion; positive regulation of angiogenesis; and positive regulation of endothelial cell proliferation. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25723) · Entrez [79805](https://www.ncbi.nlm.nih.gov/gene/79805) · UniProt [Q86V25](https://www.uniprot.org/uniprotkb/Q86V25) · Ensembl [ENSG00000143494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143494)

## Data

Gene col 6756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6756); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6756]; `tensor/DDL_lfc|DDL_z.npy` [6756]; `embed/gene_vectors.npy` [6756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6756 or target_col == 6756). Every well: [[VASH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VASH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
