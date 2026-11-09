---
symbol: "AK7"
type: "gene"
col: 6372
ensembl_id: "ENSG00000140057"
name: "adenylate kinase 7"
location: "14q32.2"
module: 21
arm: "+"
pooled_cpm: 5.47
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 26
n_dd_up_clean: 27
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# AK7

*adenylate kinase 7* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.63× (z +15.0, q 0e+00, up in 30 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.344× (z -11.7, q 5e-29, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THBS3-AS1]] (+0.54, fdr 1e-05), [[MUC1]] (+0.52, fdr 3e-05), [[KCNQ1]] (+0.52, fdr 1e-05); moves opposite to [[ABCC10]] (-0.51, fdr 2e-04), [[EEFSEC]] (-0.51, fdr 3e-05), [[INTS15]] (-0.50, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +15.0 | 0e+00 | 30/37 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +9.2 | 1e-17 | 32/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +8.5 | 5e-15 | 29/45 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +8.1 | 6e-14 | 8/21 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +7.3 | 3e-11 | 3/6 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +6.9 | 6e-10 | 26/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +6.6 | 3e-09 | 24/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +5.9 | 3e-07 | 15/33 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.70×** | +5.6 | 1e-06 | 12/30 (NCI-H460, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.61×** | +5.5 | 2e-06 | 12/40 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 8e-06 | 13/42 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.1 | 2e-05 | 13/43 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.55×** | +4.8 | 7e-05 | 10/41 (A-427, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +4.4 | 5e-04 | 13/37 (NCI-H23, A-427, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.52×** | +4.3 | 6e-04 | 11/41 (AsPC-1, C-33 A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.004 | 12/35 (LS 180, C-33 A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.005 | 10/42 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.005 | 13/44 (NCI-H23, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.344×** | -11.7 | 5e-29 | 33/45 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.378×** | -10.7 | 3e-24 | 26/33 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.389×** | -10.4 | 5e-23 | 30/42 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.485×** | -8.0 | 2e-13 | 23/40 (SHP-77, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.504×** | -7.5 | 5e-12 | 22/43 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.526×** | -6.8 | 1e-09 | 21/41 (KATO III, PANC-1, …) | two highest doses | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.681×** | -6.0 | 2e-07 | 17/42 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.394×** | -5.4 | 6e-06 | 18/34 (A549, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.621×** | -5.2 | 9e-06 | 18/45 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.610×** | -5.2 | 9e-06 | 17/27 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.654×** | -4.7 | 2e-04 | 15/36 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.677×** | -4.3 | 8e-04 | 16/34 (KATO III, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.686×** | -4.1 | 0.002 | 13/45 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.699×** | -3.9 | 0.003 | 15/40 (MIA PaCa-2, KATO III, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.714×** | -3.7 | 0.008 | 10/42 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.727×** | -3.5 | 0.015 | 12/44 (SW480, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.728×** | -3.5 | 0.015 | 7/45 (NCI-H1573, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.558×** | -3.4 | 0.023 | 11/40 (COLO 205, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.3 | 0.027 | 13/41 (A-427, HCT15, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.046 | 5/44 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 19.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -10.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.8) |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -10.4) |
| [[SW480 (line)]] | alt | 6.29 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -10.3) |
| [[LoVo (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0400× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 6.17 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.0682× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 2.31 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +9.9) | [[Isocorydine (drug)]] 0.5 µM 0.0751× (z -9.7) |
| [[A549 (line)]] | wt | 8.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[COLO 205 (line)]] | alt | 9.25 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0947× (z -9.2) |
| [[HCT15 (line)]] | alt | 6.42 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0512× (z -9.0) |
| [[HOP62 (line)]] | alt | 6.57 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.112× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~84% of this change |
| [[PANC-1 (line)]] | alt | 3.69 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0981× (z -9.7) |
| [[A-172 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.821 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THBS3-AS1]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MUC1]] | +0.52 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[KCNQ1]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[OLMALINC]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LINC02580]] | +0.51 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PNCK]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PRRT1]] | +0.50 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[FXYD2]] | +0.50 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[NME9]] | +0.49 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ALDH2]] | +0.48 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[PRMT5-DT]] | +0.48 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[CDHR2]] | +0.48 | +0.45 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC10]] | -0.51 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[EEFSEC]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[INTS15]] | -0.50 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[RSC1A1]] | -0.48 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[DCTD]] | -0.47 | -0.49 / -0.49 | both halves | 1e-05 | pathway: Interconversion of nucleotide di- and triphosphates |
| [[MTG1]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MRPL15]] | -0.46 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[ARHGDIA]] | -0.44 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[NIP7]] | -0.44 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[FEZ2]] | -0.43 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[HUS1]] | -0.42 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[MIOS]] | -0.42 | -0.13 / -0.45 | ⚠ not reproduced | 0.002 |  |
| [[ZNF696]] | -0.42 | -0.29 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AK7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CACNA1D]] | B | CACNA1D activity raises AK7's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 1.49× lower at baseline in the lines without CACNA1D | 0.074 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.402). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.8, 48.1); signed map (54.8, -2.9). **Vector** length 56.5, 8.41% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | -0.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -6.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:96,392,128-96,489,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32864, FAP75, CFAP75 |
| Gene groups (HGNC) | Adenylate kinases; Cilia and flagella associated |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M32](https://www.uniprot.org/uniprotkb/Q96M32) (Adenylate kinase 7):

> Nucleoside monophosphate (NMP) kinase that catalyzes the reversible transfer of the terminal phosphate group between nucleoside triphosphates and monophosphates. Has highest activity toward AMP, and weaker activity toward dAMP, CMP and dCMP. Also displays broad nucleoside diphosphate kinase activity. Involved in maintaining ciliary structure and function.

**Summary**, from NCBI Gene [122481](https://www.ncbi.nlm.nih.gov/gene/122481):

> This gene encodes a member of the adenylate kinase family of enzymes. The encoded enzyme is a phosphotransferase that catalyzes the reversible phosphorylation of adenine nucleotides. This enzyme plays a role in energy homeostasis of the cell. Alternative splicing results in multiple transcript variants. Mutations in the mouse gene are associated with primary ciliary dyskinesia. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:20091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20091) · Entrez [122481](https://www.ncbi.nlm.nih.gov/gene/122481) · UniProt [Q96M32](https://www.uniprot.org/uniprotkb/Q96M32) · Ensembl [ENSG00000140057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140057)

## Data

Gene col 6372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6372); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6372]; `tensor/DDL_lfc|DDL_z.npy` [6372]; `embed/gene_vectors.npy` [6372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6372 or target_col == 6372). Every well: [[AK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
