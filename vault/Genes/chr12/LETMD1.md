---
symbol: "LETMD1"
type: "gene"
col: 566
ensembl_id: "ENSG00000050426"
name: "LETM1 domain containing 1"
location: "12q13.12"
module: 11
arm: "+"
pooled_cpm: 27.36
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# LETMD1

*LETM1 domain containing 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.29× (z +3.7, q 0.071, up in 12 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.541× (z -13.8, q 9e-41, down in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.444× (z -12.9, q 1e-35, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAAF1]] (+0.62, fdr 7e-06), [[SART3]] (+0.54, fdr 3e-05), [[TIMM9]] (+0.53, fdr 3e-05); moves opposite to [[DPYSL2]] (-0.50, fdr 5e-05), [[COL13A1]] (-0.50, fdr 3e-05), [[TMSB4X]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.071 | 12/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.071 | 17/44 (MIA PaCa-2, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.071 | 15/47 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.071 | 9/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.071 | 13/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.16× | +3.4 | 0.071 | 8/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.078 | 11/47 (PANC-1, Hs 766T, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.15× | +3.2 | 0.11 | 15/48 (NCI-H2347, AsPC-1, …) | top dose only | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.16 | 9/48 (H4, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.541×** | -13.8 | 9e-41 | 45/47 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -12.9 | 1e-35 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -10.9 | 2e-25 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -10.6 | 3e-24 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.547×** | -9.6 | 9e-20 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.401×** | -7.6 | 3e-12 | 38/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.414×** | -7.3 | 2e-11 | 35/46 (SW480, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -7.2 | 4e-11 | 32/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -5.5 | 3e-06 | 26/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.744×** | -4.7 | 2e-04 | 20/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.742×** | -4.3 | 9e-04 | 19/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.759×** | -4.0 | 0.002 | 20/41 (NCI-H23, KATO III, …) | inconsistent across doses | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -4.0 | 0.002 | 19/48 (CHP-212, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.762×** | -3.9 | 0.004 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.781×** | -3.9 | 0.004 | 19/47 (A-427, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.790×** | -3.5 | 0.014 | 16/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.791×** | -3.5 | 0.015 | 17/47 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.800×** | -3.2 | 0.038 | 12/47 (SW 900, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.3 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -16.5) |
| [[PANC-1 (line)]] | alt | 36.0 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -18.6) |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Canagliflozin (drug)]] 5 µM 0.230× (z -8.7) |
| [[J82 (line)]] | alt | 25.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -9.0) |
| [[A549 (line)]] | wt | 21.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0502× (z -15.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.382× (z -9.7) |
| [[LS 180 (line)]] | wt | 34.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 43.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 28.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -16.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 15.7 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.229× (z -8.8) |
| [[A-427 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 44.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -15.3) |
| [[HCT15 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -9.0) |
| [[KATO III (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.330× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0884× (z -13.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAAF1]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SART3]] | +0.54 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[TIMM9]] | +0.53 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[POLL]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[KIAA1143]] | +0.51 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[MRPL32]] | +0.51 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[PGAP2]] | +0.50 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[MRPL46]] | +0.50 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[HPS4]] | +0.50 | +0.33 / +0.57 | both halves | 1e-04 | STRING 436 |
| [[ATP6V0D1-DT]] | +0.49 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[OXLD1]] | +0.49 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[KAT14]] | +0.49 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL2]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[COL13A1]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TMSB4X]] | -0.49 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[APLP2]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[CFL1]] | -0.49 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[ADGRE3]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TLL2]] | -0.49 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[ESAM]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[CALM2]] | -0.47 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[AMZ1]] | -0.46 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[CAVIN1]] | -0.45 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[MSN]] | -0.45 | -0.35 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.377). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-48.4, -7.9); signed map (-7.6, -16.7). **Vector** length 63.9, 11.5% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +1.7 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | -0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | -4.5 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.6 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | LETM1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:51,047,962-51,060,424 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCCR1, HCCR, HCCR-2, HCCR-1, HCCR2, SLC55A3 |
| Gene groups (HGNC) | Solute carrier family 55, LETM mitochondrial cation/proton exchangers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1Q0](https://www.uniprot.org/uniprotkb/Q6P1Q0) (LETM1 domain-containing protein 1):

> Plays an essential role for mitochondrial structure and function, as well as thermogenesis of brown adipocytes. In brown adipose tissue also localizes in the nucleus where it interacts with the chromatin remodeler SMARCA4 to regulate thermogenic genes expression, such as UCP1 (By similarity). May regulate phagocytosis and inflammatory responses to lipopolysaccharide in macrophages. Involved in tumorigenesis and may function as a negative regulator of the p53/TP53.

**Summary**, from NCBI Gene [25875](https://www.ncbi.nlm.nih.gov/gene/25875):

> This gene encodes a mitochondrial outer membrane protein. It has a potential role in tumorigenesis, which may result from negative regulation of the p53 tumor suppressor gene. Alternatively spliced transcript variants have been noted for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:24241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24241) · Entrez [25875](https://www.ncbi.nlm.nih.gov/gene/25875) · UniProt [Q6P1Q0](https://www.uniprot.org/uniprotkb/Q6P1Q0) · Ensembl [ENSG00000050426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050426)

## Data

Gene col 566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 566); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 566]; `tensor/DDL_lfc|DDL_z.npy` [566]; `embed/gene_vectors.npy` [566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 566 or target_col == 566). Every well: [[LETMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LETMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
