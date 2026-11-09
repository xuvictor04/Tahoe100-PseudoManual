---
symbol: "TRIM35"
type: "gene"
col: 2430
ensembl_id: "ENSG00000104228"
name: "tripartite motif containing 35"
location: "8p21.2"
module: 77
arm: "+"
pooled_cpm: 8.23
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TRIM35

*tripartite motif containing 35* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.80× (z +20.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.508× (z -8.8, q 7e-16, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.187×; ⚠ cell-cycle shift, explains ~24% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HOP62 0.0536×); [[Ferulic acid (drug)]] 5 µM in 1 line (AsPC-1 0.0590×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (AsPC-1 0.0840×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF5L]] (+0.70, fdr 3e-05), [[HMOX2]] (+0.69, fdr 7e-06), [[MTMR12]] (+0.67, fdr 3e-05); moves opposite to [[BAZ2B]] (-0.66, fdr 5e-05), [[AKT1S1]] (-0.63, fdr 4e-05), [[LSMEM1]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PTPRU]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MFHAS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.80×** | +20.4 | 0e+00 | 46/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.21×** | +18.7 | 0e+00 | 47/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.58×** | +17.5 | 0e+00 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.65×** | +12.7 | 9e-35 | 41/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +9.0 | 3e-17 | 21/34 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.13×** | +8.7 | 3e-16 | 31/43 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +7.0 | 3e-10 | 23/46 (LS 180, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.6 | 1e-06 | 19/46 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +5.3 | 7e-06 | 19/47 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.14×** | +5.2 | 1e-05 | 16/43 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +4.7 | 2e-04 | 9/47 (A549, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +4.2 | 0.001 | 11/46 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 11/46 (A-427, NCI-H460, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 9/46 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.37×** | +3.9 | 0.004 | 6/45 (SHP-77, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.008 | 8/48 (SW48, J82, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.019 | 4/38 (MIA PaCa-2, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2430.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.187×; ⚠ cell-cycle shift, explains ~24% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HOP62 0.0536×); [[Ferulic acid (drug)]] 5 µM in 1 line (AsPC-1 0.0590×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (AsPC-1 0.0840×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.508×** | -8.8 | 7e-16 | 26/47 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.723×** | -6.0 | 6e-07 | 21/43 (HS-578T, SK-MEL-2, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.740×** | -3.9 | 0.016 | 10/32 (HOP62, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 0.768× | -3.3 | 0.13 | 10/45 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.759× | -3.2 | 0.17 | 11/46 (SW 900, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.37× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 6.71 | 0 | 2 | — | [[Ferulic acid (drug)]] 5 µM 0.0590× (z -10.2) |
| [[LoVo (line)]] | wt | 8.42 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 5.84 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.52× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[HOP62 (line)]] | alt | 4.84 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0536× (z -11.9) |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | +0.70 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[HMOX2]] | +0.69 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MTMR12]] | +0.67 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[TMEM120B]] | +0.64 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[NUDCD3]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SNU13]] | +0.64 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[MMS19]] | +0.63 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[BRAT1]] | +0.63 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[IMPDH1]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[WRAP73]] | +0.62 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[ANKRD27]] | +0.62 | +0.54 / +0.37 | both halves | 9e-05 |  |
| [[FAM24B]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.66 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[AKT1S1]] | -0.63 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[LSMEM1]] | -0.63 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[KANSL1L]] | -0.62 | -0.62 / -0.27 | both halves | 3e-04 |  |
| [[CCDC90B-AS1]] | -0.62 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[DCAF8]] | -0.61 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[KMT2E-AS1]] | -0.61 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CHD3]] | -0.61 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[FBXL19-AS1]] | -0.60 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | -0.60 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[TIA1]] | -0.60 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[NQO1-DT]] | -0.60 | -0.44 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRU]] | B | PTPRU activity raises TRIM35's level | lines that do not express PTPRU (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without PTPRU | 0.088 | ⚠ within organs, on part of the lines; also absent: FBXO16, RNF144A |
| [[ABCA3]] | B | ABCA3 activity raises TRIM35's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without ABCA3 | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFHAS1]] | C | TRIM35's natural level strengthens MFHAS1's drug response | TRIM35's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.07; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.9, 0.1); signed map (-43.4, -3.5). **Vector** length 87.8, 17.9% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.8 | +18.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +17.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -6.3 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.1 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:27,284,886-27,311,272 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1098, MAIR, HLS5 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPQ4](https://www.uniprot.org/uniprotkb/Q9UPQ4) (E3 ubiquitin-protein ligase TRIM35):

> E3 ubiquitin-protein ligase that participates in multiple biological processes including cell death, glucose metabolism, and in particular, the innate immune response. Mediates 'Lys-63'-linked polyubiquitination of TRAF3 thereby promoting type I interferon production via RIG-I signaling pathway. Can also catalyze 'Lys-48'-linked polyubiquitination and proteasomal degradation of viral proteins such as influenza virus PB2. Acts as a negative feedback regulator of TLR7- and TLR9-triggered …

**Summary**, from NCBI Gene [23087](https://www.ncbi.nlm.nih.gov/gene/23087):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The function of this protein has not been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16285) · Entrez [23087](https://www.ncbi.nlm.nih.gov/gene/23087) · UniProt [Q9UPQ4](https://www.uniprot.org/uniprotkb/Q9UPQ4) · Ensembl [ENSG00000104228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104228)

## Data

Gene col 2430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2430); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2430]; `tensor/DDL_lfc|DDL_z.npy` [2430]; `embed/gene_vectors.npy` [2430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2430 or target_col == 2430). Every well: [[TRIM35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
