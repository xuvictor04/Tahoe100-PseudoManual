---
symbol: "RGS9"
type: "gene"
col: 2937
ensembl_id: "ENSG00000108370"
name: "regulator of G protein signaling 9"
location: "17q24.1"
module: 208
arm: "+"
pooled_cpm: 7.6
n_lines_expressing: 44
n_dd_up: 20
n_dd_down: 23
n_dd_up_clean: 14
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# RGS9

*regulator of G protein signaling 9* — 17q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.84× (z +34.2, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.491× (z -10.9, q 6e-25, down in 24 of 40 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGSM1]] (+0.65, fdr 1e-05), [[FCHO1]] (+0.62, fdr 3e-05), [[TMOD1]] (+0.61, fdr 1e-05); moves opposite to [[FARS2]] (-0.61, fdr 1e-05), [[ARID1B]] (-0.59, fdr 3e-05), [[ALG8]] (-0.58, fdr 2e-05).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HYCC1]] → it (grade B ⚠); 4 go from it, the strongest it → [[KLC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.84×** | +34.2 | 0e+00 | 39/42 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.70×** | +23.7 | 0e+00 | 37/39 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.57×** | +23.3 | 0e+00 | 38/42 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.16×** | +21.9 | 0e+00 | 37/42 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.26×** | +18.1 | 0e+00 | 35/42 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.15×** | +17.6 | 0e+00 | 35/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +11.3 | 1e-27 | 8/15 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.32×** | +11.0 | 5e-26 | 31/41 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.94×** | +10.2 | 2e-22 | 24/42 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +7.7 | 1e-12 | 14/33 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.3 | 1e-08 | 11/27 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.9 | 2e-07 | 12/34 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 1e-06 | 11/41 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +5.5 | 2e-06 | 3/18 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Brivudine (drug)]] 0.5 µM |  | **1.50×** | +4.4 | 4e-04 | 10/40 (SW480, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.005 | 8/40 (NCI-H460, HOP62, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.019 | 8/38 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 5 µM |  | 1.17× | +3.4 | 0.022 | 2/42 (HOP62, RPMI-7951) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2937.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.491×** | -10.9 | 6e-25 | 24/40 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.522×** | -9.9 | 8e-21 | 27/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.530×** | -9.7 | 4e-20 | 21/39 (SNU-423, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -7.9 | 5e-13 | 19/34 (HS-578T, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -5.7 | 2e-06 | 15/39 (HOP62, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -5.5 | 4e-06 | 16/41 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.688×** | -5.4 | 5e-06 | 14/39 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.507×** | -5.1 | 3e-05 | 9/35 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -5.0 | 5e-05 | 11/28 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.726×** | -4.9 | 6e-05 | 11/42 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -4.8 | 8e-05 | 11/40 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.803×** | -4.8 | 9e-05 | 13/38 (NCI-H1792, A498, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -4.6 | 2e-04 | 12/41 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.751×** | -4.4 | 5e-04 | 11/38 (HS-578T, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.566×** | -4.2 | 8e-04 | 8/30 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -4.1 | 0.001 | 16/36 (A-427, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.799×** | -3.4 | 0.019 | 7/42 (NCI-H460, SW 1088, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.801×** | -3.4 | 0.020 | 8/42 (hTERT-HPNE, SW 1088, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.045 | 10/33 (SNU-423, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.89 | 6 | 1 | [[Tucidinostat (drug)]] 5 µM 6.27× (z +14.9) | [[Digitoxin (drug)]] 0.5 µM 0.108× (z -12.7) |
| [[HOP62 (line)]] | alt | 5.25 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.49× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 8.24 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.65× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0489× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 4.15 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.67× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 27.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.312× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 15.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.98× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 6.56 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.27× (z +10.2) | — |
| [[H4 (line)]] | wt | 5.82 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0310× (z -8.8) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 3.85 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.06× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 8.42 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.93× (z +9.9) | — |
| [[J82 (line)]] | alt | 5.23 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.08× (z +9.4) | — |
| [[KATO III (line)]] | alt | 7.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.09× (z +11.6) | — |
| [[LoVo (line)]] | wt | 4.87 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.37× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 5.86 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.53× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.57× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 4.20 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.13× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 4.30 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.91× (z +8.6) | — |
| [[A-172 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGSM1]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.62 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[TMOD1]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[F11R]] | +0.60 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[TMCC2]] | +0.60 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[SUSD4]] | +0.60 | +0.29 / +0.61 | both halves | 3e-04 |  |
| [[TSPAN33]] | +0.60 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[TNNT1]] | +0.59 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[KIF5C]] | +0.59 | +0.23 / +0.65 | both halves | 6e-04 |  |
| [[SLC17A7]] | +0.58 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[LTBP4]] | +0.58 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SYP]] | +0.58 | +0.35 / +0.60 | both halves | 1e-04 | pathway: Sensory Perception |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARS2]] | -0.61 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ARID1B]] | -0.59 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ALG8]] | -0.58 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CUL1]] | -0.58 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[EFCAB2]] | -0.57 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ZFX]] | -0.57 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ATR]] | -0.56 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TBC1D5]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[DHX37]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[EXOC4]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[UBTF]] | -0.55 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[FBXL17]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HYCC1]] | B | HYCC1 activity raises RGS9's level | lines that do not express HYCC1 (8) vs lines expressing it (42) | 2.05× lower at baseline in the lines without HYCC1 | 0.055 | ⚠ within organs, on part of the lines; also absent: FERMT2, CCDC88A, HEG1 |
| [[SH3GL3]] | B | SH3GL3 activity raises RGS9's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without SH3GL3 | 0.080 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[LMTK3]] | B | LMTK3 activity strengthens RGS9's drug response | lines that do not express LMTK3 (13) vs lines expressing it (29) | the lines without LMTK3 respond 0.73× as strongly (z diff +0.91); strongest at Belinostat 5 µM: 2.37x vs 4.00x (z diff +2.0) | 0.090 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MPP2]] | B | MPP2 activity raises RGS9's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.04× lower at baseline in the lines without MPP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLC3]] | B | RGS9 activity raises KLC3's level | lines that do not express RGS9 (6) vs lines expressing it (44) | 2.03× lower at baseline in the lines without RGS9 | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM132A, KCNC4, ECE1; maybe low, not absent |
| [[FCHO1]] | B | RGS9 activity raises FCHO1's level | lines that do not express RGS9 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without RGS9 | 0.094 | ⚠ within organs, on part of the lines; also absent: TMEM132A, KCNC4, ECE1; maybe low, not absent |
| [[HYCC1]] | B | RGS9 activity raises HYCC1's level | lines that do not express RGS9 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without RGS9 | 0.094 | ⚠ within organs, on part of the lines; also absent: TMEM132A, KCNC4, ECE1; maybe low, not absent |
| [[BMP8B]] | B | RGS9 activity raises BMP8B's level | lines that do not express RGS9 (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without RGS9 | 0.097 | ⚠ within organs, on part of the lines; also absent: TMEM132A, KCNC4, ECE1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.3, 1.4); signed map (-19.9, 27.8). **Vector** length 80.9, 15.8% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.1 | +34.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.7 | +23.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.9 | +10.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +11.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.2 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -9.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.1 — chr17:65,100,812-65,227,703 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PERRS, RGS9L, MGC26458, MGC111763 |
| Gene groups (HGNC) | Regulators of G-protein signaling; DEP domain containing |
| Reactome | 10 pathways, smallest: Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade; Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding |
| Matched by | ensembl_id |

