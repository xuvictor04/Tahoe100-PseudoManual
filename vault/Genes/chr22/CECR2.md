---
symbol: "CECR2"
type: "gene"
col: 1834
ensembl_id: "ENSG00000099954"
name: "CECR2 histone acetyl-lysine reader"
location: "22q11.1-q11.21"
module: 128
arm: "+"
pooled_cpm: 20.78
n_lines_expressing: 26
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 9
direction_downstream: 22
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# CECR2

*CECR2 histone acetyl-lysine reader* — 22q11.1-q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +18.4, q 0e+00, up in 10 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.671× (z -6.9, q 4e-09, down in 15 of 23 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLE2]] (+0.62, fdr 1e-05), [[GRID1]] (+0.59, fdr 3e-05), [[CHD5]] (+0.57, fdr 1e-05); moves opposite to [[TAF2]] (-0.44, fdr 5e-05), [[MPV17]] (-0.44, fdr 1e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAP3K15]] → it (grade B ⚠); 22 go from it, the strongest it → [[KIF26A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +18.4 | 0e+00 | 10/23 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +13.7 | 4e-40 | 4/19 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +13.2 | 3e-37 | 12/24 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +12.0 | 7e-31 | 2/16 (HS-578T, A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +10.9 | 2e-25 | 13/22 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +5.3 | 1e-05 | 1/17 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 0.001 | 8/23 (NCI-H460, SHP-77, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 8/22 (NCI-H460, BT-474, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.0 | 0.004 | 6/20 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.26×** | +3.8 | 0.007 | 2/22 (J82, NCI-H460) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.8 | 0.007 | 6/17 (A498, BT-474, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.6 | 0.014 | 2/22 (SHP-77, PANC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.017 | 1/22 (NCI-H2030) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.019 | 2/22 (A549, NCI-H460) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.036 | 8/22 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.2 | 0.040 | 5/24 (A-427, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.098 | 4/22 (NCI-H1573, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.671×** | -6.9 | 4e-09 | 15/23 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -6.7 | 7e-09 | 14/22 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.704×** | -5.8 | 1e-06 | 10/22 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -5.8 | 1e-06 | 15/23 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.542×** | -5.5 | 4e-06 | 15/22 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.739×** | -5.2 | 2e-05 | 11/22 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.737×** | -5.1 | 3e-05 | 12/22 (HS-578T, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.766×** | -4.6 | 3e-04 | 11/22 (A-172, MIA PaCa-2, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.601×** | -4.6 | 3e-04 | 11/20 (MIA PaCa-2, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.770×** | -4.5 | 4e-04 | 10/22 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 0.847× | -4.0 | 0.003 | 14/23 (A-427, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.821×** | -3.4 | 0.031 | 9/23 (A549, A-172, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.687×** | -3.4 | 0.031 | 15/21 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.825×** | -3.3 | 0.037 | 3/22 (BT-474, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.042 | 11/22 (LoVo, A498, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.820×** | -3.2 | 0.044 | 4/21 (A-172, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 24 (16 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0788× (z -24.3) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -20.2) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 12 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0696× (z -16.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.157× (z -11.6) |
| [[A-427 (line)]] | wt | 69.1 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -24.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[LoVo (line)]] | wt | 41.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -17.5) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 35.9 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.154× (z -12.4) |
| [[AN3 CA (line)]] | alt | 223 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -13.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 184 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -19.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 16.6 | 3 | 0 | [[Tucidinostat (drug)]] 0.5 µM 4.58× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 21.4 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0835× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 244 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0236× (z -20.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 133 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.175× (z -15.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.159× (z -10.3) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.7) ⚠ cell-cycle shift, explains ~88% of this change |
| [[PANC-1 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.79 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLE2]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GRID1]] | +0.59 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[CHD5]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PALM]] | +0.57 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[KNDC1]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CYS1]] | +0.57 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[MSI1]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MAST1]] | +0.56 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[DOCK3]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[BRSK2]] | +0.53 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[MAP6]] | +0.53 | +0.37 / +0.58 | both halves | 7e-05 |  |
| [[NOL4L]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.44 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[MPV17]] | -0.44 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K15]] | B | MAP3K15 activity raises CECR2's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 2.97× lower at baseline in the lines without MAP3K15 | 0.016 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[ARHGAP44]] | B | ARHGAP44 activity raises CECR2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 3.36× lower at baseline in the lines without ARHGAP44 | 0.064 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[CHD5]] | C | CHD5 activity raises CECR2's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 3.31× lower at baseline in the lines without CHD5 | 0.011 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[LRRN2]] | C | LRRN2 activity raises CECR2's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 3.26× lower at baseline in the lines without LRRN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL; co-absent with the target |
| [[PHF21B]] | C | PHF21B activity raises CECR2's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 3.83× lower at baseline in the lines without PHF21B | 0.025 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[PAX2]] | C | PAX2 activity raises CECR2's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 4.33× lower at baseline in the lines without PAX2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises CECR2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 3.15× lower at baseline in the lines without PDZD4 | 0.050 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |
| [[ELFN1]] | C | ELFN1 activity raises CECR2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.71× lower at baseline in the lines without ELFN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; co-absent with the target |
| [[MSI1]] | C | MSI1 activity raises CECR2's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 3.27× lower at baseline in the lines without MSI1 | 0.079 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 10, C 12. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | CECR2 activity raises KIF26A's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without CECR2 | 0.011 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[RHBDL3]] | B | CECR2 activity raises RHBDL3's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without CECR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[SMO]] | B | CECR2 activity raises SMO's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without CECR2 | 0.045 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[KNDC1]] | B | CECR2 activity raises KNDC1's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without CECR2 | 0.054 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[RASGEF1C]] | B | CECR2 activity raises RASGEF1C's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.06× lower at baseline in the lines without CECR2 | 0.056 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[CRLF1]] | B | CECR2 activity raises CRLF1's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.34× lower at baseline in the lines without CECR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[CBFA2T3]] | B | CECR2 activity raises CBFA2T3's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without CECR2 | 0.061 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[CIB2]] | B | CECR2 activity raises CIB2's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CECR2 | 0.077 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[MAPT]] | B | CECR2 activity raises MAPT's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.69× lower at baseline in the lines without CECR2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[ARHGAP44]] | B | CECR2 activity raises ARHGAP44's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without CECR2 | 0.098 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[PAX2]] | C | CECR2 activity raises PAX2's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.38× lower at baseline in the lines without CECR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |
| [[CHD5]] | C | CECR2 activity raises CHD5's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.50× lower at baseline in the lines without CECR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.6, 38.2); signed map (24.5, 24.4). **Vector** length 72.5, 19.3% of its response variance represented; |z| ≥ 3 in 641 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +4.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.5 | -4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.3 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | CECR2 histone acetyl-lysine reader |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.1-q11.21 — chr22:17,359,949-17,558,151 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1740 |
| Gene groups (HGNC) | Bromodomain containing; CERF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXF3](https://www.uniprot.org/uniprotkb/Q9BXF3) (Chromatin remodeling regulator CECR2):

> Regulatory subunit of the ATP-dependent CERF-1 and CERF-5 ISWI chromatin remodeling complexes, which form ordered nucleosome arrays on chromatin and facilitate access to DNA during DNA-templated processes such as DNA replication, transcription, and repair. The complexes do not have the ability to slide mononucleosomes to the center of a DNA template. The CERF-1 ISWI chromatin remodeling complex has a lower ATP hydrolysis rate than the CERF-5 ISWI chromatin remodeling complex. Plays a role in …

**Summary**, from NCBI Gene [27443](https://www.ncbi.nlm.nih.gov/gene/27443):

> This gene encodes a bromodomain-containing protein that is involved in chromatin remodeling, and may additionally play a role in DNA damage response. The encoded protein functions as part of an ATP-dependent complex that is involved in neurulation. This gene is a candidate gene for Cat Eye Syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:1840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1840) · Entrez [27443](https://www.ncbi.nlm.nih.gov/gene/27443) · UniProt [Q9BXF3](https://www.uniprot.org/uniprotkb/Q9BXF3) · Ensembl [ENSG00000099954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099954)

## Data

Gene col 1834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1834); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1834]; `tensor/DDL_lfc|DDL_z.npy` [1834]; `embed/gene_vectors.npy` [1834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1834 or target_col == 1834). Every well: [[CECR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CECR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
