---
symbol: "EPHB1"
type: "gene"
col: 7855
ensembl_id: "ENSG00000154928"
name: "EPH receptor B1"
location: "3q22.2"
module: 61
arm: "+"
pooled_cpm: 12.09
n_lines_expressing: 34
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# EPHB1

*EPH receptor B1* — 3q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.32× (z +19.5, q 0e+00, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.588× (z -7.1, q 6e-10, down in 19 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS6ST3]] (+0.69, fdr 7e-06), [[SYN1]] (+0.67, fdr 7e-06), [[VAT1L]] (+0.65, fdr 1e-05); moves opposite to [[TCEANC2]] (-0.55, fdr 6e-05), [[NUDT13]] (-0.52, fdr 1e-04), [[ELMOD3]] (-0.51, fdr 4e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ADAM7-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[HMGA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.32×** | +19.5 | 0e+00 | 26/31 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +17.3 | 0e+00 | 25/32 (A-427, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.65×** | +17.3 | 0e+00 | 25/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.53×** | +12.4 | 4e-33 | 25/31 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.35×** | +11.4 | 4e-28 | 24/31 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +11.1 | 2e-26 | 16/30 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +10.5 | 6e-24 | 13/29 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +9.9 | 3e-21 | 3/12 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +6.9 | 3e-10 | 13/30 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +6.3 | 2e-08 | 14/28 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.8 | 3e-07 | 5/21 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +5.5 | 2e-06 | 15/31 (PANC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.3 | 6e-04 | 3/17 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.23×** | +3.8 | 0.005 | 10/32 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.007 | 8/29 (BT-474, SNU-423, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.012 | 2/31 (BT-474, LoVo) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -7.1 | 6e-10 | 19/29 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -7.0 | 9e-10 | 18/31 (NCI-H1573, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.608×** | -6.7 | 5e-09 | 18/32 (C-33 A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.611×** | -6.6 | 5e-09 | 20/29 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -5.0 | 7e-05 | 9/29 (SW1417, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.697×** | -4.8 | 1e-04 | 13/29 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.736×** | -4.1 | 0.003 | 15/30 (C-33 A, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.564×** | -4.0 | 0.004 | 12/27 (HS-578T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.770×** | -3.5 | 0.027 | 11/30 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -3.3 | 0.051 | 9/27 (HS-578T, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.785×** | -3.3 | 0.057 | 9/30 (C-33 A, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 194 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -11.8) |
| [[PANC-1 (line)]] | alt | 3.99 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 20.0× (z +13.1) | — |
| [[NCI-H460 (line)]] | wt | 4.82 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 4.01× (z +9.5) | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.159× (z -9.0) |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0320× (z -13.9) |
| [[H4 (line)]] | wt | 27.2 | 3 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 9.22× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 8.79 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 8.24× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.120× (z -9.4) |
| [[SW1417 (line)]] | alt | 82.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -14.8) |
| [[A-427 (line)]] | wt | 4.96 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.51× (z +11.0) | — |
| [[J82 (line)]] | alt | 4.88 | 0 | 2 | — | [[Budesonide (drug)]] 0.5 µM 0.0541× (z -10.5) |
| [[A-172 (line)]] | wt | 3.79 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0950× (z -8.5) |
| [[BT-474 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 7.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0244× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.552× (z -8.8) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 7.86 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0426× (z -11.7) |
| [[A498 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS6ST3]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SYN1]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[VAT1L]] | +0.65 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[KCNN2]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[ALK]] | +0.60 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[CALB2]] | +0.59 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[COLEC12]] | +0.59 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[CRTAC1]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[PKNOX2]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SH3GL2]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[KCNK13]] | +0.56 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[KCNN3]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEANC2]] | -0.55 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[NUDT13]] | -0.52 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[ELMOD3]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TRAPPC13]] | -0.48 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[C2orf42]] | -0.47 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[SNX13]] | -0.47 | -0.38 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM7-AS1]] | B | ADAM7-AS1 activity raises EPHB1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.81× lower at baseline in the lines without ADAM7-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[KCNK13]] | B | KCNK13 activity raises EPHB1's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 2.74× lower at baseline in the lines without KCNK13 | 0.085 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[MIR646HG]] | B | MIR646HG activity raises EPHB1's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.01× lower at baseline in the lines without MIR646HG | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |
| [[OR4F15]] | C | OR4F15 activity raises EPHB1's level | lines that do not express OR4F15 (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without OR4F15 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, PHACTR1, ITGA4; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA1]] | B | EPHB1 activity lowers HMGA1's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 2.01× higher at baseline in the lines without EPHB1 | 0.005 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent |
| [[MEG3]] | B | EPHB1 activity raises MEG3's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without EPHB1 | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent |
| [[MEG8]] | B | EPHB1 activity raises MEG8's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 2.56× lower at baseline in the lines without EPHB1 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent |
| [[ELMOD3]] | B | EPHB1 activity raises ELMOD3's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without EPHB1 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent |
| [[SPOCK1]] | C | EPHB1 activity raises SPOCK1's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 4.62× lower at baseline in the lines without EPHB1 | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent; co-absent with the target |
| [[OR4F15]] | C | EPHB1 activity raises OR4F15's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without EPHB1 | 0.087 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, 33.4); signed map (31.9, 26.2). **Vector** length 59.1, 9.97% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +0.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | -0.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | +1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.2 — chr3:134,795,260-135,260,467 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hek6; previously EPHT2 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Reactome | 6 pathways, smallest: Ephrin signaling; EPHB-mediated forward signaling; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P54762](https://www.uniprot.org/uniprotkb/P54762) (Ephrin type-B receptor 1):

> Receptor tyrosine kinase which binds promiscuously transmembrane ephrin-B family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Cognate/functional ephrin ligands for this receptor include EFNB1, EFNB2 and EFNB3. During nervous system development, …

**Summary**, from NCBI Gene [2047](https://www.ncbi.nlm.nih.gov/gene/2047):

> Ephrin receptors and their ligands, the ephrins, mediate numerous developmental processes, particularly in the nervous system. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which are transmembrane proteins. The Eph family of receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and …

**Accessions** — [HGNC:3392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3392) · Entrez [2047](https://www.ncbi.nlm.nih.gov/gene/2047) · UniProt [P54762](https://www.uniprot.org/uniprotkb/P54762) · Ensembl [ENSG00000154928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154928)

## Data

Gene col 7855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7855); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7855]; `tensor/DDL_lfc|DDL_z.npy` [7855]; `embed/gene_vectors.npy` [7855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7855 or target_col == 7855). Every well: [[EPHB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
