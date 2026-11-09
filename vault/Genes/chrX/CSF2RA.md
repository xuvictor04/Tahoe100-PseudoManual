---
symbol: "CSF2RA"
type: "gene"
col: 12557
ensembl_id: "ENSG00000198223"
name: "colony stimulating factor 2 receptor subunit alpha"
location: "Xp22.32 and Yp11.3"
module: 34
arm: "+"
pooled_cpm: 11.46
n_lines_expressing: 22
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CSF2RA

*colony stimulating factor 2 receptor subunit alpha* — Xp22.32 and Yp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.98× (z +15.3, q 0e+00, up in 8 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.36× (z +13.4, q 9e-39, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Diphenhydramine (drug)]] 0.05 µM: 0.644× (z -4.5, q 0.004, down in 2 of 19 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCTP1]] (+0.56, fdr 5e-05), [[TMEM154]] (+0.55, fdr 3e-05), [[GTF2IP7]] (+0.54, fdr 6e-05); moves opposite to [[ZHX1]] (-0.45, fdr 2e-04), [[RNF170]] (-0.44, fdr 1e-04), [[TCEANC2]] (-0.40, fdr 3e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINP1]] → it (grade C ⚠); 9 go from it, the strongest it → [[ESYT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.98×** | +15.3 | 0e+00 | 8/17 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +15.0 | 0e+00 | 5/12 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +13.4 | 9e-39 | 16/19 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +11.2 | 4e-27 | 5/14 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +10.6 | 5e-24 | 4/19 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +6.7 | 2e-09 | 8/19 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +6.1 | 7e-08 | 13/19 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.9 | 6e-05 | 5/19 (HEC-1-A, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 1e-04 | 8/19 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.1 | 0.002 | 3/17 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.043 | 4/18 (NCI-H2030, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.3 | 0.050 | 3/16 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.069 | 4/18 (HEC-1-A, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.1 | 0.069 | 9/19 (SNU-423, NCI-H23, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.069 | 6/19 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.069 | 7/19 (LS 180, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12557.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.644×** | -4.5 | 0.004 | 2/19 (KATO III, Panc 03.27) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.669×** | -4.3 | 0.006 | 9/18 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.696×** | -4.0 | 0.012 | 5/19 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.692×** | -3.8 | 0.024 | 1/19 (NCI-H2347) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.704×** | -3.6 | 0.038 | 6/19 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -3.5 | 0.042 | 14/18 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.731×** | -3.5 | 0.042 | 7/19 (SNU-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.742×** | -3.3 | 0.067 | 7/19 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.746× | -3.1 | 0.14 | 1/19 (SW1417) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.3 | 1 | 18 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.28× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -19.0) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.151× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 70.0 | 0 | 9 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0341× (z -24.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.116× (z -14.3) |
| [[SNU-1 (line)]] | wt | 68.3 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -18.8) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.275× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 31.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.3) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -10.6) |
| [[LS 180 (line)]] | wt | 41.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -12.5) ⚠ cell-cycle shift, explains ~7% of this change |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0490× (z -14.3) ⚠ toxic |
| [[A549 (line)]] | wt | 12.2 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0796× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.5) ⚠ cell-cycle shift, explains ~7% of this change |
| [[J82 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 8.45 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.26× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 8.31 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 15.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.06× (z +8.5) | — |
| [[A-172 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTP1]] | +0.56 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[TMEM154]] | +0.55 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[GTF2IP7]] | +0.54 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[UNC5D]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ANKRD29]] | +0.51 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[CCDC68]] | +0.51 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[SERPIND1]] | +0.51 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PLAC4]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[LINC02320]] | +0.50 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[LCP1]] | +0.49 | +0.39 / +0.49 | both halves | 6e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[IL18R1]] | +0.49 | +0.43 / +0.56 | both halves | 3e-05 | same gene group; pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING |
| [[UNC13A]] | +0.49 | +0.35 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZHX1]] | -0.45 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[RNF170]] | -0.44 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[TCEANC2]] | -0.40 | -0.36 / -0.26 | both halves | 3e-04 |  |
| [[WNK1]] | -0.40 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[UBR5]] | -0.39 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[NR0B1]] | -0.39 | -0.44 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINP1]] | C | LINP1 activity raises CSF2RA's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.94× lower at baseline in the lines without LINP1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESYT3]] | B | CSF2RA activity raises ESYT3's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 1.60× lower at baseline in the lines without CSF2RA | 0.034 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A |
| [[COL4A4]] | B | CSF2RA activity raises COL4A4's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without CSF2RA | 0.085 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A |
| [[PRICKLE1]] | B | CSF2RA activity raises PRICKLE1's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without CSF2RA | 0.091 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A |
| [[SH2D3A]] | C | CSF2RA activity raises SH2D3A's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without CSF2RA | 0.042 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A; co-absent with the target |
| [[LINP1]] | C | CSF2RA activity raises LINP1's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without CSF2RA | 0.062 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A; co-absent with the target |
| [[XDH]] | C | CSF2RA activity raises XDH's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without CSF2RA | 0.081 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A; co-absent with the target |
| [[LINC02742]] | C | CSF2RA activity raises LINC02742's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without CSF2RA | 0.082 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A; co-absent with the target |
| [[LAMC2]] | C | CSF2RA activity raises LAMC2's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 2.93× lower at baseline in the lines without CSF2RA | 0.094 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A; co-absent with the target |
| [[COL4A3]] | C | CSF2RA activity raises COL4A3's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without CSF2RA | 0.098 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.414). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.2, 15.4); signed map (17.2, 55.7). **Vector** length 56.7, 14.2% of its response variance represented; |z| ≥ 3 in 521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +11.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +1.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | colony stimulating factor 2 receptor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.32 and Yp11.3 — chrX:1,268,800-1,310,381 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD116, alphaGMR; previously CSF2R |
| Gene groups (HGNC) | CD molecules; Pseudoautosomal region 1 |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, KRAS_SIGNALING_UP |
| Reactome | 11 pathways, smallest: Diseases associated with surfactant metabolism; Surfactant metabolism; Interleukin receptor SHC signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P15509](https://www.uniprot.org/uniprotkb/P15509) (Granulocyte-macrophage colony-stimulating factor receptor subunit alpha):

> Low affinity receptor for granulocyte-macrophage colony-stimulating factor. Transduces a signal that results in the proliferation, differentiation, and functional activation of hematopoietic cells.

**Summary**, from NCBI Gene [1438](https://www.ncbi.nlm.nih.gov/gene/1438):

> The protein encoded by this gene is the alpha subunit of the heterodimeric receptor for colony stimulating factor 2, a cytokine which controls the production, differentiation, and function of granulocytes and macrophages. The encoded protein is a member of the cytokine family of receptors. This gene is found in the pseudoautosomal region (PAR) of the X and Y chromosomes. Multiple transcript variants encoding different isoforms have been found for this gene, with some of the isoforms being …

**Accessions** — [HGNC:2435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2435) · Entrez [1438](https://www.ncbi.nlm.nih.gov/gene/1438) · UniProt [P15509](https://www.uniprot.org/uniprotkb/P15509) · Ensembl [ENSG00000198223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198223)

## Data

Gene col 12557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12557); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12557]; `tensor/DDL_lfc|DDL_z.npy` [12557]; `embed/gene_vectors.npy` [12557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12557 or target_col == 12557). Every well: [[CSF2RA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSF2RA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
