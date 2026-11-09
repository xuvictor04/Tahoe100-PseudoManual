---
symbol: "DEPTOR"
type: "gene"
col: 7918
ensembl_id: "ENSG00000155792"
name: "DEP domain containing MTOR interacting protein"
location: "8q24.12"
module: 8
arm: "+"
pooled_cpm: 10.13
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 34
n_dd_up_clean: 20
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 12
direction_downstream: 2
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DEPTOR

*DEP domain containing MTOR interacting protein* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.56× (z +15.2, q 0e+00, up in 28 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.378× (z -11.2, q 4e-26, down in 31 of 39 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.443× (z -9.0, q 8e-17, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF1A-AS1]] (+0.60, fdr 1e-05), [[SORL1]] (+0.57, fdr 1e-05), [[TNRC6B]] (+0.57, fdr 3e-05); moves opposite to [[IPO13]] (-0.52, fdr 9e-05), [[SFN]] (-0.50, fdr 2e-05), [[SVIL-AS1-1]] (-0.45, fdr 6e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[RNF128]] → it (grade B ⚠); 2 go from it, the strongest it → [[DLEU1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +15.2 | 0e+00 | 28/32 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.06×** | +12.4 | 9e-33 | 28/40 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.63×** | +10.7 | 2e-24 | 25/39 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +10.4 | 2e-23 | 27/39 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.24×** | +9.3 | 3e-18 | 22/40 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.8 | 4e-13 | 7/13 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.80×** | +6.5 | 5e-09 | 22/40 (BT-474, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.5 | 6e-09 | 18/32 (HT-29, J82, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.2 | 3e-08 | 15/33 (HT-29, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.62×** | +5.8 | 4e-07 | 10/38 (HT-29, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.7 | 5e-07 | 13/39 (LoVo, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +5.5 | 2e-06 | 19/38 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 3e-05 | 13/38 (HS-578T, SHP-77, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.48×** | +4.5 | 2e-04 | 14/39 (NCI-H2030, LS 180, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.4 | 5e-04 | 7/27 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.003 | 7/37 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.011 | 10/41 (KATO III, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.378×** | -11.2 | 4e-26 | 31/39 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.443×** | -9.0 | 8e-17 | 23/38 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -6.9 | 8e-10 | 20/33 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.556×** | -6.7 | 3e-09 | 20/38 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -6.5 | 9e-09 | 24/35 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.369×** | -6.0 | 2e-07 | 21/36 (SW48, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.600×** | -5.8 | 4e-07 | 20/38 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.700×** | -5.8 | 6e-07 | 22/39 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.392×** | -5.6 | 1e-06 | 20/34 (SHP-77, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.601×** | -5.5 | 2e-06 | 20/38 (NCI-H1792, SK-MEL-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -5.4 | 3e-06 | 17/40 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.611×** | -5.4 | 3e-06 | 22/39 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.437×** | -5.0 | 3e-05 | 20/38 (COLO 205, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.651×** | -4.9 | 4e-05 | 13/37 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.564×** | -4.7 | 1e-04 | 18/39 (SW480, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.649×** | -4.7 | 1e-04 | 16/38 (PANC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -4.4 | 4e-04 | 15/39 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 73.9 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -19.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0769× (z -15.8) |
| [[PANC-1 (line)]] | alt | 33.8 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -21.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0499× (z -20.5) |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0737× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.0443× (z -10.6) |
| [[KATO III (line)]] | alt | 27.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0916× (z -12.3) |
| [[HT-29 (line)]] | alt | 15.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0961× (z -11.2) |
| [[A-427 (line)]] | wt | 5.86 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0749× (z -10.0) |
| [[BT-474 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 4.41 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0361× (z -10.5) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 5.48 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF1A-AS1]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SORL1]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TNRC6B]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[HNMT]] | +0.52 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[PRR15-DT]] | +0.51 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[AGR3]] | +0.50 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[ACSM3]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[FAAH2]] | +0.50 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[EPCAM-DT]] | +0.49 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MAP2K6]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[RNF183]] | +0.49 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[RORC]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO13]] | -0.52 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[SFN]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[SVIL-AS1-1]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ZFP28]] | -0.44 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CC2D1B]] | -0.44 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[PCYT1A]] | -0.43 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[CFAP20DC]] | -0.42 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[YWHAH]] | -0.42 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[FAM219A]] | -0.42 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[SPEG]] | -0.41 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[LINC02377]] | -0.41 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[FAM50A]] | -0.41 | -0.30 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF128]] | B | RNF128 activity raises DEPTOR's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.77× lower at baseline in the lines without RNF128 | 0.008 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[LINC00992]] | B | LINC00992 activity raises DEPTOR's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without LINC00992 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[SORL1]] | B | SORL1 activity raises DEPTOR's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without SORL1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[ZFP28]] | B | ZFP28 activity lowers DEPTOR's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.86× higher at baseline in the lines without ZFP28 | 0.045 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises DEPTOR's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.19× lower at baseline in the lines without HNF1A-AS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[SFN]] | B | SFN activity raises DEPTOR's level | lines that do not express SFN (20) vs lines expressing it (30) | 2.16× lower at baseline in the lines without SFN | 0.069 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A |
| [[AGR3]] | B | AGR3 activity raises DEPTOR's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 2.68× lower at baseline in the lines without AGR3 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[IGFBP1]] | B | IGFBP1 activity raises DEPTOR's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.71× lower at baseline in the lines without IGFBP1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2 |
| [[TMC4]] | B | TMC4 activity raises DEPTOR's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without TMC4 | 0.085 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[RORC]] | B | RORC activity raises DEPTOR's level | lines that do not express RORC (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without RORC | 0.091 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[PRKG2-AS1]] | B | PRKG2-AS1 activity raises DEPTOR's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without PRKG2-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[PRR15L]] | B | PRR15L activity raises DEPTOR's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.33× lower at baseline in the lines without PRR15L | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLEU1]] | B | DEPTOR activity raises DLEU1's level | lines that do not express DEPTOR (6) vs lines expressing it (44) | 3.22× lower at baseline in the lines without DEPTOR | 0.057 | ⚠ within organs, on part of the lines; also absent: WWOX; maybe low, not absent |
| [[ZNRF2]] | B | DEPTOR activity raises ZNRF2's level | lines that do not express DEPTOR (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without DEPTOR | 0.061 | ⚠ within organs, on part of the lines; also absent: WWOX; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.6, 49.4); signed map (65.3, -2.1). **Vector** length 68.4, 12.3% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | -6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +5.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +4.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -11.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -6.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -5.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | DEP domain containing MTOR interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:119,873,717-120,050,918 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DEP.6, FLJ12428; previously DEPDC6 |
| Gene groups (HGNC) | PDZ domain containing; DEP domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB45](https://www.uniprot.org/uniprotkb/Q8TB45) (DEP domain-containing mTOR-interacting protein):

> Negative regulator of the mTORC1 and mTORC2 complexes: inhibits the protein kinase activity of MTOR, thereby inactivating both complexes. DEPTOR inhibits mTORC1 and mTORC2 to induce autophagy. In contrast to AKT1S1/PRAS40, only partially inhibits mTORC1 activity.

**Summary**, from NCBI Gene [64798](https://www.ncbi.nlm.nih.gov/gene/64798):

> Enables phosphatidic acid binding activity and protein serine/threonine kinase inhibitor activity. Involved in several processes, including negative regulation of TOR signaling; negative regulation of cell size; and negative regulation of protein kinase activity. Is active in lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22953) · Entrez [64798](https://www.ncbi.nlm.nih.gov/gene/64798) · UniProt [Q8TB45](https://www.uniprot.org/uniprotkb/Q8TB45) · Ensembl [ENSG00000155792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155792)

## Data

Gene col 7918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7918); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7918]; `tensor/DDL_lfc|DDL_z.npy` [7918]; `embed/gene_vectors.npy` [7918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7918 or target_col == 7918). Every well: [[DEPTOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEPTOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
