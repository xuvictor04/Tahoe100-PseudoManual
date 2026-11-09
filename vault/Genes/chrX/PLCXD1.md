---
symbol: "PLCXD1"
type: "gene"
col: 11281
ensembl_id: "ENSG00000182378"
name: "phosphatidylinositol specific phospholipase C X domain containing 1"
location: "Xp22.33 and Yp11.32"
module: 136
arm: "+"
pooled_cpm: 19.49
n_lines_expressing: 39
n_dd_up: 0
n_dd_down: 37
n_dd_up_clean: 0
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# PLCXD1

*phosphatidylinositol specific phospholipase C X domain containing 1* — Xp22.33 and Yp11.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 5.92×).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.392× (z -15.6, q 0e+00, down in 34 of 36 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAQR5]] (+0.54, fdr 1e-05), [[ATG16L1]] (+0.52, fdr 3e-05), [[PYGL]] (+0.52, fdr 6e-05); moves opposite to [[SAMD12-AS1]] (-0.46, fdr 4e-05), [[RARRES1]] (-0.46, fdr 2e-04), [[IFT57]] (-0.45, fdr 2e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[GNAI2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11281.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 5.92×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | 1.73× | +3.4 | 0.37 | 10/35 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.392×** | -15.6 | 0e+00 | 34/36 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -10.1 | 1e-21 | 23/34 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.437×** | -9.4 | 9e-19 | 28/35 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.472×** | -8.5 | 2e-15 | 24/34 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.481×** | -8.3 | 9e-15 | 27/36 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.581×** | -6.4 | 1e-08 | 19/36 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.586×** | -6.1 | 1e-07 | 23/33 (NCI-H23, A549, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.590×** | -6.0 | 1e-07 | 20/35 (CHP-212, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -5.9 | 3e-07 | 20/35 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.610×** | -5.8 | 3e-07 | 20/37 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.621×** | -5.6 | 9e-07 | 23/35 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -5.1 | 1e-05 | 9/20 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.694×** | -5.0 | 2e-05 | 14/36 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -4.6 | 1e-04 | 19/33 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.667×** | -4.6 | 1e-04 | 14/35 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.759×** | -4.6 | 1e-04 | 18/37 (PANC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -4.5 | 3e-04 | 16/37 (A549, HepG2/C3A, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.753×** | -4.3 | 5e-04 | 17/36 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 62.4 | 0 | 24 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0997× (z -20.1) |
| [[A549 (line)]] | wt | 90.4 | 0 | 14 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0895× (z -20.6) |
| [[C32 (line)]] | wt | 28.8 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0989× (z -16.4) |
| [[PANC-1 (line)]] | alt | 47.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -23.8) |
| [[A-172 (line)]] | wt | 19.0 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 54.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.0) |
| [[SHP-77 (line)]] | alt | 32.0 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 52.3 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.510× (z -13.0) ⚠ position not correctable · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 41.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -13.9) |
| [[RKO (line)]] | wt | 41.7 | 0 | 2 | — | [[Binimetinib (drug)]] 5 µM 0.193× (z -9.3) |
| [[A-427 (line)]] | wt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.4) |
| [[A498 (line)]] | wt | 6.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -8.6) |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -10.3) |
| [[CHP-212 (line)]] | wt | 76.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.6) |
| [[Hs 766T (line)]] | wt | 6.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -9.3) |
| [[HT-29 (line)]] | alt | 22.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0634× (z -9.6) |
| [[NCI-H661 (line)]] | alt | 87.9 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.151× (z -8.5) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -10.5) |
| [[SW480 (line)]] | alt | 10.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.92× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR5]] | +0.54 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ATG16L1]] | +0.52 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PYGL]] | +0.52 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[FLNB]] | +0.52 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[PLEKHG5]] | +0.50 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[BMP6]] | +0.49 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[FLNB-AS1]] | +0.49 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[HK1]] | +0.49 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[CACNA1H]] | +0.49 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[ATP11A]] | +0.49 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[FBXL16]] | +0.48 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[CSNK1E]] | +0.48 | +0.58 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD12-AS1]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RARRES1]] | -0.46 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[IFT57]] | -0.45 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[WDFY3]] | -0.45 | -0.29 / -0.25 | both halves | 4e-04 |  |
| [[RNF146]] | -0.44 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[PSMB10]] | -0.44 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[GALNT7]] | -0.43 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[PHC3]] | -0.43 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[MTUS1-DT]] | -0.43 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[RBPMS]] | -0.42 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[TNS3]] | -0.42 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[BTC]] | -0.42 | -0.41 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PLCXD1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises PLCXD1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.4% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[DPYSL2]] | B | DPYSL2 activity lowers PLCXD1's level | lines that do not express DPYSL2 (5) vs lines expressing it (45) | 2.07× higher at baseline in the lines without DPYSL2 | 0.048 | ⚠ within organs, on part of the lines; also absent: PHLDA1, PARP3; maybe low, not absent |
| [[CACNA1H]] | B | CACNA1H activity raises PLCXD1's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 1.66× lower at baseline in the lines without CACNA1H | 0.066 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3 |
| [[ADGRB1]] | B | ADGRB1 activity raises PLCXD1's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.02× lower at baseline in the lines without ADGRB1 | 0.088 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAI2]] | B | PLCXD1 activity lowers GNAI2's level | lines that do not express PLCXD1 (11) vs lines expressing it (39) | 1.59× higher at baseline in the lines without PLCXD1 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GLDC]] | B | PLCXD1 activity raises GLDC's level | lines that do not express PLCXD1 (11) vs lines expressing it (39) | 2.15× lower at baseline in the lines without PLCXD1 | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, 6.3); signed map (-7.2, 44.8). **Vector** length 101, 24.6% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +4.8 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -8.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -2.7 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -0.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol specific phospholipase C X domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 and Yp11.32 — chrX:276,322-303,356 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11323 |
| Gene groups (HGNC) | Pseudoautosomal region 1 |
| Matched by | ensembl_id |

UniProt [Q9NUJ7](https://www.uniprot.org/uniprotkb/Q9NUJ7) carries no function annotation.

**Summary**, from NCBI Gene [55344](https://www.ncbi.nlm.nih.gov/gene/55344):

> This gene is the most terminal protein-coding gene in the pseudoautosomal (PAR) region on chromosomes X and Y. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:23148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23148) · Entrez [55344](https://www.ncbi.nlm.nih.gov/gene/55344) · UniProt [Q9NUJ7](https://www.uniprot.org/uniprotkb/Q9NUJ7) · Ensembl [ENSG00000182378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182378)

## Data

Gene col 11281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11281); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11281]; `tensor/DDL_lfc|DDL_z.npy` [11281]; `embed/gene_vectors.npy` [11281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11281 or target_col == 11281). Every well: [[PLCXD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCXD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
