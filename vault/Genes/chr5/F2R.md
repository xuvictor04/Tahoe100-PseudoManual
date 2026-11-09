---
symbol: "F2R"
type: "gene"
col: 11167
ensembl_id: "ENSG00000181104"
name: "coagulation factor II thrombin receptor"
location: "5q13.3"
module: 78
arm: "+"
pooled_cpm: 21.77
n_lines_expressing: 38
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 12
direction_downstream: 3
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# F2R

*coagulation factor II thrombin receptor* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.08× (z +12.4, q 2e-32, up in 23 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +5.6, q 3e-06, up in 20 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.262× (z -19.9, q 0e+00, down in 32 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFRP1]] (+0.66, fdr 1e-05), [[NES]] (+0.66, fdr 7e-06), [[FKBP1A]] (+0.65, fdr 1e-05); moves opposite to [[FBXO6]] (-0.48, fdr 9e-05), [[HOMEZ]] (-0.48, fdr 9e-05), [[SELENOM]] (-0.47, fdr 4e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[FHL1]] → it (grade B ⚠); 3 go from it, the strongest it → [[PPFIBP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.08×** | +12.4 | 2e-32 | 23/28 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +12.3 | 2e-32 | 20/25 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.7 | 2e-06 | 17/26 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.6 | 3e-06 | 20/36 (A-427, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 5e-04 | 15/36 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +4.5 | 6e-04 | 19/36 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.002 | 15/36 (C32, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.41×** | +3.8 | 0.011 | 11/36 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.40×** | +3.7 | 0.015 | 12/36 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.015 | 12/36 (C-33 A, A549, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.015 | 12/36 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.059 | 9/36 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.095 | 7/36 (HOP62, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11167.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.262×** | -19.9 | 0e+00 | 32/35 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -9.6 | 1e-19 | 28/36 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.432×** | -9.2 | 7e-18 | 27/34 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.460×** | -8.0 | 1e-13 | 31/35 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.493×** | -7.7 | 1e-12 | 26/36 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.493×** | -7.5 | 8e-12 | 24/35 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.545×** | -6.4 | 1e-08 | 24/35 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.584×** | -5.9 | 3e-07 | 24/35 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.593×** | -5.7 | 6e-07 | 22/36 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.669×** | -4.5 | 4e-04 | 19/36 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.763×** | -4.0 | 0.003 | 16/36 (SK-MEL-2, A549, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.750×** | -3.8 | 0.006 | 14/36 (MIA PaCa-2, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -3.6 | 0.015 | 15/36 (MIA PaCa-2, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.731×** | -3.4 | 0.025 | 12/36 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.734×** | -3.4 | 0.027 | 15/36 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.641×** | -3.2 | 0.041 | 11/33 (RPMI-7951, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 171 | 0 | 18 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0835× (z -22.1) |
| [[PANC-1 (line)]] | alt | 57.9 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0649× (z -30.0) |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -15.0) |
| [[RPMI-7951 (line)]] | alt | 67.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -18.8) |
| [[C32 (line)]] | wt | 16.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.4× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 22.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -14.7) |
| [[HOP62 (line)]] | alt | 35.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -20.3) |
| [[hTERT-HPNE (line)]] | wt | 59.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0729× (z -13.8) |
| [[J82 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.0558× (z -12.7) |
| [[SNU-423 (line)]] | alt | 97.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -17.5) |
| [[A-172 (line)]] | wt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -8.5) |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -9.1) |
| [[Hs 766T (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.5) |
| [[LoVo (line)]] | wt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 7.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0393× (z -18.6) |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.5) |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.99 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFRP1]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[NES]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[FKBP1A]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[EHD3]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DKK3]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ITGB1]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FHL1]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[DNMBP]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[LDOC1]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[PCDHGC3]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[WWTR1]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[NT5E]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO6]] | -0.48 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[HOMEZ]] | -0.48 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[SELENOM]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[NDUFA6]] | -0.47 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[SNHG32]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[GSDMD]] | -0.47 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[FNBP4]] | -0.46 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[ZCCHC8]] | -0.46 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[NOL3]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[C11orf52]] | -0.46 | -0.42 / -0.23 | both halves | 5e-04 |  |
| [[SNHG12]] | -0.46 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[CEBPD]] | -0.46 | -0.47 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHL1]] | B | FHL1 activity raises F2R's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 3.27× lower at baseline in the lines without FHL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[VASH1]] | B | VASH1 activity raises F2R's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without VASH1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[SCARA3]] | B | SCARA3 activity raises F2R's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without SCARA3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[SELENOM]] | B | SELENOM activity raises F2R's level | lines that do not express SELENOM (14) vs lines expressing it (36) | 1.99× lower at baseline in the lines without SELENOM | 0.027 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S |
| [[NT5E]] | B | NT5E activity raises F2R's level | lines that do not express NT5E (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without NT5E | 0.033 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[DKK3]] | B | DKK3 activity raises F2R's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.67× lower at baseline in the lines without DKK3 | 0.035 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[KDF1]] | B | KDF1 activity lowers F2R's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 2.88× higher at baseline in the lines without KDF1 | 0.056 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[COL4A2]] | B | COL4A2 activity raises F2R's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 3.10× lower at baseline in the lines without COL4A2 | 0.079 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1 |
| [[C11orf52]] | B | C11orf52 activity lowers F2R's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.31× higher at baseline in the lines without C11orf52 | 0.082 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[PRSS23-AS1]] | B | PRSS23-AS1 activity raises F2R's level | lines that do not express PRSS23-AS1 (10) vs lines expressing it (40) | 1.62× lower at baseline in the lines without PRSS23-AS1 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[F2RL2]] | B | F2RL2 activity strengthens F2R's drug response | lines that do not express F2RL2 (21) vs lines expressing it (15) | the lines without F2RL2 respond 0.58× as strongly (z diff +1.83); strongest at Harringtonine 5 µM: 0.62x vs 0.31x (z diff +3.4) | 0.090 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA; target measured in part of the lines; artifact flags |
| [[RNF182]] | C | RNF182 activity raises F2R's level | lines that do not express RNF182 (22) vs lines expressing it (28) | 4.25× lower at baseline in the lines without RNF182 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTX3, FZD8, ENSG00000230615; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPFIBP1]] | B | F2R activity raises PPFIBP1's level | lines that do not express F2R (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without F2R | 0.060 | ⚠ within organs, on part of the lines; also absent: FGF2, LHFPL6, LGALS1 |
| [[C11orf52]] | B | F2R activity lowers C11orf52's level | lines that do not express F2R (12) vs lines expressing it (38) | 2.40× higher at baseline in the lines without F2R | 0.086 | ⚠ within organs, on part of the lines; also absent: FGF2, LHFPL6, LGALS1 |
| [[RNF182]] | C | F2R activity raises RNF182's level | lines that do not express F2R (12) vs lines expressing it (38) | 3.61× lower at baseline in the lines without F2R | 0.097 | ⚠ within organs, on part of the lines; also absent: FGF2, LHFPL6, LGALS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 10.8); signed map (22.2, 41.7). **Vector** length 94.9, 24.1% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +12.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.1 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -19.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | coagulation factor II thrombin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:76,716,126-76,735,770 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TR, CF2R, PAR1, PAR-1 |
| Gene groups (HGNC) | F2R receptors |
| Hallmark sets | ALLOGRAFT_REJECTION, APOPTOSIS, P53_PATHWAY |
| Reactome | 11 pathways, smallest: Thrombin signalling through proteinase activated receptors (PARs); Regulation of clotting cascade; Coagulation pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P25116](https://www.uniprot.org/uniprotkb/P25116) (Proteinase-activated receptor 1):

> High affinity receptor that binds the activated thrombin, leading to calcium release from intracellular stores. The thrombin-activated receptor signaling pathway is mediated through PTX-insensitive G proteins, activation of phospholipase C resulting in the production of 1D-myo-inositol 1,4,5-trisphosphate (InsP3) which binds to InsP3 receptors causing calcium release from the stores (By similarity). In astrocytes, the calcium released into the cytosol allows the Ca(2+)-dependent release of …

**Summary**, from NCBI Gene [2149](https://www.ncbi.nlm.nih.gov/gene/2149):

> Coagulation factor II receptor is a 7-transmembrane receptor involved in the regulation of thrombotic response. Proteolytic cleavage leads to the activation of the receptor. F2R is a G-protein coupled receptor family member. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:3537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3537) · Entrez [2149](https://www.ncbi.nlm.nih.gov/gene/2149) · UniProt [P25116](https://www.uniprot.org/uniprotkb/P25116) · Ensembl [ENSG00000181104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181104)

## Data

Gene col 11167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11167); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11167]; `tensor/DDL_lfc|DDL_z.npy` [11167]; `embed/gene_vectors.npy` [11167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11167 or target_col == 11167). Every well: [[F2R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/F2R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
