---
symbol: "MEX3C"
type: "gene"
col: 10737
ensembl_id: "ENSG00000176624"
name: "mex-3 RNA binding family member C"
location: "18q21.2"
module: 95
arm: "+"
pooled_cpm: 32.08
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# MEX3C

*mex-3 RNA binding family member C* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +17.8, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.530× (z -14.3, q 8e-44, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00938]] (+0.58, fdr 4e-05), [[TRIM8]] (+0.58, fdr 1e-05), [[FAM120AOS]] (+0.56, fdr 9e-05); moves opposite to [[CDIN1]] (-0.57, fdr 1e-05), [[HERC2P2]] (-0.56, fdr 5e-05), [[ERI3]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +17.8 | 0e+00 | 43/48 (NCI-H2030, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.76×** | +15.6 | 0e+00 | 45/48 (C32, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.56×** | +14.1 | 1e-42 | 34/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +12.4 | 3e-33 | 39/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +9.9 | 8e-21 | 31/48 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +8.5 | 1e-15 | 30/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.1 | 3e-14 | 29/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +7.5 | 6e-12 | 26/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +7.0 | 1e-10 | 26/47 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.5 | 3e-06 | 22/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.28×** | +5.3 | 5e-06 | 18/48 (NCI-H1573, SNU-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.20×** | +4.1 | 0.002 | 8/47 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.016 | 11/47 (NCI-H460, SW480, …) | two highest doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.016 | 12/42 (Panc 03.27, SHP-77, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.022 | 12/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.031 | 10/47 (LS 180, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.083 | 4/48 (A498, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10737.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.530×** | -14.3 | 8e-44 | 38/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.576×** | -12.5 | 4e-33 | 36/48 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.632×** | -10.3 | 1e-22 | 33/48 (NCI-H2347, BT-474, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.762×** | -6.1 | 1e-07 | 25/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.799×** | -5.1 | 5e-05 | 22/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -4.8 | 1e-04 | 15/48 (NCI-H2347, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.816×** | -4.6 | 3e-04 | 18/48 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.810×** | -4.6 | 3e-04 | 18/39 (SK-MEL-2, H4, …) | top dose only | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.827×** | -4.1 | 0.002 | 15/47 (SK-MEL-2, C32, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.8 | 0.007 | 15/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.842× | -3.7 | 0.013 | 18/48 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.852× | -3.6 | 0.014 | 10/48 (NCI-H2347, A-427, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.2 | 0.071 | 9/48 (SHP-77, HT-29, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.874× | -3.1 | 0.072 | 8/48 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 41.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.4× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 42.5 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.364× (z -12.2) |
| [[BT-474 (line)]] | alt | 39.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -15.4) |
| [[HS-578T (line)]] | alt | 53.2 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0929× (z -12.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -10.7) |
| [[LoVo (line)]] | wt | 21.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 29.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 44.0 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.03× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.451× (z -9.3) |
| [[SW480 (line)]] | alt | 25.8 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.53× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.395× (z -10.0) |
| [[C-33 A (line)]] | alt | 49.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.32× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 29.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 31.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 19.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 56.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.208× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 42.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.9) | — |
| [[A498 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 50.2 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.149× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +12.8) | — |
| [[H4 (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.135× (z -9.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 1 | — | [[AZD1390 (drug)]] 5 µM 0.0498× (z -9.5) |
| [[J82 (line)]] | alt | 32.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[KATO III (line)]] | alt | 28.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.418× (z -8.6) |
| [[RKO (line)]] | wt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00938]] | +0.58 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[TRIM8]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 | same gene group |
| [[FAM120AOS]] | +0.56 | +0.41 / +0.36 | both halves | 9e-05 |  |
| [[EP300]] | +0.55 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[ZEB1-AS1]] | +0.55 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[FBXO48]] | +0.55 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[SP3]] | +0.55 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[CGGBP1]] | +0.54 | +0.39 / +0.40 | both halves | 6e-05 |  |
| [[NIPBL-DT]] | +0.54 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[MALINC1]] | +0.54 | +0.37 / +0.32 | both halves | 2e-04 |  |
| [[ZBED5]] | +0.53 | +0.32 / +0.39 | both halves | 2e-04 |  |
| [[ZBED5-AS1]] | +0.53 | +0.33 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDIN1]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[HERC2P2]] | -0.56 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ERI3]] | -0.54 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[ARHGAP8]] | -0.54 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[CAMK2G]] | -0.53 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DFFA]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SPIDR]] | -0.52 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TMEM241]] | -0.52 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[TMEM161A]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[RNF216]] | -0.51 | -0.44 / -0.32 | both halves | 2e-04 | same gene group |
| [[HERC2]] | -0.50 | -0.50 / -0.34 | both halves | 1e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PWWP3A]] | -0.50 | -0.47 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MEX3C's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (14.5, 9.0); signed map (19.5, -8.8). **Vector** length 92.0, 20.2% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.3 | +17.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.4 | +14.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.1 | +1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -6.2 | -4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.3 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.0 | -14.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -12.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | mex-3 RNA binding family member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:51,174,550-51,218,333 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38871, RNF194; previously RKHD2 |
| Gene groups (HGNC) | Ring finger proteins; Mex-3 RNA binding family |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5U5Q3](https://www.uniprot.org/uniprotkb/Q5U5Q3) (RNA-binding E3 ubiquitin-protein ligase MEX3C):

> E3 ubiquitin ligase responsible for the post-transcriptional regulation of common HLA-A allotypes. Binds to the 3' UTR of HLA-A2 mRNA, and regulates its levels by promoting mRNA decay. RNA binding is sufficient to prevent translation, but ubiquitin ligase activity is required for mRNA degradation. Positively regulates RIGI-mediated antiviral innate immunity. Mechanistically, mediates 'Lys-63'-linked polyubiquitination of the tandem CARD region of RIGI, a modification required for downstream …

**Summary**, from NCBI Gene [51320](https://www.ncbi.nlm.nih.gov/gene/51320):

> This gene encodes a member of a family of proteins with two K homology (KH) RNA-binding domains and a C-terminal RING-finger domain. The protein interacts with mRNA via the KH domains, and the protein shuttles between the nucleus and cytoplasm. Polymorphisms in this gene may contribute to hypertension. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:28040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28040) · Entrez [51320](https://www.ncbi.nlm.nih.gov/gene/51320) · UniProt [Q5U5Q3](https://www.uniprot.org/uniprotkb/Q5U5Q3) · Ensembl [ENSG00000176624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176624)

## Data

Gene col 10737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10737); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10737]; `tensor/DDL_lfc|DDL_z.npy` [10737]; `embed/gene_vectors.npy` [10737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10737 or target_col == 10737). Every well: [[MEX3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEX3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
