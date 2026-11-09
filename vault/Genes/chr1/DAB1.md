---
symbol: "DAB1"
type: "gene"
col: 10379
ensembl_id: "ENSG00000173406"
name: "DAB adaptor protein 1"
location: "1p32.2"
module: 26
arm: "+"
pooled_cpm: 13.76
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 23
n_dd_up_clean: 21
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# DAB1

*DAB adaptor protein 1* — 1p32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +11.6, q 1e-28, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.453× (z -8.9, q 4e-16, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.520× (z -7.3, q 5e-11, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00276]] (+0.72, fdr 7e-06), [[CFAP418-AS1]] (+0.69, fdr 7e-06), [[LINC01208]] (+0.68, fdr 8e-06); moves opposite to [[LSM11]] (-0.60, fdr 1e-05), [[LCMT1]] (-0.55, fdr 1e-04), [[NBPF3]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02641]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +11.6 | 1e-28 | 33/44 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +8.9 | 2e-16 | 29/48 (A498, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.6 | 8e-09 | 21/38 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +5.9 | 6e-07 | 10/21 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +5.8 | 6e-07 | 25/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.64×** | +5.4 | 7e-06 | 27/45 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.0 | 5e-05 | 17/48 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +4.9 | 6e-05 | 14/30 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.6 | 2e-04 | 18/45 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.48×** | +4.3 | 0.001 | 15/48 (NCI-H460, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.48×** | +4.3 | 0.001 | 16/46 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.001 | 13/46 (C32, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.008 | 11/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.009 | 18/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.015 | 13/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.023 | 8/46 (NCI-H460, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.034 | 12/47 (NCI-H23, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.034 | 10/45 (SW 900, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.453×** | -8.9 | 4e-16 | 33/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.500×** | -7.5 | 3e-11 | 24/40 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -7.3 | 5e-11 | 32/47 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.523×** | -7.3 | 5e-11 | 32/46 (NCI-H1573, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.551×** | -6.7 | 3e-09 | 28/45 (NCI-H1573, HEC-1-A, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.580×** | -5.7 | 9e-07 | 24/47 (COLO 205, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.725×** | -5.1 | 3e-05 | 24/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.645×** | -4.9 | 7e-05 | 23/46 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.652×** | -4.3 | 0.001 | 18/44 (BT-474, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.496×** | -4.1 | 0.002 | 18/42 (NCI-H1573, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.689×** | -4.0 | 0.003 | 19/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.706×** | -3.9 | 0.005 | 18/45 (KATO III, SNU-423, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.787×** | -3.8 | 0.007 | 15/48 (RPMI-7951, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.545×** | -3.6 | 0.015 | 15/43 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.561×** | -3.4 | 0.027 | 14/47 (NCI-H1573, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.730×** | -3.2 | 0.041 | 10/43 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.748×** | -3.1 | 0.054 | 15/45 (RKO, SW 900, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.591×** | -3.1 | 0.059 | 9/45 (NCI-H23, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.682×** | -3.0 | 0.063 | 5/48 (SW480, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.750×** | -3.0 | 0.065 | 9/46 (A-427, LS 180, …) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -2.9 | 0.092 | 7/48 (NCI-H661, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 48.1 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0948× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.184× (z -12.2) |
| [[COLO 205 (line)]] | alt | 57.8 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~52% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.235× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 36.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0820× (z -8.6) |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0840× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 55.3 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0592× (z -13.7) ⚠ toxic |
| [[C32 (line)]] | wt | 47.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0782× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.148× (z -11.4) |
| [[SW480 (line)]] | alt | 9.55 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.4) | — |
| [[A498 (line)]] | wt | 6.83 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.10× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 4.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +8.5) | — |
| [[H4 (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 8.83 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0409× (z -10.6) |
| [[HS-578T (line)]] | alt | 8.31 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -8.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 8.83 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0801× (z -11.2) |
| [[LoVo (line)]] | wt | 9.61 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.99× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 6.81 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0813× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 4.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +9.3) | — |
| [[RKO (line)]] | wt | 4.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.05× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0589× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00276]] | +0.72 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[CFAP418-AS1]] | +0.69 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[LINC01208]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[FSIP2-AS1]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZRANB2-DT]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[TMEM232]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HULC]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[RAP2C-AS1]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | +0.63 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[SLC38A4-AS1]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CHODL]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM11]] | -0.60 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.55 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[NBPF3]] | -0.54 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[SMYD4]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02641]] | B | LINC02641 activity raises DAB1's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.96× lower at baseline in the lines without LINC02641 | 0.014 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity strengthens DAB1's drug response | lines that do not express LINC02641 (14) vs lines expressing it (34) | the lines without LINC02641 respond 0.88× as strongly (z diff +0.59); strongest at Topotecan (hydrochloride) 5 µM: 0.71x vs 0.36x (z diff +3.3) | 0.067 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers DAB1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[RAPGEF4]] | B | RAPGEF4 activity raises DAB1's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without RAPGEF4 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.3, 16.4); signed map (24.7, 0.9). **Vector** length 72.9, 13.4% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +0.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.8 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.4 | -7.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.9 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | DAB adaptor protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.2 — chr1:56,994,778-58,546,734 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 3 pathways, smallest: Reelin signalling pathway; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [O75553](https://www.uniprot.org/uniprotkb/O75553) (Disabled homolog 1):

> Signaling adapter of the reelin-mediated signaling pathway, which regulates the migration and differentiation of postmitotic neurons during brain development. Mediates intracellular transduction of Reelin signaling following reelin (RELN)-binding to its receptor: acts by docking proteins through its phosphotyrosine residues and PID domain.

**Summary**, from NCBI Gene [1600](https://www.ncbi.nlm.nih.gov/gene/1600):

> The laminar organization of multiple neuronal types in the cerebral cortex is required for normal cognitive function. In mice, the disabled-1 gene plays a central role in brain development, directing the migration of cortical neurons past previously formed neurons to reach their proper layer. This gene is similar to disabled-1, and the protein encoded by this gene is thought to be a signal transducer that interacts with protein kinase pathways to regulate neuronal positioning in the developing …

**Accessions** — [HGNC:2661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2661) · Entrez [1600](https://www.ncbi.nlm.nih.gov/gene/1600) · UniProt [O75553](https://www.uniprot.org/uniprotkb/O75553) · Ensembl [ENSG00000173406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173406)

## Data

Gene col 10379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10379); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10379]; `tensor/DDL_lfc|DDL_z.npy` [10379]; `embed/gene_vectors.npy` [10379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10379 or target_col == 10379). Every well: [[DAB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
