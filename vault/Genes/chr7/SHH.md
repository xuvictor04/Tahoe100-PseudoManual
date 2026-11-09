---
symbol: "SHH"
type: "gene"
col: 8990
ensembl_id: "ENSG00000164690"
name: "sonic hedgehog signaling molecule"
location: "7q36.3"
module: 162
arm: "+"
pooled_cpm: 3.79
n_lines_expressing: 21
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 20
direction_downstream: 46
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# SHH

*sonic hedgehog signaling molecule* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.05× (z +11.5, q 7e-28, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +9.8, q 1e-20, up in 6 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.574× (z -4.7, q 0.002, down in 10 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA2]] (+0.71, fdr 7e-06), [[LINC00659]] (+0.64, fdr 7e-06), [[ABHD11]] (+0.64, fdr 7e-06); moves opposite to [[ELMOD3]] (-0.50, fdr 4e-05), [[SNX3]] (-0.49, fdr 3e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[PDE9A]] → it (grade B ⚠); 46 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +11.5 | 7e-28 | 2/7 (PANC-1, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.81×** | +11.4 | 7e-28 | 3/13 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +9.8 | 1e-20 | 6/18 (A549, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +9.6 | 7e-20 | 10/19 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +9.2 | 5e-18 | 12/19 (LS 180, SNU-423, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.93×** | +8.5 | 2e-15 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +5.8 | 7e-07 | 11/19 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.5 | 2e-06 | 1/13 (MIA PaCa-2) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +5.3 | 9e-06 | 8/19 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.18×** | +4.7 | 1e-04 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.3 | 0.001 | 4/17 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.00×** | +4.2 | 0.001 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.1 | 0.002 | 1/17 (SW480) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +3.9 | 0.004 | 3/14 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.011 | 3/19 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.032 | 1/19 (NCI-H23) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.038 | 1/19 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.038 | 4/16 (HepG2/C3A, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.41×** | +2.9 | 0.085 | 3/15 (SW480, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.085 | 0/16 | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +2.9 | 0.087 | 9/19 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +2.9 | 0.087 | 4/19 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.092 | 1/17 (Panc 03.27) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.574×** | -4.7 | 0.002 | 10/19 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.612×** | -4.2 | 0.007 | 13/19 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.639×** | -3.7 | 0.043 | 8/19 (SW1417, A549, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -3.5 | 0.058 | 3/19 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.650×** | -3.4 | 0.067 | 7/19 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.734×** | -3.4 | 0.067 | 10/19 (MIA PaCa-2, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.686×** | -3.2 | 0.087 | 13/19 (MIA PaCa-2, SW48, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.686×** | -3.2 | 0.087 | 9/19 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | 0.499× | -3.1 | 0.12 | 9/17 (KATO III, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 0.511× | -3.0 | 0.15 | 4/19 (MIA PaCa-2, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 17.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.225× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 2 | — | [[Benproperine (phosphate) (drug)]] 0.05 µM 0.0517× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 9.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0301× (z -17.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0676× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0787× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.81 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.279× (z -16.7) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 9.82 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.300× (z -14.4) ⚠ position not correctable |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0303× (z -8.6) ⚠ cell-cycle shift, explains ~98% of this change |
| [[A-172 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA2]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[LINC00659]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ABHD11]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[KRT18]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[SLC52A3]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[KCNH8]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MAP2K3]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[PIWIL1]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MST1R]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[EGR2]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TRIM15]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMOD3]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SNX3]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE9A]] | B | PDE9A activity raises SHH's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.13× lower at baseline in the lines without PDE9A | 0.026 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[ABCC3]] | B | ABCC3 activity raises SHH's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without ABCC3 | 0.038 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[IQGAP2]] | B | IQGAP2 activity raises SHH's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without IQGAP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[ZNF860]] | B | ZNF860 activity raises SHH's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without ZNF860 | 0.052 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[MAP2K2]] | B | MAP2K2 activity raises SHH's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PRSS22]] | C | PRSS22 activity raises SHH's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 3.40× lower at baseline in the lines without PRSS22 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14; co-absent with the target |
| [[GPR35]] | C | GPR35 activity raises SHH's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.01× lower at baseline in the lines without GPR35 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent; co-absent with the target |
| [[EREG]] | C | EREG activity raises SHH's level | lines that do not express EREG (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without EREG | 0.022 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1; co-absent with the target |
| [[CYP3A5]] | C | CYP3A5 activity raises SHH's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.02× lower at baseline in the lines without CYP3A5 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises SHH's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without HNF4A | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises SHH's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without COL17A1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[GOLT1A]] | C | GOLT1A activity raises SHH's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without GOLT1A | 0.060 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 19, C 27. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | SHH activity raises EPHA2's level | lines that do not express SHH (29) vs lines expressing it (21) | 3.92× lower at baseline in the lines without SHH | 0.005 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[ITGA6]] | B | SHH activity raises ITGA6's level | lines that do not express SHH (29) vs lines expressing it (21) | 3.49× lower at baseline in the lines without SHH | 0.005 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[BAIAP2L2]] | B | SHH activity raises BAIAP2L2's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.74× lower at baseline in the lines without SHH | 0.008 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[PDE9A]] | B | SHH activity raises PDE9A's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.77× lower at baseline in the lines without SHH | 0.012 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[KRT8]] | B | SHH activity raises KRT8's level | lines that do not express SHH (29) vs lines expressing it (21) | 3.91× lower at baseline in the lines without SHH | 0.012 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[VPS37B]] | B | SHH activity raises VPS37B's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without SHH | 0.012 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[SOX13]] | B | SHH activity raises SOX13's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.75× lower at baseline in the lines without SHH | 0.038 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[ABCC3]] | B | SHH activity raises ABCC3's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.83× lower at baseline in the lines without SHH | 0.041 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[GPR39]] | B | SHH activity raises GPR39's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without SHH | 0.044 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[SH3D19]] | B | SHH activity raises SH3D19's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without SHH | 0.045 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[ZNF860]] | B | SHH activity raises ZNF860's level | lines that do not express SHH (29) vs lines expressing it (21) | 2.12× lower at baseline in the lines without SHH | 0.047 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[SFR1]] | B | SHH activity raises SFR1's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without SHH | 0.048 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.5, 50.8); signed map (6.1, 38.7). **Vector** length 50.0, 11.9% of its response variance represented; |z| ≥ 3 in 537 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +9.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +0.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.1 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sonic hedgehog signaling molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:155,799,980-155,812,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HHG1, SMMCI, TPT, TPTPS, MCOPCB5; previously HPE3, HLP3 |
| Gene groups (HGNC) | Hedgehog signaling molecule family |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 15 pathways, smallest: Formation of lateral plate mesoderm; Ligand-receptor interactions; Release of Hh-Np from the secreting cell |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15465](https://www.uniprot.org/uniprotkb/Q15465) (Sonic hedgehog protein):

> [Sonic hedgehog protein]: Precursor of sonic hedgehog, a morphogen that activates the smoothened signaling pathway, and which is essential for a variety of patterning events during development. The C-terminal part of the precursor displays an autoproteolysis and a cholesterol transferase activity, resulting (1) in the cleavage of the full-length protein into two parts, Sonic hedgehog protein N-product and C-product (ShhN and ShhC, respectively) and (2) covalent attachment of a cholesterol …

**Summary**, from NCBI Gene [6469](https://www.ncbi.nlm.nih.gov/gene/6469):

> This gene encodes a protein that is instrumental in patterning the early embryo. It has been implicated as the key inductive signal in patterning of the ventral neural tube, the anterior-posterior limb axis, and the ventral somites. Of three human proteins showing sequence and functional similarity to the sonic hedgehog protein of Drosophila, this protein is the most similar. The protein is made as a precursor that is autocatalytically cleaved; the N-terminal portion is soluble and contains the …

**Accessions** — [HGNC:10848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10848) · Entrez [6469](https://www.ncbi.nlm.nih.gov/gene/6469) · UniProt [Q15465](https://www.uniprot.org/uniprotkb/Q15465) · Ensembl [ENSG00000164690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164690)

## Data

Gene col 8990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8990); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8990]; `tensor/DDL_lfc|DDL_z.npy` [8990]; `embed/gene_vectors.npy` [8990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8990 or target_col == 8990). Every well: [[SHH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
