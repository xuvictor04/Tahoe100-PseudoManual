---
symbol: "PLEKHS1"
type: "gene"
col: 7311
ensembl_id: "ENSG00000148735"
name: "pleckstrin homology domain containing S1"
location: "10q25.3"
module: 87
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 35
n_dd_up: 22
n_dd_down: 19
n_dd_up_clean: 17
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 15
direction_downstream: 27
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# PLEKHS1

*pleckstrin homology domain containing S1* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.48× (z +10.2, q 1e-21, up in 9 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.370× (z -7.9, q 1e-12, down in 22 of 31 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.422× (z -6.9, q 2e-09, down in 20 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTTNBP2]] (+0.63, fdr 1e-05), [[ATP10B]] (+0.62, fdr 1e-05), [[FAM3B]] (+0.62, fdr 1e-05); moves opposite to [[AHNAK2]] (-0.45, fdr 1e-04), [[C3orf18]] (-0.44, fdr 2e-04), [[IAH1]] (-0.43, fdr 2e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[ATP10B]] → it (grade B ⚠); 27 go from it, the strongest it → [[CATSPERB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +10.2 | 1e-21 | 9/21 (HEC-1-A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +10.1 | 1e-21 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +7.9 | 6e-13 | 1/6 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +7.0 | 5e-10 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +5.4 | 6e-06 | 5/23 (A-172, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.89×** | +4.9 | 1e-04 | 7/15 (KATO III, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.007 | 7/31 (SW1417, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +3.7 | 0.018 | 3/32 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.045 | 11/24 (SW1417, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.35×** | +3.3 | 0.045 | 4/31 (NCI-H460, KATO III, …) | top dose only | low cells (technical?) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.52×** | +3.3 | 0.045 | 1/31 (SW1417) | inconsistent across doses |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.045 | 1/23 (KATO III) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.053 | 1/21 (LoVo) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.054 | 2/13 (LoVo, A498) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.054 | 1/16 (HEC-1-A) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.054 | 0/13 | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.53×** | +3.1 | 0.057 | 0/11 | inconsistent across doses |  |
| [[Imiquimod (maleate) (drug)]] 5 µM |  | **1.48×** | +3.0 | 0.082 | 0/15 | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.50×** | +3.0 | 0.082 | 0/11 | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.45×** | +2.9 | 0.088 | 4/29 (CFPAC-1, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.370×** | -7.9 | 1e-12 | 22/31 (SW1417, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.422×** | -6.9 | 2e-09 | 20/30 (C32, COLO 205, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.567×** | -6.4 | 3e-08 | 17/23 (SW1417, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.448×** | -6.1 | 1e-07 | 15/29 (SW1417, KATO III, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.474×** | -6.0 | 3e-07 | 16/27 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.495×** | -5.6 | 2e-06 | 19/27 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.498×** | -5.6 | 2e-06 | 18/27 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.504×** | -5.5 | 4e-06 | 16/31 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.527×** | -5.1 | 2e-05 | 12/24 (KATO III, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.543×** | -4.7 | 2e-04 | 11/28 (NCI-H2030, COLO 205, …) | top dose only |  |
| [[Bexarotene (drug)]] 5 µM |  | **0.565×** | -4.6 | 3e-04 | 10/31 (NCI-H460, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.583×** | -4.3 | 8e-04 | 12/29 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.622×** | -3.8 | 0.007 | 11/29 (C32, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.433×** | -3.5 | 0.020 | 11/26 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.738×** | -3.4 | 0.023 | 7/30 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.029 | 6/31 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.761×** | -3.1 | 0.063 | 5/31 (KATO III, SW48, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **0.669×** | -3.1 | 0.063 | 6/28 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.680×** | -3.1 | 0.063 | 13/26 (SK-MEL-2, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 22.5 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0358× (z -21.1) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0800× (z -11.3) |
| [[C32 (line)]] | wt | 36.2 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0728× (z -16.2) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0307× (z -15.2) |
| [[KATO III (line)]] | alt | 13.1 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0135× (z -16.4) |
| [[COLO 205 (line)]] | alt | 30.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -14.8) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0264× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0119× (z -17.7) |
| [[A498 (line)]] | wt | 3.53 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -9.2) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A-172 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.731 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.731 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.565 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTTNBP2]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ATP10B]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[FAM3B]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[SLC44A3-AS1]] | +0.57 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[TMEM229B]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ARHGAP6]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[LDLRAD4]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SMIM2-AS1]] | +0.54 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[SAMMSON]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LEF1-AS1]] | +0.53 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[A2M]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[NTRK2]] | +0.52 | +0.38 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHNAK2]] | -0.45 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[C3orf18]] | -0.44 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[IAH1]] | -0.43 | -0.47 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP10B]] | B | ATP10B activity raises PLEKHS1's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 4.17× lower at baseline in the lines without ATP10B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[COL19A1]] | B | COL19A1 activity raises PLEKHS1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 1.73× lower at baseline in the lines without COL19A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7 |
| [[MGAM2]] | B | MGAM2 activity raises PLEKHS1's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without MGAM2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[PRR15]] | B | PRR15 activity raises PLEKHS1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 1.37× lower at baseline in the lines without PRR15 | 0.030 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[GJB1]] | B | GJB1 activity raises PLEKHS1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.83× lower at baseline in the lines without GJB1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |
| [[CD74]] | B | CD74 activity raises PLEKHS1's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without CD74 | 0.046 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[VSNL1]] | B | VSNL1 activity raises PLEKHS1's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.09× lower at baseline in the lines without VSNL1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[FBXO39]] | B | FBXO39 activity raises PLEKHS1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without FBXO39 | 0.063 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[B3GNT7]] | B | B3GNT7 activity raises PLEKHS1's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.70× lower at baseline in the lines without B3GNT7 | 0.081 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[CTSS]] | B | CTSS activity raises PLEKHS1's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.43× lower at baseline in the lines without CTSS | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[LHFPL3-AS1]] | B | LHFPL3-AS1 activity raises PLEKHS1's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 2.88× lower at baseline in the lines without LHFPL3-AS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1 |
| [[PLA2G2A]] | B | PLA2G2A activity raises PLEKHS1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 1.78× lower at baseline in the lines without PLA2G2A | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CATSPERB]] | B | PLEKHS1 activity raises CATSPERB's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 3.22× lower at baseline in the lines without PLEKHS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[PLSCR2]] | B | PLEKHS1 activity raises PLSCR2's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without PLEKHS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[PRR15]] | B | PLEKHS1 activity raises PRR15's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.93× lower at baseline in the lines without PLEKHS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[SIDT1]] | B | PLEKHS1 activity raises SIDT1's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 2.37× lower at baseline in the lines without PLEKHS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[NRIR]] | B | PLEKHS1 activity raises NRIR's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.68× lower at baseline in the lines without PLEKHS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[SLC44A3-AS1]] | B | PLEKHS1 activity raises SLC44A3-AS1's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 2.08× lower at baseline in the lines without PLEKHS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[TCN1]] | B | PLEKHS1 activity raises TCN1's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without PLEKHS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| cells under [[Trifluridine (drug)]] 0.5 µM | B | PLEKHS1 activity raises the cells' numbers under Trifluridine 0.5 µM (protects the cells) | lines that do not express PLEKHS1 (15) vs lines expressing it (33) | the lines without PLEKHS1: 0.87× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[C4orf19]] | B | PLEKHS1 activity raises C4orf19's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without PLEKHS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[MGAM2]] | B | PLEKHS1 activity raises MGAM2's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without PLEKHS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[MUC5B]] | B | PLEKHS1 activity raises MUC5B's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without PLEKHS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[LINC02331]] | B | PLEKHS1 activity raises LINC02331's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without PLEKHS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.1, 57.5); signed map (67.0, 1.7). **Vector** length 61.7, 12.3% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +5.4 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.6 | -6.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing S1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:113,751,262-113,783,429 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23537, bA211N11.2; previously C10orf81 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

UniProt [Q5SXH7](https://www.uniprot.org/uniprotkb/Q5SXH7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26285) · Entrez [79949](https://www.ncbi.nlm.nih.gov/gene/79949) · UniProt [Q5SXH7](https://www.uniprot.org/uniprotkb/Q5SXH7) · Ensembl [ENSG00000148735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148735)

## Data

Gene col 7311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7311); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7311]; `tensor/DDL_lfc|DDL_z.npy` [7311]; `embed/gene_vectors.npy` [7311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7311 or target_col == 7311). Every well: [[PLEKHS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
