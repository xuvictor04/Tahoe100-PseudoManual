---
symbol: "CUTALP"
type: "gene"
col: 13553
ensembl_id: "ENSG00000226752"
name: "cutA divalent cation tolerance like, pseudogene"
location: "9q33.2"
module: 10
arm: "+"
pooled_cpm: 27.12
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CUTALP

*cutA divalent cation tolerance like, pseudogene* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.35× (z +10.7, q 5e-24, up in 29 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.44× (z +6.7, q 2e-09, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.526× (z -8.4, q 4e-14, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00174]] (+0.70, fdr 7e-06), [[RBM39]] (+0.68, fdr 1e-05), [[FAM227B]] (+0.68, fdr 7e-06); moves opposite to [[NTAQ1]] (-0.59, fdr 1e-05), [[BRI3BP]] (-0.58, fdr 1e-05), [[SNHG30]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PIK3CA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.7 | 5e-24 | 29/36 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +8.6 | 2e-15 | 28/39 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +8.6 | 2e-15 | 31/46 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +6.7 | 2e-09 | 25/47 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.43×** | +4.7 | 4e-04 | 25/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.6 | 4e-04 | 20/48 (Hs 766T, SW480, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.007 | 17/47 (HOP62, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.013 | 14/48 (RKO, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.014 | 19/48 (HEC-1-A, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.015 | 18/47 (A498, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.024 | 20/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.034 | 10/46 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.057 | 19/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.057 | 18/47 (KATO III, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.070 | 17/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.071 | 13/47 (LoVo, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.526×** | -8.4 | 4e-14 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.535×** | -8.1 | 1e-13 | 35/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.549×** | -7.8 | 1e-12 | 32/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.561×** | -7.5 | 8e-12 | 31/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.582×** | -7.0 | 2e-10 | 35/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.630×** | -6.0 | 2e-07 | 32/47 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.639×** | -5.5 | 3e-06 | 29/48 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.673×** | -5.1 | 2e-05 | 26/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -4.8 | 1e-04 | 23/47 (A-427, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -4.4 | 7e-04 | 24/47 (SW480, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.555×** | -3.9 | 0.006 | 20/41 (Panc 03.27, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.755×** | -3.6 | 0.012 | 21/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.574×** | -3.6 | 0.012 | 20/48 (SK-MEL-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.667×** | -3.6 | 0.015 | 12/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.620×** | -3.1 | 0.063 | 15/47 (Hs 766T, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.0 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -12.0) |
| [[PANC-1 (line)]] | alt | 18.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.281× (z -9.9) |
| [[LoVo (line)]] | wt | 45.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.17× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.331× (z -8.7) |
| [[SHP-77 (line)]] | alt | 45.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.10× (z +12.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.25× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 9.87 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.88× (z +8.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 61.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -9.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.278× (z -9.3) |
| [[HOP62 (line)]] | alt | 17.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.90× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.2) | — |
| [[A-427 (line)]] | wt | 31.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.296× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0921× (z -10.7) |
| [[Hs 766T (line)]] | wt | 54.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -9.0) |
| [[J82 (line)]] | alt | 40.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.324× (z -9.6) |
| [[KATO III (line)]] | alt | 68.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.315× (z -9.5) |
| [[LS 180 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.63× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.6) |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Raltitrexed (drug)]] 5 µM 0.197× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 23.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.90× (z +10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0780× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.30× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.109× (z -8.5) ⚠ toxic; unreliable plate only |
| [[A549 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00174]] | +0.70 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[RBM39]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[FAM227B]] | +0.68 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[BRAF]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ING3]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[CHD2]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZMAT1]] | +0.65 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[COQ5]] | +0.64 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[MTMR3]] | +0.64 | +0.36 / +0.66 | both halves | 9e-05 |  |
| [[TCEANC]] | +0.64 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ETFRF1]] | +0.64 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[LINC02340]] | +0.63 | +0.73 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAQ1]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[BRI3BP]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CPSF4]] | -0.57 | -0.67 / -0.39 | both halves | 6e-05 |  |
| [[PAQR4]] | -0.56 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[HACD3]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[POP1]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.56 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[MAD1L1]] | -0.55 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[HSPA8]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[KATNB1]] | -0.54 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[C1orf216]] | -0.54 | -0.60 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CA]] | B | PIK3CA activity lowers CUTALP's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PSMB5]] | B | PSMB5 activity raises CUTALP's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-25.6, 13.5); signed map (7.9, -17.6). **Vector** length 96.8, 23.9% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +8.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -5.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.4 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cutA divalent cation tolerance like, pseudogene |
| Locus type | pseudogene |
| Location | 9q33.2 — chr9:120,847,294-120,851,339 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ; previously PSMD5-AS1 |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27367) · Entrez [253039](https://www.ncbi.nlm.nih.gov/gene/253039) · Ensembl [ENSG00000226752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226752)

## Data

Gene col 13553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13553); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13553]; `tensor/DDL_lfc|DDL_z.npy` [13553]; `embed/gene_vectors.npy` [13553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13553 or target_col == 13553). Every well: [[CUTALP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUTALP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
