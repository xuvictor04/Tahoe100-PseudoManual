---
symbol: "ETNK2"
type: "gene"
col: 6813
ensembl_id: "ENSG00000143845"
name: "ethanolamine kinase 2"
location: "1q32.1"
module: 82
arm: "+"
pooled_cpm: 3.71
n_lines_expressing: 39
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# ETNK2

*ethanolamine kinase 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.92× (z +7.3, q 2e-10, up in 1 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.97× (z +7.2, q 2e-10, up in 17 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.491× (z -8.3, q 7e-14, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5R1]] (+0.68, fdr 1e-05), [[HDAC11]] (+0.66, fdr 2e-05), [[CARMIL2]] (+0.61, fdr 4e-05); moves opposite to [[DARS1-AS1]] (-0.59, fdr 7e-05), [[ANKRD17-DT]] (-0.54, fdr 2e-04), [[CRPPA]] (-0.53, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[DNAJB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.3 | 2e-10 | 1/8 (CFPAC-1) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +7.2 | 2e-10 | 17/35 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +7.1 | 2e-10 | 14/32 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +5.7 | 2e-06 | 14/36 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.4 | 1e-05 | 7/19 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +5.2 | 2e-05 | 11/29 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +5.1 | 3e-05 | 13/36 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 4e-05 | 8/32 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +4.1 | 0.002 | 1/11 (A-172) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.004 | 6/35 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.009 | 8/35 (PANC-1, SHP-77, …) | two highest doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.51×** | +3.4 | 0.029 | 2/12 (PANC-1, A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.030 | 6/32 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.031 | 9/36 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.031 | 4/35 (HCT15, NCI-H2347, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.032 | 3/29 (LoVo, SNU-423, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.040 | 4/32 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.078 | 1/18 (A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.491×** | -8.3 | 7e-14 | 23/36 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -6.3 | 1e-07 | 16/27 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -6.1 | 2e-07 | 17/29 (C32, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.628×** | -5.4 | 8e-06 | 11/36 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -5.3 | 1e-05 | 16/33 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -5.1 | 4e-05 | 15/26 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.627×** | -4.9 | 6e-05 | 13/33 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -4.9 | 6e-05 | 11/35 (A-172, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.694×** | -4.3 | 0.001 | 4/36 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.713×** | -3.9 | 0.004 | 8/33 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.708×** | -3.9 | 0.006 | 8/29 (HepG2/C3A, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.553×** | -3.6 | 0.015 | 9/29 (NCI-H1792, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.659×** | -3.5 | 0.023 | 4/37 (CFPAC-1, SW 1271, …) | two highest doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -3.1 | 0.067 | 11/30 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.1) |
| [[HOP62 (line)]] | alt | 5.92 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0844× (z -11.0) |
| [[J82 (line)]] | alt | 4.60 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0685× (z -10.3) |
| [[A-172 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5R1]] | +0.68 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[HDAC11]] | +0.66 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[CARMIL2]] | +0.61 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[ZDHHC18]] | +0.60 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[FKBP1B]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[GIPC1]] | +0.60 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[MOCS1]] | +0.59 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[FAM241B]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[KCTD21]] | +0.59 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[FSD1]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[OSBPL9]] | +0.58 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[TBCE]] | +0.57 | +0.47 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS1-AS1]] | -0.59 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[ANKRD17-DT]] | -0.54 | -0.31 / -0.29 | both halves | 2e-04 |  |
| [[CRPPA]] | -0.53 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[CLOCK]] | -0.52 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[RFX3]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[NQO1]] | -0.52 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[LINC01004]] | -0.51 | -0.23 / -0.31 | both halves | 5e-04 |  |
| [[CBR4]] | -0.51 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[NAALADL2]] | -0.51 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[GABPB1-AS1]] | -0.51 | -0.32 / -0.26 | both halves | 4e-04 |  |
| [[C5orf15]] | -0.51 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[IGF2BP3]] | -0.51 | -0.32 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ETNK2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CERS4]] | C | CERS4 activity raises ETNK2's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 2.47× lower at baseline in the lines without CERS4 | 0.062 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10; co-absent with the target |
| [[ANKRD6]] | C | ANKRD6 activity raises ETNK2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.32× lower at baseline in the lines without ANKRD6 | 0.074 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJB1]] | B | ETNK2 activity raises DNAJB1's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without ETNK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[HDAC11]] | B | ETNK2 activity raises HDAC11's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without ETNK2 | 0.014 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[SHROOM2]] | B | ETNK2 activity raises SHROOM2's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 2.50× lower at baseline in the lines without ETNK2 | 0.051 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[SNX15]] | B | ETNK2 activity raises SNX15's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.25× lower at baseline in the lines without ETNK2 | 0.067 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[EPHA10]] | B | ETNK2 activity raises EPHA10's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without ETNK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[FKBP1B]] | B | ETNK2 activity raises FKBP1B's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without ETNK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[FXYD6]] | B | ETNK2 activity raises FXYD6's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without ETNK2 | 0.099 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[SRRM3]] | B | ETNK2 activity raises SRRM3's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without ETNK2 | 0.099 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[ANKRD6]] | C | ETNK2 activity raises ANKRD6's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 3.79× lower at baseline in the lines without ETNK2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.6, 3.6); signed map (-39.6, -5.3). **Vector** length 47.4, 7.40% of its response variance represented; |z| ≥ 3 in 627 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.7 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +1.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ethanolamine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,131,062-204,152,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10761, EKI2 |
| Gene groups (HGNC) | Ethanolamine kinase family |
| Reactome | 4 pathways, smallest: Synthesis of PE; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVF9](https://www.uniprot.org/uniprotkb/Q9NVF9) (Ethanolamine kinase 2):

> Catalyzes the ATP-dependent phosphorylation of ethanolamine to phosphoethanolamine (By similarity). Highly specific for ethanolamine phosphorylation and does not exhibit choline kinase activity (By similarity).

**Summary**, from NCBI Gene [55224](https://www.ncbi.nlm.nih.gov/gene/55224):

> The protein encoded by this gene is a member of choline/ethanolamine kinase family which catalyzes the first step of phosphatidylethanolamine (PtdEtn) biosynthesis via the cytidine diphosphate (CDP) ethanolamine pathway. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:25575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25575) · Entrez [55224](https://www.ncbi.nlm.nih.gov/gene/55224) · UniProt [Q9NVF9](https://www.uniprot.org/uniprotkb/Q9NVF9) · Ensembl [ENSG00000143845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143845)

## Data

Gene col 6813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6813); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6813]; `tensor/DDL_lfc|DDL_z.npy` [6813]; `embed/gene_vectors.npy` [6813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6813 or target_col == 6813). Every well: [[ETNK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETNK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
