---
symbol: "RASSF4"
type: "gene"
col: 2857
ensembl_id: "ENSG00000107551"
name: "Ras association domain family member 4"
location: "10q11.21"
module: 103
arm: "+"
pooled_cpm: 10.3
n_lines_expressing: 39
n_dd_up: 25
n_dd_down: 20
n_dd_up_clean: 25
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 10
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# RASSF4

*Ras association domain family member 4* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.76× (z +11.7, q 9e-29, up in 28 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.284× (z -14.5, q 6e-45, down in 35 of 37 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THEMIS2]] (+0.65, fdr 1e-05), [[HOXA13]] (+0.62, fdr 1e-05), [[DEPP1]] (+0.60, fdr 3e-05, ⚠ same locus), [[FOXO6]] (+0.56, fdr 5e-05); moves opposite to [[EPM2A]] (-0.58, fdr 4e-05), [[PTPN9]] (-0.53, fdr 9e-05), [[DNAAF10]] (-0.53, fdr 2e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SMIM10]] → it (grade B ⚠); 10 go from it, the strongest it → [[STRA6LP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, none with an alert; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.76×** | +11.7 | 9e-29 | 28/37 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +9.1 | 3e-17 | 21/35 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +8.2 | 6e-14 | 23/35 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.1 | 2e-10 | 20/36 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +6.8 | 1e-09 | 19/33 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.62×** | +5.4 | 7e-06 | 14/33 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +5.3 | 7e-06 | 16/33 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.1 | 3e-05 | 16/37 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +4.7 | 2e-04 | 10/34 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.68×** | +4.3 | 0.001 | 10/33 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.001 | 10/37 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 12/37 (KATO III, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 11/33 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.003 | 11/37 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.003 | 11/37 (SW480, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.284×** | -14.5 | 6e-45 | 35/37 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.345×** | -12.3 | 4e-32 | 29/32 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.380×** | -11.2 | 1e-26 | 28/34 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.403×** | -10.5 | 2e-23 | 30/34 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -10.1 | 5e-22 | 25/34 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -8.4 | 3e-15 | 26/32 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.487×** | -8.3 | 9e-15 | 23/34 (Panc 03.27, MIA PaCa-2, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.528×** | -7.4 | 1e-11 | 23/36 (MIA PaCa-2, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.550×** | -6.6 | 2e-09 | 13/35 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -6.5 | 4e-09 | 19/33 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.601×** | -5.9 | 2e-07 | 17/37 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -4.7 | 9e-05 | 18/29 (NCI-H1792, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.664×** | -4.7 | 9e-05 | 15/34 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -4.3 | 8e-04 | 17/31 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -3.9 | 0.004 | 16/34 (SNU-423, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.721×** | -3.8 | 0.006 | 12/36 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -3.6 | 0.012 | 16/36 (PANC-1, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0832× (z -20.6) |
| [[SNU-423 (line)]] | alt | 85.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -13.2) |
| [[H4 (line)]] | wt | 26.2 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0354× (z -13.7) |
| [[HOP62 (line)]] | alt | 18.1 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.01× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.0516× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.4) |
| [[SW480 (line)]] | alt | 9.69 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0675× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -10.7) |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.309× (z -12.0) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0246× (z -18.3) |
| [[SHP-77 (line)]] | alt | 9.15 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0613× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 9.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -9.1) |
| [[HS-578T (line)]] | alt | 9.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -10.5) |
| [[HT-29 (line)]] | alt | 4.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0313× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 6.31 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0628× (z -8.9) |
| [[RKO (line)]] | wt | 7.18 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0849× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0988× (z -11.3) |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0490× (z -9.8) |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0779× (z -10.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 4.76 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0384× (z -12.1) |
| [[A-427 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEMIS2]] | +0.65 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[HOXA13]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[DEPP1]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[FOXO6]] | +0.56 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[RAB30]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SMIM10]] | +0.54 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[TCN2]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ALAD]] | +0.54 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[SMARCD3]] | +0.54 | +0.45 / +0.38 | both halves | 7e-05 |  |
| [[ZNF404]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[THAP8]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[NFIL3]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[CFD]] | +0.52 | +0.31 / +0.45 | both halves | 2e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPM2A]] | -0.58 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PTPN9]] | -0.53 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[DNAAF10]] | -0.53 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[AVEN]] | -0.52 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[GPATCH2]] | -0.51 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[E2F3]] | -0.51 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CSTF3]] | -0.51 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[PBX3]] | -0.51 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[PCBD2]] | -0.51 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[HCG18]] | -0.50 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.50 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[METTL21A]] | -0.49 | -0.31 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM10]] | B | SMIM10 activity raises RASSF4's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without SMIM10 | 0.003 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[DEPP1]] | B | DEPP1 activity raises RASSF4's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without DEPP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[ZNF883]] | B | ZNF883 activity raises RASSF4's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without ZNF883 | 0.047 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43 |
| [[STRA6LP]] | B | STRA6LP activity raises RASSF4's level | lines that do not express STRA6LP (9) vs lines expressing it (41) | 1.94× lower at baseline in the lines without STRA6LP | 0.056 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CCDC180 |
| [[LOX]] | B | LOX activity raises RASSF4's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.65× lower at baseline in the lines without LOX | 0.062 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[VSIR]] | B | VSIR activity raises RASSF4's level | lines that do not express VSIR (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without VSIR | 0.067 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers RASSF4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ZNF439]] | B | ZNF439 activity raises RASSF4's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without ZNF439 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R |
| [[MAP7]] | B | MAP7 activity lowers RASSF4's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 2.12× higher at baseline in the lines without MAP7 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[GMPR]] | B | GMPR activity raises RASSF4's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without GMPR | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STRA6LP]] | B | RASSF4 activity raises STRA6LP's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without RASSF4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[DEPP1]] | B | RASSF4 activity raises DEPP1's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 5.98× lower at baseline in the lines without RASSF4 | 0.010 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[EFNA3]] | B | RASSF4 activity lowers EFNA3's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 1.60× higher at baseline in the lines without RASSF4 | 0.051 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[ALAD]] | B | RASSF4 activity strengthens ALAD's drug response | lines that do not express RASSF4 (11) vs lines expressing it (37) | the lines without RASSF4 respond 0.85× as strongly (z diff +0.74); strongest at Panobinostat 0.5 µM: 3.20x vs 4.59x (z diff +1.8) | 0.054 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[THEMIS2]] | B | RASSF4 activity raises THEMIS2's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 2.59× lower at baseline in the lines without RASSF4 | 0.058 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[VSIR]] | B | RASSF4 activity raises VSIR's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without RASSF4 | 0.059 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[ZNF439]] | B | RASSF4 activity raises ZNF439's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without RASSF4 | 0.071 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[ZNF22]] | B | RASSF4 activity raises ZNF22's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without RASSF4 | 0.086 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[GPATCH11]] | B | RASSF4 activity weakens GPATCH11's drug response | lines that do not express RASSF4 (11) vs lines expressing it (37) | the lines without RASSF4 respond 1.19× as strongly (z diff -0.95); strongest at Homoharringtonine 5 µM: 2.18x vs 1.33x (z diff -3.6) | 0.093 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SMIM10]] | B | RASSF4 activity raises SMIM10's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without RASSF4 | 0.093 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.0, -13.9); signed map (-31.7, 28.5). **Vector** length 72.8, 14.8% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +9.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.0 | +8.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +5.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | +1.4 |
|  | [[Dihydroartemisinin (drug)]] 0.05 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Ras association domain family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:44,959,407-44,995,891 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AD037, MGC44914 |
| Gene groups (HGNC) | Ras association domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2L5](https://www.uniprot.org/uniprotkb/Q9H2L5) (Ras association domain-containing protein 4):

> Potential tumor suppressor. May act as a KRAS effector protein. May promote apoptosis and cell cycle arrest.

**Summary**, from NCBI Gene [83937](https://www.ncbi.nlm.nih.gov/gene/83937):

> The function of this gene has not yet been determined but may involve a role in tumor suppression. Alternative splicing of this gene results in several transcript variants; however, most of the variants have not been fully described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20793) · Entrez [83937](https://www.ncbi.nlm.nih.gov/gene/83937) · UniProt [Q9H2L5](https://www.uniprot.org/uniprotkb/Q9H2L5) · Ensembl [ENSG00000107551](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107551)

## Data

Gene col 2857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2857); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2857]; `tensor/DDL_lfc|DDL_z.npy` [2857]; `embed/gene_vectors.npy` [2857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2857 or target_col == 2857). Every well: [[RASSF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASSF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
