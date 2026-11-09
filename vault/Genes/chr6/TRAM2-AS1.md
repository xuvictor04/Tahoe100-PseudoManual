---
symbol: "TRAM2-AS1"
type: "gene"
col: 13486
ensembl_id: "ENSG00000225791"
name: "TRAM2 antisense RNA 1"
location: "6p12.2"
module: 10
arm: "+"
pooled_cpm: 5.28
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TRAM2-AS1

*TRAM2 antisense RNA 1* — 6p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +14.9, q 0e+00, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.555× (z -6.9, q 4e-09, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[F8]] (+0.77, fdr 2e-05), [[WAC-AS1]] (+0.73, fdr 2e-05), [[KRBA2]] (+0.72, fdr 3e-05); moves opposite to [[NPHP4]] (-0.63, fdr 2e-05), [[LPCAT1]] (-0.62, fdr 2e-04), [[RNF216]] (-0.61, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[C7orf31]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +14.9 | 0e+00 | 33/42 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +14.5 | 7e-45 | 21/22 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +13.4 | 8e-39 | 10/10 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.04×** | +12.4 | 2e-33 | 29/46 (A498, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.83×** | +11.9 | 2e-30 | 14/14 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +8.0 | 1e-13 | 22/41 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.3 | 3e-08 | 18/48 (HS-578T, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.0 | 2e-07 | 15/39 (C32, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +5.5 | 3e-06 | 14/46 (C32, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.9 | 7e-05 | 8/27 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.4 | 5e-04 | 1/12 (A-172) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.41×** | +4.2 | 0.001 | 12/44 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.002 | 13/45 (HOP62, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.008 | 4/40 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.024 | 8/44 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.041 | 7/45 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.073 | 2/47 (HepG2/C3A, C32) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.073 | 4/47 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.099 | 6/46 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.099 | 6/38 (A-172, C32, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.555×** | -6.9 | 4e-09 | 23/43 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -5.6 | 6e-06 | 18/46 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.644×** | -5.4 | 1e-05 | 22/47 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.650×** | -5.3 | 2e-05 | 18/46 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.678×** | -4.8 | 2e-04 | 17/46 (NCI-H2030, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.680×** | -4.7 | 2e-04 | 17/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.706×** | -4.3 | 0.001 | 12/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -3.8 | 0.010 | 12/46 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Fusidic acid (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.026 | 10/47 (SHP-77, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -3.5 | 0.029 | 9/44 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.593×** | -3.4 | 0.039 | 8/38 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.604×** | -3.2 | 0.055 | 8/21 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 0.784× | -3.0 | 0.12 | 12/47 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +10.1) | — |
| [[A549 (line)]] | wt | 4.29 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0802× (z -8.8) |
| [[COLO 205 (line)]] | alt | 7.53 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0737× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 7.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 2.86 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0638× (z -11.4) |
| [[PANC-1 (line)]] | alt | 7.75 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.254× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 8.00 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0787× (z -10.9) |
| [[A-172 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F8]] | +0.77 | +0.83 / +0.46 | both halves | 2e-05 |  |
| [[WAC-AS1]] | +0.73 | +0.73 / +0.47 | both halves | 2e-05 | same gene group |
| [[KRBA2]] | +0.72 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[TIGD6]] | +0.72 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[DDX19A-DT]] | +0.72 | +0.77 / +0.49 | both halves | 1e-05 |  |
| [[LRRC37A3]] | +0.72 | +0.78 / +0.32 | both halves | 2e-04 |  |
| [[RWDD2B]] | +0.72 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[SMIM19]] | +0.71 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[FNBP1P1]] | +0.71 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.71 | +0.78 / +0.31 | both halves | 2e-04 |  |
| [[CLN5]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[PGBD4]] | +0.70 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.63 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[LPCAT1]] | -0.62 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[RNF216]] | -0.61 | -0.67 / -0.29 | both halves | 2e-04 |  |
| [[CENPX]] | -0.60 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[TOMM5]] | -0.60 | -0.65 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C7orf31]] | B | C7orf31 activity raises TRAM2-AS1's level | lines that do not express C7orf31 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without C7orf31 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC00888, TMEM145, TBKBP1; maybe low, not absent |
| [[GDAP1]] | B | GDAP1 activity raises TRAM2-AS1's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without GDAP1 | 0.048 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[HECTD2]] | B | HECTD2 activity raises TRAM2-AS1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.59× lower at baseline in the lines without HECTD2 | 0.050 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises TRAM2-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HHAT]] | C | HHAT activity raises TRAM2-AS1's level | lines that do not express HHAT (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without HHAT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01341, C2orf92, GDAP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.8, 13.7); signed map (22.2, -14.8). **Vector** length 62.5, 8.88% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.9 | +12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +13.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -6.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | TRAM2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p12.2 — chr6:52,576,787-52,643,058 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48663) · Entrez [401264](https://www.ncbi.nlm.nih.gov/gene/401264) · Ensembl [ENSG00000225791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225791)

## Data

Gene col 13486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13486); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13486]; `tensor/DDL_lfc|DDL_z.npy` [13486]; `embed/gene_vectors.npy` [13486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13486 or target_col == 13486). Every well: [[TRAM2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAM2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
