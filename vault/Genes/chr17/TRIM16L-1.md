---
symbol: "TRIM16L-1"
type: "gene"
col: 16588
ensembl_id: "ENSG00000291110"
name: ""
location: ""
module: 117
arm: "+"
pooled_cpm: 10.92
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# TRIM16L-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.30× (z +8.7, q 1e-15, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.328× (z -11.7, q 1e-28, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM16L]] (+0.81, fdr 7e-06, ⚠ same locus), [[TRIM16]] (+0.80, fdr 7e-06), [[TMEM17]] (+0.67, fdr 7e-06), [[ASF1A]] (+0.65, fdr 7e-06); moves opposite to [[ATP6AP2]] (-0.56, fdr 1e-05), [[SMARCD2]] (-0.54, fdr 3e-05), [[TPTEP2-CSNK1E]] (-0.54, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TRIM16L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.30×** | +8.7 | 1e-15 | 24/40 (HOP62, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.9 | 1e-06 | 22/43 (LS 180, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.9 | 1e-04 | 4/16 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD-7648 (drug)]] 5 µM |  | **2.18×** | +4.3 | 0.003 | 12/35 (NCI-H2030, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.015 | 14/45 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.015 | 15/43 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.7 | 0.015 | 11/32 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.45×** | +3.7 | 0.015 | 13/42 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.016 | 11/45 (NCI-H1573, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.032 | 11/44 (J82, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.056 | 15/42 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.056 | 8/43 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.2 | 0.058 | 13/31 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.058 | 7/45 (NCI-H1573, SK-MEL-2, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.058 | 7/36 (SW 900, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.067 | 11/45 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.072 | 11/45 (J82, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.089 | 18/43 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.328×** | -11.7 | 1e-28 | 39/45 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -10.1 | 1e-21 | 27/41 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.383×** | -10.0 | 2e-21 | 35/43 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.469×** | -7.9 | 3e-13 | 31/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -7.9 | 3e-13 | 31/41 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.326×** | -6.1 | 8e-08 | 25/42 (NCI-H460, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.615×** | -5.1 | 3e-05 | 20/43 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -4.9 | 7e-05 | 19/40 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.631×** | -4.8 | 9e-05 | 19/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.667×** | -4.2 | 0.001 | 17/44 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -4.0 | 0.003 | 16/34 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -3.9 | 0.004 | 17/42 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -3.8 | 0.005 | 15/41 (PANC-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.724×** | -3.4 | 0.029 | 17/44 (NCI-H460, A498, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.569×** | -3.1 | 0.078 | 7/40 (PANC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.816×** | -3.0 | 0.089 | 8/45 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.52 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.164× (z -12.0) |
| [[SHP-77 (line)]] | alt | 49.7 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0383× (z -16.6) |
| [[A498 (line)]] | wt | 44.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -10.2) |
| [[A-427 (line)]] | wt | 7.22 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -9.6) |
| [[HCT15 (line)]] | alt | 7.19 | 0 | 1 | — | [[Busulfan (drug)]] 0.5 µM 0.0647× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 5.34 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0838× (z -9.9) |
| [[HOP62 (line)]] | alt | 7.69 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +10.1) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.209× (z -8.5) |
| [[LS 180 (line)]] | wt | 5.23 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0682× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 7.34 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0853× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 22.9 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 8.60× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 23.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0505× (z -12.7) |
| [[SW480 (line)]] | alt | 5.53 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -10.6) |
| [[A-172 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM16L]] | +0.81 | +0.82 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TRIM16]] | +0.80 | +0.74 / +0.83 | both halves | 7e-06 |  |
| [[TMEM17]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ASF1A]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[RTL6]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ME1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CAPS2]] | +0.60 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NMRAL2P-1]] | +0.59 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[NFE2L2]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[USP40]] | +0.58 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ALOX12P2-1]] | +0.57 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6AP2]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CCDC168]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[RASA2]] | -0.53 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[ZNF710-AS1]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CD9]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[MXRA7]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CDK2]] | -0.52 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[SLC41A3]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ZNF250]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[CERS5]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM16L]] | B | TRIM16L activity raises TRIM16L-1's level | lines that do not express TRIM16L (8) vs lines expressing it (42) | 2.40× lower at baseline in the lines without TRIM16L | 0.023 | ⚠ within organs, on part of the lines; also absent: DSCC1, FOXP4-AS1; maybe low, not absent |
| [[L3MBTL4]] | B | L3MBTL4 activity raises TRIM16L-1's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 1.95× lower at baseline in the lines without L3MBTL4 | 0.036 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1 |
| [[LINC02328]] | B | LINC02328 activity raises TRIM16L-1's level | lines that do not express LINC02328 (14) vs lines expressing it (36) | 1.47× lower at baseline in the lines without LINC02328 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, PDE4B; maybe low, not absent |
| [[ALOX12P2-1]] | B | ALOX12P2-1 activity raises TRIM16L-1's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without ALOX12P2-1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[PIR]] | B | PIR activity raises TRIM16L-1's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without PIR | 0.068 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers TRIM16L-1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[VEGFD]] | B | VEGFD activity raises TRIM16L-1's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.61× lower at baseline in the lines without VEGFD | 0.089 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[ZNF710-AS1]] | C | ZNF710-AS1's natural level strengthens TRIM16L-1's drug response | ZNF710-AS1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.29; direction not clear | 0.038 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.9, 49.3); signed map (49.8, -10.2). **Vector** length 86.7, 18.1% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.8 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -7.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | -7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -11.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

> [!warning] No registry record
> TRIM16L-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16588); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16588]; `tensor/DDL_lfc|DDL_z.npy` [16588]; `embed/gene_vectors.npy` [16588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16588 or target_col == 16588). Every well: [[TRIM16L-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM16L-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