**Function**, from UniProt [O75916](https://www.uniprot.org/uniprotkb/O75916) (Regulator of G protein signaling 9):

> GTPase-activating protein (GAP) that accelerates the intrinsic GTPase activity of activated G protein alpha subunits, thereby promoting termination of G protein-mediated signaling.; [Isoform RGS9-1]: Retina-specific GAP that forms a stable complex with GNB5 (isoform Gbeta5L) and the membrane anchor RGS9BP. Accelerates the deactivation of transducin signaling in rod and cone photoreceptors, thereby promoting termination of phototransduction and rapid recovery of the photoresponse.; [Isoform …

**Summary**, from NCBI Gene [8787](https://www.ncbi.nlm.nih.gov/gene/8787):

> This gene encodes a member of the RGS family of GTPase activating proteins that function in various signaling pathways by accelerating the deactivation of G proteins. This protein is anchored to photoreceptor membranes in retinal cells and deactivates G proteins in the rod and cone phototransduction cascades. Mutations in this gene result in bradyopsia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:10004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10004) · Entrez [8787](https://www.ncbi.nlm.nih.gov/gene/8787) · UniProt [O75916](https://www.uniprot.org/uniprotkb/O75916) · Ensembl [ENSG00000108370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108370)

## Data

Gene col 2937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2937); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2937]; `tensor/DDL_lfc|DDL_z.npy` [2937]; `embed/gene_vectors.npy` [2937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2937 or target_col == 2937). Every well: [[RGS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
