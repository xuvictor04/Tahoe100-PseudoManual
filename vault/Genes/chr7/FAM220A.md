---
symbol: "FAM220A"
type: "gene"
col: 10923
ensembl_id: "ENSG00000178397"
name: "family with sequence similarity 220 member A"
location: "7p22.1"
module: 41
arm: "+"
pooled_cpm: 11.11
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# FAM220A

*family with sequence similarity 220 member A* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.23× (z +18.5, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.333× (z -17.3, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB33B]] (+0.63, fdr 7e-06), [[GOLGA5]] (+0.63, fdr 3e-05), [[ZBTB41]] (+0.60, fdr 1e-05); moves opposite to [[STAU2]] (-0.53, fdr 2e-04), [[MTHFD2L]] (-0.52, fdr 5e-05), [[PARD3]] (-0.50, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.23×** | +18.5 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.03×** | +17.5 | 0e+00 | 46/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +12.6 | 2e-34 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +11.4 | 7e-28 | 31/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +7.4 | 2e-11 | 24/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.5 | 3e-06 | 17/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.28×** | +5.5 | 3e-06 | 16/48 (A-172, NCI-H460, …) | top dose only | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.3 | 6e-06 | 17/40 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +5.3 | 8e-06 | 16/48 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.42×** | +5.1 | 2e-05 | 15/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +4.9 | 5e-05 | 13/45 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.8 | 7e-05 | 11/48 (A-427, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.8 | 8e-05 | 16/45 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.7 | 1e-04 | 17/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.31×** | +4.6 | 2e-04 | 13/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 2e-04 | 13/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +4.4 | 4e-04 | 12/47 (SW480, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.333×** | -17.3 | 0e+00 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -15.2 | 0e+00 | 38/45 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.426×** | -13.4 | 9e-39 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -11.8 | 8e-30 | 34/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.591×** | -8.2 | 2e-14 | 32/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.584×** | -8.1 | 4e-14 | 25/41 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.649×** | -6.8 | 1e-09 | 20/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.666×** | -6.4 | 1e-08 | 23/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -6.4 | 1e-08 | 20/47 (A498, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.688×** | -5.5 | 2e-06 | 20/47 (RPMI-7951, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.659×** | -4.7 | 2e-04 | 7/48 (NCI-H661, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.636×** | -3.4 | 0.031 | 10/44 (Hs 766T, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.4 | 0.032 | 6/48 (C32, SW48, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.653×** | -3.2 | 0.054 | 10/35 (NCI-H460, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.3 | 4 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.66× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.200× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -10.6) |
| [[SW480 (line)]] | alt | 9.03 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.85× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.127× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 8.81 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.95× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -11.9) |
| [[A498 (line)]] | wt | 18.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.18× (z +11.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.302× (z -8.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 17.7 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.09× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0822× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.101× (z -9.7) |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 7.69 | 0 | 2 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0644× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0755× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[C32 (line)]] | wt | 7.24 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0657× (z -9.7) |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0863× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.174× (z -9.3) |
| [[J82 (line)]] | alt | 9.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0620× (z -14.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 9.77 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -12.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 4.80 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0970× (z -9.3) |
| [[LS 180 (line)]] | wt | 6.71 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 9.71 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.151× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 9.97 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.0) |
| [[RKO (line)]] | wt | 4.64 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0815× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.122× (z -8.9) |
| [[SHP-77 (line)]] | alt | 7.49 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0996× (z -8.5) |
| [[SW 900 (line)]] | alt | 7.37 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0791× (z -10.4) |
| [[SW48 (line)]] | wt | 11.8 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0762× (z -9.6) |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB33B]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GOLGA5]] | +0.63 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ZBTB41]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ARL2BP]] | +0.59 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[ARV1]] | +0.57 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[ARMC1]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZNF526]] | +0.56 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[ZNF550]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[MED20]] | +0.55 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[KCTD18]] | +0.55 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[MMUT]] | +0.55 | +0.60 / +0.35 | both halves | 1e-04 |  |
| [[ZNF25]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAU2]] | -0.53 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[MTHFD2L]] | -0.52 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[PARD3]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TUSC3]] | -0.48 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[BICD1]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[HSPE1]] | -0.47 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PLPP2]] | -0.47 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[GBX2-AS1]] | -0.46 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[ATE1]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[TANGO6]] | -0.46 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[NF1]] | -0.46 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[FBXL19-AS1]] | -0.45 | -0.34 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises FAM220A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.3, -16.0); signed map (-18.9, -13.6). **Vector** length 67.2, 11.5% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +17.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.5 | +5.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -15.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -13.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 220 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,329,411-6,348,981 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SIPAR, MGC12966, ACPIN1; previously C7orf70 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4H9](https://www.uniprot.org/uniprotkb/Q7Z4H9) (Protein FAM220A):

> Promotes dephosphorylation of transcriptional activator STAT3 by interacting with both STAT3 and protein phosphatase PTPN2. This promotes interaction of PTPN2 with STAT3 and mediates STAT3 dephosphorylation by PTPN2, leading to negative regulation of STAT3 transcriptional activator activity. May be required for spermiogenesis or sperm function.

**Summary**, from NCBI Gene [84792](https://www.ncbi.nlm.nih.gov/gene/84792):

> Predicted to enable STAT family protein binding activity. Predicted to be involved in intracellular signal transduction. Predicted to act upstream of or within negative regulation of transcription by RNA polymerase II and protein dephosphorylation. Predicted to be located in acrosomal vesicle. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22422) · Entrez [84792](https://www.ncbi.nlm.nih.gov/gene/84792) · UniProt [Q7Z4H9](https://www.uniprot.org/uniprotkb/Q7Z4H9) · Ensembl [ENSG00000178397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178397)

## Data

Gene col 10923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10923); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10923]; `tensor/DDL_lfc|DDL_z.npy` [10923]; `embed/gene_vectors.npy` [10923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10923 or target_col == 10923). Every well: [[FAM220A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM220A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
