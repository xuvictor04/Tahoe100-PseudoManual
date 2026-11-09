---
symbol: "SEMA5A"
type: "gene"
col: 3417
ensembl_id: "ENSG00000112902"
name: "semaphorin 5A"
location: "5p15.31"
module: 13
arm: "+"
pooled_cpm: 68.14
n_lines_expressing: 22
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 49
direction_downstream: 44
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SEMA5A

*semaphorin 5A* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.22× (z +10.0, q 1e-20, up in 2 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +5.7, q 2e-06, up in 3 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.491× (z -9.2, q 2e-17, down in 17 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL5A1]] (+0.73, fdr 7e-06), [[LINC01411]] (+0.69, fdr 7e-06), [[APCDD1L]] (+0.67, fdr 7e-06); moves opposite to [[SRGN]] (-0.47, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[NMNAT2]] → it (grade B ⚠); 44 go from it, the strongest it → [[NMNAT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +10.0 | 1e-20 | 2/19 (NCI-H460, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +7.4 | 4e-11 | 3/19 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.9 | 8e-07 | 3/21 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.7 | 2e-06 | 3/20 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.5 | 4e-06 | 3/22 (LS 180, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.3 | 1e-05 | 5/20 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.007 | 9/20 (LoVo, Hs 766T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.073 | 7/20 (C32, Hs 766T, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.073 | 4/21 (C32, LoVo, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.079 | 4/21 (C32, LoVo, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.13 | 2/20 (C32, LoVo) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.491×** | -9.2 | 2e-17 | 17/20 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.557×** | -7.5 | 1e-11 | 17/20 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -7.1 | 3e-10 | 19/20 (RPMI-7951, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.610×** | -6.4 | 3e-08 | 19/20 (LoVo, RPMI-7951, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.627×** | -6.0 | 2e-07 | 16/20 (A-172, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -5.8 | 5e-07 | 19/20 (RPMI-7951, H4, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -5.8 | 7e-07 | 18/20 (H4, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -5.5 | 3e-06 | 17/20 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.666×** | -5.2 | 1e-05 | 11/20 (hTERT-HPNE, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.657×** | -5.2 | 1e-05 | 11/20 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.668×** | -5.2 | 1e-05 | 14/20 (RPMI-7951, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.670×** | -5.2 | 1e-05 | 10/20 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.675×** | -5.1 | 2e-05 | 13/20 (LoVo, HOP62, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.761×** | -5.0 | 3e-05 | 14/20 (hTERT-HPNE, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.694×** | -4.7 | 1e-04 | 12/20 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.725×** | -4.1 | 0.001 | 11/20 (hTERT-HPNE, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -3.9 | 0.004 | 14/20 (A-172, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 99.4 | 6 (1 ⚠) | 6 (3 ⚠) | [[Binimetinib (drug)]] 5 µM 4.12× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.162× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.177× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 9 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0682× (z -15.3) |
| [[H4 (line)]] | wt | 475 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0797× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -11.8) |
| [[A-172 (line)]] | wt | 453 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -21.0) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -12.2) |
| [[C32 (line)]] | wt | 138 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.4) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 371 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -9.8) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.206× (z -9.8) |
| [[J82 (line)]] | alt | 374 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -12.9) |
| [[SW1417 (line)]] | alt | 115 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -18.2) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0913× (z -13.7) |
| [[HS-578T (line)]] | alt | 567 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -10.5) |
| [[BT-474 (line)]] | alt | 48.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +18.3) ⚠ cell-cycle shift, explains <1% of this change | — |
| [[A498 (line)]] | wt | 36.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 179 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 62.4 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 5.04× (z +9.4) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[SNU-423 (line)]] | alt | 64.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -9.9) |
| [[SW 1088 (line)]] | alt | 692 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0205× (z -16.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A1]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CARMN]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ABI3BP]] | +0.66 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PDGFRB]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NAV1]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 | same gene group |
| [[THBS2]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 | pathway: Defective B3GALTL causes PpS |
| [[INSYN2B]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[SYNDIG1]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[GDNF-AS1]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[VSTM4]] | +0.61 | +0.57 / +0.64 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 2, C 47. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMNAT2]] | B | NMNAT2 activity raises SEMA5A's level | lines that do not express NMNAT2 (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without NMNAT2 | 0.045 | ⚠ within organs, on part of the lines; also absent: NTF3, C7orf57, CELF2; maybe low, not absent |
| [[RASGEF1A]] | B | RASGEF1A activity lowers SEMA5A's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 3.44× higher at baseline in the lines without RASGEF1A | 0.051 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[HTR1F]] | C | HTR1F activity raises SEMA5A's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 7.18× lower at baseline in the lines without HTR1F | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[SNHG18]] | C | SNHG18 activity raises SEMA5A's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 9.87× lower at baseline in the lines without SNHG18 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises SEMA5A's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 9.31× lower at baseline in the lines without PDGFRB | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises SEMA5A's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 4.56× lower at baseline in the lines without SPOCK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises SEMA5A's level | lines that do not express GDNF (38) vs lines expressing it (12) | 6.07× lower at baseline in the lines without GDNF | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[BAALC]] | C | BAALC activity raises SEMA5A's level | lines that do not express BAALC (32) vs lines expressing it (18) | 5.18× lower at baseline in the lines without BAALC | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises SEMA5A's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 7.23× lower at baseline in the lines without TIMP3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises SEMA5A's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 6.72× lower at baseline in the lines without ITGA11 | 0.009 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises SEMA5A's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 5.75× lower at baseline in the lines without COL15A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[P3H2]] | C | P3H2 activity raises SEMA5A's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 3.89× lower at baseline in the lines without P3H2 | 0.010 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 11, C 33. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMNAT2]] | B | SEMA5A activity raises NMNAT2's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.49× lower at baseline in the lines without SEMA5A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[SYNJ2]] | B | SEMA5A activity raises SYNJ2's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without SEMA5A | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[RASGEF1A]] | B | SEMA5A activity lowers RASGEF1A's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 1.70× higher at baseline in the lines without SEMA5A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[SETBP1]] | B | SEMA5A activity raises SETBP1's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 3.19× lower at baseline in the lines without SEMA5A | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[PRSS23]] | B | SEMA5A activity raises PRSS23's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.54× lower at baseline in the lines without SEMA5A | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[BMPER]] | B | SEMA5A activity raises BMPER's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without SEMA5A | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[RNF152]] | B | SEMA5A activity raises RNF152's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 3.03× lower at baseline in the lines without SEMA5A | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[SYNJ2]] | B | SEMA5A activity strengthens SYNJ2's drug response | lines that do not express SEMA5A (25) vs lines expressing it (20) | the lines without SEMA5A respond 0.62× as strongly (z diff +2.07); strongest at Topotecan (hydrochloride) 5 µM: 0.78x vs 0.55x (z diff +3.5) | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; target measured in part of the lines; artifact flags |
| [[SLCO1C1]] | B | SEMA5A activity raises SLCO1C1's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 1.67× lower at baseline in the lines without SEMA5A | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| cells under [[Mebendazole (drug)]] 5 µM | B | SEMA5A activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express SEMA5A (28) vs lines expressing it (20) | the lines without SEMA5A: 0.70× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[MYO10]] | B | SEMA5A activity raises MYO10's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without SEMA5A | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH |
| [[SNHG18]] | C | SEMA5A activity raises SNHG18's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 4.77× lower at baseline in the lines without SEMA5A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.3, 17.7); signed map (24.7, 46.9). **Vector** length 93.0, 32.8% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.52 to 9); *Collagen chain trimerization* (reactome, mean cos +0.51 to 7); *NCAM1 interactions* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | +3.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +0.2 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -6.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.31 — chr5:9,035,033-9,546,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | semF; previously SEMAF |
| Gene groups (HGNC) | Semaphorins; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: Other semaphorin interactions; Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13591](https://www.uniprot.org/uniprotkb/Q13591) (Semaphorin-5A):

> Bifunctional axonal guidance cue regulated by sulfated proteoglycans; attractive effects result from interactions with heparan sulfate proteoglycans (HSPGs), while the inhibitory effects depend on interactions with chondroitin sulfate proteoglycans (CSPGs) (By similarity). Ligand for receptor PLXNB3. In glioma cells, SEMA5A stimulation of PLXNB3 results in the disassembly of F-actin stress fibers, disruption of focal adhesions and cellular collapse as well as inhibition of cell migration and …

**Summary**, from NCBI Gene [9037](https://www.ncbi.nlm.nih.gov/gene/9037):

> This gene belongs to the semaphorin gene family that encodes membrane proteins containing a semaphorin domain and several thrombospondin type-1 repeats. Members of this family are involved in axonal guidance during neural development. This gene has been implicated as an autism susceptibility gene.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:10736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10736) · Entrez [9037](https://www.ncbi.nlm.nih.gov/gene/9037) · UniProt [Q13591](https://www.uniprot.org/uniprotkb/Q13591) · Ensembl [ENSG00000112902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112902)

## Data

Gene col 3417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3417); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3417]; `tensor/DDL_lfc|DDL_z.npy` [3417]; `embed/gene_vectors.npy` [3417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3417 or target_col == 3417). Every well: [[SEMA5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
