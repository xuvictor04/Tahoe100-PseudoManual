---
symbol: "SBK1"
type: "gene"
col: 12005
ensembl_id: "ENSG00000188322"
name: "SH3 domain binding kinase 1"
location: "16p12.1"
module: 115
arm: "+"
pooled_cpm: 6.76
n_lines_expressing: 34
n_dd_up: 21
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 15
direction_downstream: 11
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# SBK1

*SH3 domain binding kinase 1* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.59× (z +17.2, q 0e+00, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.513× (z -7.5, q 3e-11, down in 22 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGSM1]] (+0.68, fdr 1e-05), [[TSPAN33]] (+0.68, fdr 1e-05), [[LINC00937]] (+0.67, fdr 7e-06); moves opposite to [[ZRANB2-DT]] (-0.59, fdr 2e-04), [[USP40]] (-0.59, fdr 1e-04), [[METTL6]] (-0.55, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); 11 go from it, the strongest it → [[ASRGL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.59×** | +17.2 | 0e+00 | 25/31 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.50×** | +17.0 | 0e+00 | 23/31 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.58×** | +15.1 | 0e+00 | 23/30 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.39×** | +13.8 | 4e-41 | 23/31 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.18×** | +13.0 | 8e-37 | 23/31 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +11.0 | 5e-26 | 14/29 (A549, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.52×** | +10.4 | 1e-23 | 12/22 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.51×** | +10.4 | 2e-23 | 19/29 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.09×** | +8.0 | 9e-14 | 6/11 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.90×** | +7.2 | 2e-11 | 21/26 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.78×** | +6.5 | 3e-09 | 19/31 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +6.1 | 4e-08 | 12/29 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.72×** | +5.9 | 2e-07 | 12/22 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.65×** | +5.2 | 7e-06 | 3/13 (SW1417, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +4.2 | 9e-04 | 6/25 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.007 | 5/28 (LoVo, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.034 | 4/30 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.050 | 4/30 (A-427, NCI-H661, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.513×** | -7.5 | 3e-11 | 22/31 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.542×** | -6.9 | 1e-09 | 19/28 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.546×** | -6.8 | 2e-09 | 19/30 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.348×** | -6.2 | 7e-08 | 18/27 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -6.1 | 1e-07 | 20/31 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.600×** | -5.8 | 8e-07 | 17/31 (NCI-H1573, SW1417, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -5.3 | 1e-05 | 18/27 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.719×** | -5.2 | 1e-05 | 21/28 (SW1417, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -4.5 | 4e-04 | 15/31 (A-427, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.540×** | -3.6 | 0.016 | 14/30 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.737×** | -3.4 | 0.030 | 11/31 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.743×** | -3.3 | 0.039 | 10/29 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pentagastrin (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.060 | 3/31 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.765× | -3.0 | 0.10 | 12/30 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.86 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 11.3× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.132× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0512× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 8.82 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0665× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -10.2) |
| [[BT-474 (line)]] | alt | 33.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -12.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -9.5) |
| [[KATO III (line)]] | alt | 9.37 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -10.1) |
| [[LoVo (line)]] | wt | 13.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 10.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -11.9) |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0832× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 7.05 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.125× (z -9.2) |
| [[RKO (line)]] | wt | 9.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -9.5) |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0786× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.889 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGSM1]] | +0.68 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.68 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[SLC29A4]] | +0.65 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[PARD6G]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[ARHGAP44]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MLXIPL]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CIB2]] | +0.63 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[LHX2]] | +0.63 | +0.41 / +0.73 | both halves | 4e-05 |  |
| [[HES2]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD9]] | +0.59 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[KCNQ2]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZRANB2-DT]] | -0.59 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[USP40]] | -0.59 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[METTL6]] | -0.55 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TRMT13]] | -0.54 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[RFX3-DT]] | -0.54 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[PKN2-AS1]] | -0.54 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.53 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[EFCAB6]] | -0.53 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[DPH6-DT]] | -0.52 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[SLC38A4-AS1]] | -0.51 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[MCPH1]] | -0.51 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[SUMF1]] | -0.51 | -0.29 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises SBK1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 3.05× lower at baseline in the lines without TSPAN33 | 0.005 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[UNC5A]] | B | UNC5A activity raises SBK1's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 2.97× lower at baseline in the lines without UNC5A | 0.009 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[LHX2]] | B | LHX2 activity raises SBK1's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 2.21× lower at baseline in the lines without LHX2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[DPYSL5]] | B | DPYSL5 activity raises SBK1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.58× lower at baseline in the lines without DPYSL5 | 0.035 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[CIB2]] | B | CIB2 activity raises SBK1's level | lines that do not express CIB2 (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without CIB2 | 0.067 | ⚠ within organs, on part of the lines; also absent: HID1, ENSG00000266869, FAM169A; maybe low, not absent |
| [[EGFL7]] | B | EGFL7 activity raises SBK1's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 2.29× lower at baseline in the lines without EGFL7 | 0.068 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[RIMS3]] | B | RIMS3 activity raises SBK1's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.16× lower at baseline in the lines without RIMS3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[ADGRB1]] | B | ADGRB1 activity raises SBK1's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.35× lower at baseline in the lines without ADGRB1 | 0.071 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[LMX1B]] | B | LMX1B activity raises SBK1's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without LMX1B | 0.082 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[RET]] | B | RET activity raises SBK1's level | lines that do not express RET (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without RET | 0.093 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[ARHGAP44]] | B | ARHGAP44 activity raises SBK1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.70× lower at baseline in the lines without ARHGAP44 | 0.096 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[HES6]] | B | HES6 activity raises SBK1's level | lines that do not express HES6 (8) vs lines expressing it (42) | 2.44× lower at baseline in the lines without HES6 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASRGL1]] | B | SBK1 activity raises ASRGL1's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.64× lower at baseline in the lines without SBK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[FBXL16]] | B | SBK1 activity raises FBXL16's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without SBK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[CIB2]] | B | SBK1 activity raises CIB2's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without SBK1 | 0.029 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[TMEM63C]] | B | SBK1 activity raises TMEM63C's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without SBK1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[MNX1]] | B | SBK1 activity raises MNX1's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without SBK1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[DMBX1]] | B | SBK1 activity raises DMBX1's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without SBK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[STRBP]] | B | SBK1 activity raises STRBP's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without SBK1 | 0.077 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[TSPAN33]] | B | SBK1 activity raises TSPAN33's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without SBK1 | 0.083 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[RBM38]] | B | SBK1 activity raises RBM38's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without SBK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[KCNQ2]] | C | SBK1 activity raises KCNQ2's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without SBK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3; co-absent with the target |
| [[MYT1]] | C | SBK1 activity raises MYT1's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without SBK1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.8, 37.7); signed map (-21.3, 31.7). **Vector** length 59.4, 11.9% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +15.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.9 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.7 | +10.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.1 | +6.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | +0.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:28,259,246-28,323,849 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sbk |
| Gene groups (HGNC) | SH3 domain binding kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q52WX2](https://www.uniprot.org/uniprotkb/Q52WX2) (Serine/threonine-protein kinase SBK1):

> May be involved in signal-transduction pathways related to the control of brain development.

**Summary**, from NCBI Gene [388228](https://www.ncbi.nlm.nih.gov/gene/388228):

> Predicted to enable protein serine/threonine kinase activity. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17699) · Entrez [388228](https://www.ncbi.nlm.nih.gov/gene/388228) · UniProt [Q52WX2](https://www.uniprot.org/uniprotkb/Q52WX2) · Ensembl [ENSG00000188322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188322)

## Data

Gene col 12005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12005); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12005]; `tensor/DDL_lfc|DDL_z.npy` [12005]; `embed/gene_vectors.npy` [12005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12005 or target_col == 12005). Every well: [[SBK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
