---
symbol: "STYXL1"
type: "gene"
col: 4847
ensembl_id: "ENSG00000127952"
name: "serine/threonine/tyrosine interacting like 1"
location: "7q11.23"
module: 11
arm: "+"
pooled_cpm: 41.66
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# STYXL1

*serine/threonine/tyrosine interacting like 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +8.8, q 1e-15, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.407× (z -13.6, q 4e-39, down in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.409× (z -13.5, q 4e-39, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO38]] (+0.70, fdr 1e-05), [[UTP3]] (+0.68, fdr 1e-05), [[NSRP1]] (+0.67, fdr 7e-06); moves opposite to [[PPT1]] (-0.63, fdr 7e-06), [[PRDX3]] (-0.62, fdr 1e-05), [[FAM102B]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +8.8 | 1e-15 | 34/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.7 | 5e-09 | 38/48 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.2 | 8e-08 | 35/48 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 9e-08 | 32/47 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.0 | 2e-07 | 32/48 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +5.7 | 1e-06 | 29/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +5.6 | 2e-06 | 30/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +5.2 | 1e-05 | 25/48 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 3e-05 | 28/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +4.8 | 1e-04 | 27/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 6e-04 | 28/48 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.4 | 6e-04 | 25/48 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.009 | 21/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.011 | 16/48 (HepG2/C3A, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.013 | 14/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.407×** | -13.6 | 4e-39 | 41/47 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.409×** | -13.5 | 4e-39 | 41/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.472×** | -11.4 | 1e-27 | 40/48 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.487×** | -10.9 | 2e-25 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.587×** | -7.7 | 1e-12 | 36/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.559×** | -4.6 | 4e-04 | 17/33 (SW 900, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.723×** | -4.2 | 0.002 | 23/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.746×** | -3.8 | 0.010 | 19/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.786×** | -3.7 | 0.015 | 19/48 (NCI-H2030, BT-474, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.635×** | -3.6 | 0.018 | 21/47 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.786×** | -3.5 | 0.022 | 18/48 (A-172, SW 1088, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.787×** | -3.5 | 0.022 | 23/46 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.753×** | -3.1 | 0.092 | 12/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 58.3 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 41.9 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.1) | [[Digitoxin (drug)]] 0.5 µM 0.302× (z -11.1) |
| [[SW480 (line)]] | alt | 46.2 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.269× (z -13.8) |
| [[KATO III (line)]] | alt | 77.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 52.8 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.270× (z -11.4) |
| [[PANC-1 (line)]] | alt | 46.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.379× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 38.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.263× (z -13.2) |
| [[A-427 (line)]] | wt | 31.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.355× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0861× (z -11.9) |
| [[HT-29 (line)]] | alt | 50.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -10.6) |
| [[J82 (line)]] | alt | 29.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 66.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -9.0) ⚠ toxic |
| [[C32 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -9.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 38.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.198× (z -11.3) |
| [[HCT15 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -8.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.264× (z -8.8) |
| [[LS 180 (line)]] | wt | 29.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.268× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 62.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.363× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.247× (z -10.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0589× (z -11.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO38]] | +0.70 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[UTP3]] | +0.68 | +0.82 / +0.55 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.67 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[MZF1-AS1]] | +0.66 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[KRCC1]] | +0.64 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[EID2]] | +0.63 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[R3HDM2]] | +0.63 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[BPTF]] | +0.63 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[LINC00174]] | +0.63 | +0.81 / +0.39 | both halves | 5e-05 |  |
| [[TIMMDC1]] | +0.63 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[CES2]] | +0.63 | +0.77 / +0.49 | both halves | 1e-05 |  |
| [[C6orf62]] | +0.62 | +0.70 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | -0.63 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[PRDX3]] | -0.62 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[FAM102B]] | -0.61 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[METAP1]] | -0.60 | -0.77 / -0.47 | both halves | 2e-05 |  |
| [[RPA1]] | -0.60 | -0.70 / -0.53 | both halves | 1e-05 |  |
| [[TECR]] | -0.58 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[CALM3]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[MDH2]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SKP2]] | -0.57 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[PPAT]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ELL3]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PRPS2]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CREG1]] | -0.56 | -0.35 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STYXL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WFDC10B]] | B | WFDC10B activity raises STYXL1's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.18× lower at baseline in the lines without WFDC10B | 0.031 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[NUP62CL]] | B | NUP62CL activity raises STYXL1's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.14× lower at baseline in the lines without NUP62CL | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| [[LAPTM4B]] | C | LAPTM4B activity raises STYXL1's level | lines that do not express LAPTM4B (4) vs lines expressing it (46) | 1.33× lower at baseline in the lines without LAPTM4B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: BMS1P23; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.4, 5.9); signed map (0.4, -17.6). **Vector** length 104, 28.7% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.9 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.5 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.6 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine/tyrosine interacting like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,996,338-76,048,004 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MK-STYX; previously DUSP24 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6J8](https://www.uniprot.org/uniprotkb/Q9Y6J8) (Serine/threonine/tyrosine-interacting-like protein 1):

> Catalytically inactive phosphatase. By binding to G3BP1, inhibits the formation of G3BP1-induced stress granules. Does not act by protecting the dephosphorylation of G3BP1 at 'Ser-149'. Inhibits PTPMT1 phosphatase activity. By inhibiting PTPMT1, positively regulates intrinsic apoptosis. May play a role in the formation of neurites during neuronal development.

**Summary**, from NCBI Gene [51657](https://www.ncbi.nlm.nih.gov/gene/51657):

> Enables protein phosphatase binding activity and pseudophosphatase activity. Involved in negative regulation of stress granule assembly; positive regulation of intrinsic apoptotic signaling pathway; and positive regulation of neuron projection development. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18165) · Entrez [51657](https://www.ncbi.nlm.nih.gov/gene/51657) · UniProt [Q9Y6J8](https://www.uniprot.org/uniprotkb/Q9Y6J8) · Ensembl [ENSG00000127952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127952)

## Data

Gene col 4847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4847); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4847]; `tensor/DDL_lfc|DDL_z.npy` [4847]; `embed/gene_vectors.npy` [4847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4847 or target_col == 4847). Every well: [[STYXL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STYXL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
