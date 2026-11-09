---
symbol: "MELTF"
type: "gene"
col: 8827
ensembl_id: "ENSG00000163975"
name: "melanotransferrin"
location: "3q29"
module: 45
arm: "-"
pooled_cpm: 36.65
n_lines_expressing: 43
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# MELTF

*melanotransferrin* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.35× (z +6.0, q 1e-06, up in 19 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.472× (z -10.4, q 1e-22, down in 33 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE2]] (+0.62, fdr 1e-05), [[GATAD2A]] (+0.56, fdr 2e-05), [[EBF4]] (+0.55, fdr 8e-05); moves opposite to [[PEX2]] (-0.59, fdr 2e-05), [[SPATA7]] (-0.53, fdr 2e-05), [[RHOXF1]] (-0.52, fdr 9e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CARD11]] → it (grade B ⚠); 4 go from it, the strongest it → [[CLCF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.0 | 1e-06 | 19/41 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.5 | 0.002 | 17/36 (A-427, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.4 | 0.002 | 13/32 (SW 900, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.39×** | +4.4 | 0.002 | 19/40 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.1 | 0.005 | 12/29 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.011 | 8/41 (Panc 03.27, A-172, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.8 | 0.011 | 3/41 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.037 | 16/40 (A-172, SW480, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.038 | 16/40 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.038 | 12/41 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.077 | 11/41 (J82, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.472×** | -10.4 | 1e-22 | 33/40 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.466×** | -10.2 | 6e-22 | 31/39 (Panc 03.27, A-172, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.521×** | -9.0 | 3e-17 | 29/40 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.531×** | -8.8 | 3e-16 | 29/39 (SNU-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.653×** | -8.3 | 9e-15 | 22/40 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.379×** | -7.0 | 2e-10 | 26/38 (LOX-IMVI, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -7.0 | 2e-10 | 27/39 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.382×** | -7.0 | 2e-10 | 29/41 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.618×** | -6.7 | 2e-09 | 25/40 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.618×** | -6.4 | 8e-09 | 24/37 (NCI-H23, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.639×** | -6.2 | 3e-08 | 27/40 (SK-MEL-2, A-172, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.646×** | -6.0 | 7e-08 | 23/40 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.660×** | -5.7 | 4e-07 | 22/40 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.671×** | -5.5 | 1e-06 | 22/40 (SK-MEL-2, A-172, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.725×** | -4.4 | 3e-04 | 15/41 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -4.1 | 0.001 | 19/40 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.003 | 15/41 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.822×** | -3.8 | 0.004 | 18/41 (A498, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.761×** | -3.8 | 0.005 | 19/39 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.786×** | -3.3 | 0.024 | 12/40 (SW480, A-172, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.783×** | -3.2 | 0.030 | 16/40 (SK-MEL-2, C32, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.795×** | -3.2 | 0.037 | 16/40 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 86.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 272 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -15.9) |
| [[SNU-1 (line)]] | wt | 45.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0778× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 58.4 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.214× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 194 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -28.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -23.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -10.7) |
| [[SW480 (line)]] | alt | 29.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -10.8) |
| [[A-427 (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -11.4) |
| [[A549 (line)]] | wt | 39.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.3) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.206× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 36.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.8) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RKO (line)]] | wt | 24.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW 900 (line)]] | alt | 31.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -11.5) |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -8.8) |
| [[SW48 (line)]] | wt | 54.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -10.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -14.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[C32 (line)]] | wt | 93.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0781× (z -8.7) |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.96 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE2]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[GATAD2A]] | +0.56 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[EBF4]] | +0.55 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[TBILA]] | +0.54 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[EFCAB8]] | +0.53 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[ADCY7]] | +0.52 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[SFXN5]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MSANTD1]] | +0.50 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[MDGA1]] | +0.50 | +0.46 / +0.52 | both halves | 3e-05 | pathway: Post-translational modification: synthesis of GPI-anchored proteins |
| [[KCNC4]] | +0.50 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[AKR1E2]] | +0.50 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[WNT3]] | +0.49 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX2]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[SPATA7]] | -0.53 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[RHOXF1]] | -0.52 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[NUDCD2]] | -0.50 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[ANAPC16]] | -0.49 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[RCOR3]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[IFT172]] | -0.49 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[TRAPPC11]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[NSL1]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[GEMIN8]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ABITRAM]] | -0.47 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[NIPSNAP2]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD11]] | B | CARD11 activity raises MELTF's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.72× lower at baseline in the lines without CARD11 | 0.040 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[SLC4A3]] | B | SLC4A3 activity raises MELTF's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.03× lower at baseline in the lines without SLC4A3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCF1]] | B | MELTF activity raises CLCF1's level | lines that do not express MELTF (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without MELTF | 0.060 | ⚠ within organs, on part of the lines; also absent: EPHX2, ACCS; maybe low, not absent; its own permutation p |
| [[CPNE2]] | B | MELTF activity raises CPNE2's level | lines that do not express MELTF (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without MELTF | 0.060 | ⚠ within organs, on part of the lines; also absent: EPHX2, ACCS; maybe low, not absent; its own permutation p |
| [[SLC22A20P]] | B | MELTF activity raises SLC22A20P's level | lines that do not express MELTF (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without MELTF | 0.089 | ⚠ within organs, on part of the lines; also absent: EPHX2, ACCS; maybe low, not absent; its own permutation p |
| [[DPM3]] | B | MELTF activity lowers DPM3's level | lines that do not express MELTF (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without MELTF | 0.090 | ⚠ within organs, on part of the lines; also absent: EPHX2, ACCS; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.354). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (18.4, -11.8); signed map (-11.1, 41.1). **Vector** length 91.7, 21.2% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | -1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.4 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.3 | -10.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | melanotransferrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,980,590-197,029,835 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD228, FLJ38863, MAP97, MGC4856, MTF1, MTf; previously MFI2 |
| Gene groups (HGNC) | CD molecules; Transferrins |
| Reactome | 3 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins; Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P08582](https://www.uniprot.org/uniprotkb/P08582) (Melanotransferrin):

> Involved in iron cellular uptake. Seems to be internalized and then recycled back to the cell membrane. Binds a single atom of iron per subunit. Could also bind zinc.

**Summary**, from NCBI Gene [4241](https://www.ncbi.nlm.nih.gov/gene/4241):

> The protein encoded by this gene is a cell-surface glycoprotein found on melanoma cells. The protein shares sequence similarity and iron-binding properties with members of the transferrin superfamily. The importance of the iron binding function has not yet been identified. This gene resides in the same region of chromosome 3 as members of the transferrin superfamily. Alternative splicing results in two transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7037) · Entrez [4241](https://www.ncbi.nlm.nih.gov/gene/4241) · UniProt [P08582](https://www.uniprot.org/uniprotkb/P08582) · Ensembl [ENSG00000163975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163975)

## Data

Gene col 8827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8827); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8827]; `tensor/DDL_lfc|DDL_z.npy` [8827]; `embed/gene_vectors.npy` [8827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8827 or target_col == 8827). Every well: [[MELTF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MELTF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
