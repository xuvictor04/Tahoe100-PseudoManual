---
symbol: "MDGA1"
type: "gene"
col: 3324
ensembl_id: "ENSG00000112139"
name: "MAM domain containing glycosylphosphatidylinositol anchor 1"
location: "6p21.2"
module: 13
arm: "+"
pooled_cpm: 7.52
n_lines_expressing: 37
n_dd_up: 6
n_dd_down: 35
n_dd_up_clean: 6
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MDGA1

*MAM domain containing glycosylphosphatidylinositol anchor 1* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.82× (z +16.0, q 0e+00, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.487× (z -7.8, q 3e-12, down in 23 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTHLH]] (+0.66, fdr 7e-06), [[STK10]] (+0.61, fdr 1e-05), [[FMNL1-DT]] (+0.60, fdr 1e-05); moves opposite to [[PTGES2]] (-0.56, fdr 3e-05), [[ACBD6]] (-0.52, fdr 4e-05), [[TMEM182]] (-0.52, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[STARD8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +16.0 | 0e+00 | 25/30 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +8.3 | 2e-14 | 18/29 (H4, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +5.7 | 2e-06 | 13/30 (HS-578T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.7 | 4e-04 | 14/30 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 5e-04 | 10/31 (SK-MEL-2, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.010 | 5/33 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.33× | +3.1 | 0.17 | 8/30 (SW480, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.17 | 7/33 (MIA PaCa-2, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.487×** | -7.8 | 3e-12 | 23/35 (SK-MEL-2, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.269×** | -7.5 | 2e-11 | 23/31 (NCI-H1792, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.561×** | -6.3 | 6e-08 | 18/34 (Hs 766T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.582×** | -5.9 | 6e-07 | 17/35 (SK-MEL-2, HS-578T, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.595×** | -5.6 | 2e-06 | 16/34 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.607×** | -5.4 | 5e-06 | 15/32 (NCI-H1792, MIA PaCa-2, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.615×** | -5.3 | 1e-05 | 16/34 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.408×** | -5.1 | 2e-05 | 15/30 (MIA PaCa-2, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.640×** | -4.9 | 7e-05 | 17/35 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.432×** | -4.8 | 1e-04 | 14/32 (MIA PaCa-2, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.439×** | -4.7 | 1e-04 | 16/31 (A-172, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.657×** | -4.6 | 2e-04 | 13/35 (SW480, H4, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.657×** | -4.6 | 2e-04 | 14/35 (HOP62, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.743×** | -4.6 | 2e-04 | 14/34 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.667×** | -4.4 | 4e-04 | 16/34 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.678×** | -4.2 | 8e-04 | 13/32 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.691×** | -4.0 | 0.002 | 9/31 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.503×** | -3.9 | 0.003 | 13/28 (SK-MEL-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0886× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.132× (z -10.2) |
| [[HS-578T (line)]] | alt | 17.9 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0610× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.155× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0841× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0173× (z -11.9) |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -9.1) ⚠ position not correctable |
| [[SW480 (line)]] | alt | 7.93 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +10.4) | — |
| [[A498 (line)]] | wt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +9.1) | — |
| [[A549 (line)]] | wt | 8.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0873× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 5.85 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0447× (z -9.8) |
| [[LoVo (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 4.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0853× (z -8.5) |
| [[A-172 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTHLH]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[STK10]] | +0.61 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[FMNL1-DT]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[IL1B]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SPSB1]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[GPR161]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CSMD2]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[BMAL2-AS1]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[NTNG2]] | +0.57 | +0.39 / +0.64 | both halves | 6e-05 | pathway: Post-translational modification: synthesis of GPI-anchored proteins; STRING 634 |
| [[MANCR]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[KCNC4]] | +0.56 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PECAM1]] | +0.55 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGES2]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ACBD6]] | -0.52 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[TMEM182]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[GPAM]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[MRPL42]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TRAPPC11]] | -0.50 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[UBXN2B]] | -0.50 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[ZZZ3]] | -0.50 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[COPS8]] | -0.49 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SKIC3]] | -0.49 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[TRIT1]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SSRP1]] | -0.48 | -0.31 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MDGA1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GPR161]] | B | GPR161 activity raises MDGA1's level | lines that do not express GPR161 (6) vs lines expressing it (44) | 3.51× lower at baseline in the lines without GPR161 | 0.076 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PPP2R3A, NKAIN1 |
| [[MMP1]] | B | MMP1 activity raises MDGA1's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without MMP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[STARD8]] | B | STARD8 activity raises MDGA1's level | lines that do not express STARD8 (9) vs lines expressing it (41) | 2.69× lower at baseline in the lines without STARD8 | 0.085 | ⚠ within organs, on part of the lines; also absent: ADGRG2, TMEM132B; maybe low, not absent |
| [[MANCR]] | B | MANCR activity strengthens MDGA1's drug response | lines that do not express MANCR (14) vs lines expressing it (21) | the lines without MANCR respond 0.48× as strongly (z diff +1.31); strongest at Panobinostat 5 µM: 0.74x vs 0.41x (z diff +3.3) | 0.086 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD8]] | B | MDGA1 activity raises STARD8's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without MDGA1 | 0.045 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |
| [[TRAPPC11]] | B | MDGA1 activity raises TRAPPC11's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without MDGA1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |
| [[ST6GALNAC2]] | B | MDGA1 activity raises ST6GALNAC2's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without MDGA1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |
| [[LMO2]] | B | MDGA1 activity raises LMO2's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without MDGA1 | 0.079 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |
| [[FMNL1-DT]] | B | MDGA1 activity raises FMNL1-DT's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without MDGA1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.6, -4.2); signed map (17.3, 49.5). **Vector** length 84.3, 19.1% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +16.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +8.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.9 |
| fall | [[Triamcinolone (drug)]] 0.5 µM |  | -2.7 | -4.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -5.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | MAM domain containing glycosylphosphatidylinositol anchor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:37,630,679-37,699,306 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPIM, MAMDC3 |
| Gene groups (HGNC) | I-set domain containing |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFP4](https://www.uniprot.org/uniprotkb/Q8NFP4) (MAM domain-containing glycosylphosphatidylinositol anchor protein 1):

> Plays a role in the formation or maintenance of inhibitory synapses, probably acting through the inhibition of NLGN2 activity. Is also required for proper maintenance of dendritic branching (By similarity). Negatively regulates synaptic transmission and strength at GABAergic synapses (By similarity).

**Summary**, from NCBI Gene [266727](https://www.ncbi.nlm.nih.gov/gene/266727):

> This gene encodes a glycosylphosphatidylinositol (GPI)-anchored cell surface glycoprotein that is expressed predominantly in the developing nervous system. In addition to possessing several cell adhesion molecule-like domains, the mature protein has six Ig-like domains, a single fibronectin type III domain, a MAM domain and a C-terminal GPI-anchoring site. Studies in other mammals suggest this protein plays a role in cell adhesion, migration, and axon guidance and, in the developing brain, …

**Accessions** — [HGNC:19267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19267) · Entrez [266727](https://www.ncbi.nlm.nih.gov/gene/266727) · UniProt [Q8NFP4](https://www.uniprot.org/uniprotkb/Q8NFP4) · Ensembl [ENSG00000112139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112139)

## Data

Gene col 3324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3324); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3324]; `tensor/DDL_lfc|DDL_z.npy` [3324]; `embed/gene_vectors.npy` [3324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3324 or target_col == 3324). Every well: [[MDGA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDGA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
