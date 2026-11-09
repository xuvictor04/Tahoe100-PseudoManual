---
symbol: "PCAT7"
type: "gene"
col: 13815
ensembl_id: "ENSG00000231806"
name: "prostate cancer associated transcript 7"
location: "9q22.32"
module: 187
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 38
n_dd_up: 27
n_dd_down: 15
n_dd_up_clean: 22
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# PCAT7

*prostate cancer associated transcript 7* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.79× (z +22.1, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.484× (z -8.6, q 6e-15, down in 26 of 36 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.506× (z -8.0, q 3e-13, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC2]] (+0.58, fdr 1e-05), [[EAPP]] (+0.58, fdr 1e-05), [[FBXO8]] (+0.57, fdr 2e-05); moves opposite to [[BRI3BP]] (-0.54, fdr 1e-04), [[GMDS]] (-0.52, fdr 1e-04), [[LMBR1]] (-0.52, fdr 1e-04).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[BTN2A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.79×** | +22.1 | 0e+00 | 29/32 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.76×** | +11.9 | 2e-30 | 30/36 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +10.8 | 5e-25 | 17/31 (C-33 A, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +9.7 | 4e-20 | 28/36 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +7.8 | 9e-13 | 22/36 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.4 | 1e-08 | 15/36 (J82, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.46×** | +6.3 | 2e-08 | 20/36 (A549, C32, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +5.8 | 4e-07 | 18/34 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +5.3 | 7e-06 | 19/36 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 2e-05 | 13/33 (C-33 A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +4.5 | 4e-04 | 6/36 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.3 | 9e-04 | 10/25 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.2 | 1e-03 | 11/35 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.001 | 11/32 (HEC-1-A, C-33 A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.002 | 6/33 (HEC-1-A, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.002 | 9/33 (KATO III, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.002 | 8/36 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.484×** | -8.6 | 6e-15 | 26/36 (AN3 CA, SHP-77, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -8.0 | 3e-13 | 22/36 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -6.7 | 3e-09 | 23/36 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -6.0 | 2e-07 | 17/31 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.648×** | -5.1 | 4e-05 | 16/36 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.666×** | -4.8 | 2e-04 | 15/36 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.446×** | -4.8 | 2e-04 | 15/34 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.575×** | -4.7 | 2e-04 | 16/36 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.677×** | -4.3 | 9e-04 | 16/34 (SNU-1, NCI-H1573, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.700×** | -4.2 | 0.001 | 15/36 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.491×** | -4.2 | 0.001 | 12/32 (LoVo, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -4.1 | 0.002 | 12/27 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.003 | 9/36 (HT-29, NCI-H661, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.508×** | -4.0 | 0.003 | 14/29 (LoVo, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.555×** | -3.5 | 0.020 | 13/28 (LoVo, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 30.2 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.17× (z +25.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.317× (z -9.2) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 17.8 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +12.9) | [[venetoclax (drug)]] 5 µM 0.0608× (z -9.5) |
| [[C-33 A (line)]] | alt | 33.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +13.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -11.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 4.77 | 0 | 3 | — | [[Ranolazine (drug)]] 0.05 µM 0.0620× (z -10.6) |
| [[C32 (line)]] | wt | 9.81 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0487× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Pimozide (drug)]] 0.05 µM 0.0812× (z -10.5) |
| [[CHP-212 (line)]] | wt | 39.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +9.2) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.112× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 8.67 | 0 | 2 (1 ⚠) | — | [[Altretamine (drug)]] 5 µM 0.0537× (z -10.0) |
| [[KATO III (line)]] | alt | 18.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.40× (z +18.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.199× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 6.29 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0840× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.165× (z -9.0) |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -9.0) |
| [[A549 (line)]] | wt | 4.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0817× (z -10.0) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 8.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.96× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 4.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.95× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 8.60 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 5.40 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0693× (z -9.4) |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.176× (z -9.6) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 9.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 4.75 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0727× (z -8.5) |
| [[SW1417 (line)]] | alt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +9.3) | — |
| [[SW48 (line)]] | wt | 7.88 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0550× (z -8.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 8.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +13.0) | — |
| [[A-427 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.980 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC2]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[EAPP]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FBXO8]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[IKZF5]] | +0.56 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[SUPT7L]] | +0.54 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[CIR1]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[RBM33]] | +0.53 | +0.40 / +0.38 | both halves | 7e-05 |  |
| [[CHD6]] | +0.53 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[MPHOSPH8]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ATG2B]] | +0.52 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[PAPOLG]] | +0.52 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[HOXC6]] | +0.51 | +0.38 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRI3BP]] | -0.54 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[GMDS]] | -0.52 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[LMBR1]] | -0.52 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[PRRG1]] | -0.45 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[TRAPPC9]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[AHCY]] | -0.44 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[SCART1]] | -0.44 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[RNGTT]] | -0.44 | -0.46 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCAT7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTN2A1]] | B | PCAT7 activity lowers BTN2A1's level | lines that do not express PCAT7 (12) vs lines expressing it (38) | 1.32× higher at baseline in the lines without PCAT7 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000286850, CRACD, NFIA; maybe low, not absent |
| [[LMBR1]] | B | PCAT7 activity raises LMBR1's level | lines that do not express PCAT7 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without PCAT7 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000286850, CRACD, NFIA; maybe low, not absent |
| [[FBXO8]] | B | PCAT7 activity lowers FBXO8's level | lines that do not express PCAT7 (12) vs lines expressing it (38) | 1.32× higher at baseline in the lines without PCAT7 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000286850, CRACD, NFIA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.7, -47.1); signed map (-13.6, 6.1). **Vector** length 51.0, 7.57% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +22.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -8.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | prostate cancer associated transcript 7 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q22.32 — chr9:94,555,054-94,603,990 (+) |
| Ensembl biotype | lncRNA |
| Also known as | PCAN-R2 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48824) · Entrez [101928099](https://www.ncbi.nlm.nih.gov/gene/101928099) · Ensembl [ENSG00000231806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231806)

## Data

Gene col 13815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13815); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13815]; `tensor/DDL_lfc|DDL_z.npy` [13815]; `embed/gene_vectors.npy` [13815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13815 or target_col == 13815). Every well: [[PCAT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCAT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
