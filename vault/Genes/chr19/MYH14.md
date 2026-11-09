---
symbol: "MYH14"
type: "gene"
col: 2588
ensembl_id: "ENSG00000105357"
name: "myosin heavy chain 14"
location: "19q13.33"
module: 8
arm: "+"
pooled_cpm: 90.82
n_lines_expressing: 29
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 92
direction_downstream: 116
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MYH14

*myosin heavy chain 14* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.72× (z +15.4, q 0e+00, up in 21 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 2.55× (z +13.6, q 2e-39, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.697× (z -5.5, q 2e-05, down in 19 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC4]] (+0.73, fdr 7e-06), [[CLIC5]] (+0.72, fdr 7e-06), [[MUC3A]] (+0.72, fdr 7e-06); moves opposite to [[PHC2-AS1]] (-0.57, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 92 arrows point to it, the strongest [[CYP4F3]] → it (grade B ⚠); 116 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +15.4 | 0e+00 | 21/28 (C-33 A, C32, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.55×** | +13.6 | 2e-39 | 18/27 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.40×** | +13.5 | 4e-39 | 23/27 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.29×** | +12.7 | 8e-35 | 22/27 (PANC-1, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +11.5 | 1e-28 | 16/27 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +11.1 | 1e-26 | 18/27 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +10.6 | 1e-24 | 15/25 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +10.6 | 2e-24 | 15/23 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +9.1 | 4e-18 | 17/27 (SW480, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +8.1 | 2e-14 | 14/27 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.88×** | +5.8 | 3e-07 | 11/28 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-06 | 17/28 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.4 | 3e-06 | 14/26 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.8 | 7e-05 | 14/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.003 | 13/27 (AsPC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.065 | 10/27 (BT-474, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.697×** | -5.5 | 2e-05 | 19/27 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.780×** | -5.4 | 2e-05 | 18/27 (SW48, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -5.3 | 2e-05 | 20/27 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.806×** | -4.7 | 5e-04 | 7/27 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.752×** | -4.4 | 0.001 | 17/27 (AsPC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.613×** | -3.9 | 0.009 | 17/28 (HT-29, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.024 | 18/27 (LS 180, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.5 | 0.032 | 2/29 (AN3 CA, NCI-H661) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.807× | -3.1 | 0.13 | 4/27 (SW480, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.0 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.48× (z +17.7) | — |
| [[SW480 (line)]] | alt | 24.5 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 1,095 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -24.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -12.0) |
| [[BT-474 (line)]] | alt | 116 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.275× (z -11.6) |
| [[C32 (line)]] | wt | 32.2 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.73× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 299 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -13.6) |
| [[A-427 (line)]] | wt | 54.6 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.69× (z +12.3) | — |
| [[AsPC-1 (line)]] | alt | 113 | 4 (1 ⚠) | 1 | [[Binimetinib (drug)]] 0.05 µM 2.34× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -8.8) |
| [[C-33 A (line)]] | alt | 28.9 | 4 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.65× (z +9.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -8.6) |
| [[LoVo (line)]] | wt | 289 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 61.0 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.44× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 161 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[SW48 (line)]] | wt | 235 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.432× (z -11.0) |
| [[COLO 205 (line)]] | alt | 229 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 153 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -11.9) |
| [[SW1417 (line)]] | alt | 343 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 54.3 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.73× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -9.1) |
| [[KATO III (line)]] | alt | 266 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -20.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.51× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 61.0 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.72× (z +8.9) | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0625× (z -8.8) |
| [[SW 900 (line)]] | alt | 27.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.65× (z +9.2) | — |
| [[A-172 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.18 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.00 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC4]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.72 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[MUC3A]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ALOX5]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TJP3]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PLEKHG6]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[FUT2]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[CYP4F12]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[BICDL2]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MUC13]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2-AS1]] | -0.57 | -0.46 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*92 arrows, 92 of them with an alert ⚠; grade A 0, B 30, C 62. Shown: the 12 strongest; 80 more arrows (80 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP4F3]] | B | CYP4F3 activity raises MYH14's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 4.50× lower at baseline in the lines without CYP4F3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[EPS8L1]] | B | EPS8L1 activity raises MYH14's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without EPS8L1 | 0.005 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[ARHGAP30]] | B | ARHGAP30 activity raises MYH14's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without ARHGAP30 | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[MUC13]] | B | MUC13 activity raises MYH14's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 7.18× lower at baseline in the lines without MUC13 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[CYP4F12]] | B | CYP4F12 activity raises MYH14's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.95× lower at baseline in the lines without CYP4F12 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[UCA1]] | B | UCA1 activity raises MYH14's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 4.46× lower at baseline in the lines without UCA1 | 0.011 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[MUC17]] | B | MUC17 activity raises MYH14's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 7.09× lower at baseline in the lines without MUC17 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[CLU]] | B | CLU activity lowers MYH14's level | lines that do not express CLU (11) vs lines expressing it (39) | 3.47× higher at baseline in the lines without CLU | 0.016 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HHLA2]] | B | HHLA2 activity raises MYH14's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 4.76× lower at baseline in the lines without HHLA2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[MISP]] | B | MISP activity raises MYH14's level | lines that do not express MISP (23) vs lines expressing it (27) | 3.89× lower at baseline in the lines without MISP | 0.016 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[GABRP]] | B | GABRP activity raises MYH14's level | lines that do not express GABRP (44) vs lines expressing it (6) | 5.45× lower at baseline in the lines without GABRP | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[HEPH]] | B | HEPH activity raises MYH14's level | lines that do not express HEPH (41) vs lines expressing it (9) | 6.88× lower at baseline in the lines without HEPH | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |

### Downstream of this gene

*116 arrows, 116 of them with an alert ⚠; grade A 0, B 61, C 55. Shown: the 12 strongest; 104 more arrows (104 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | MYH14 activity raises EPS8L1's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 3.29× lower at baseline in the lines without MYH14 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ELF3-AS1]] | B | MYH14 activity raises ELF3-AS1's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.77× lower at baseline in the lines without MYH14 | 0.002 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ABHD11]] | B | MYH14 activity raises ABHD11's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.24× lower at baseline in the lines without MYH14 | 0.003 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[MISP]] | B | MYH14 activity raises MISP's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 3.29× lower at baseline in the lines without MYH14 | 0.012 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[CD24]] | B | MYH14 activity raises CD24's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.72× lower at baseline in the lines without MYH14 | 0.012 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | B | MYH14 activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.71× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | MYH14 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.16× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[KIAA1522]] | B | MYH14 activity raises KIAA1522's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.11× lower at baseline in the lines without MYH14 | 0.019 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | B | MYH14 activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.79× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | B | MYH14 activity raises the cells' numbers under Vinblastine (sulfate) 0.05 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.86× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ZDHHC11B]] | B | MYH14 activity raises ZDHHC11B's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.11× lower at baseline in the lines without MYH14 | 0.028 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[BCL2L15]] | B | MYH14 activity raises BCL2L15's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.18× lower at baseline in the lines without MYH14 | 0.028 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.1, 53.8); signed map (61.0, 5.6). **Vector** length 115, 37.5% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *O-linked glycosylation of mucins* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.6 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +15.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.1 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +10.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +9.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +3.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.4 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -5.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | myosin heavy chain 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:50,188,186-50,310,542 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13881, KIAA2034, MHC16, MYH17; previously DFNA4 |
| Gene groups (HGNC) | Myosin heavy chains, class II |
| Reactome | 14 pathways, smallest: RHO GTPases Activate ROCKs; RHO GTPases activate CIT; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z406](https://www.uniprot.org/uniprotkb/Q7Z406) (Myosin-14):

> Cellular myosin that appears to play a role in cytokinesis, cell shape, and specialized functions such as secretion and capping.

**Summary**, from NCBI Gene [79784](https://www.ncbi.nlm.nih.gov/gene/79784):

> This gene encodes a member of the myosin superfamily. The protein represents a conventional non-muscle myosin; it should not be confused with the unconventional myosin-14 (MYO14). Myosins are actin-dependent motor proteins with diverse functions including regulation of cytokinesis, cell motility, and cell polarity. Mutations in this gene result in one form of autosomal dominant hearing impairment. Multiple transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:23212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23212) · Entrez [79784](https://www.ncbi.nlm.nih.gov/gene/79784) · UniProt [Q7Z406](https://www.uniprot.org/uniprotkb/Q7Z406) · Ensembl [ENSG00000105357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105357)

## Data

Gene col 2588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2588); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2588]; `tensor/DDL_lfc|DDL_z.npy` [2588]; `embed/gene_vectors.npy` [2588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2588 or target_col == 2588). Every well: [[MYH14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYH14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
