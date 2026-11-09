---
symbol: "CKLF"
type: "gene"
col: 13285
ensembl_id: "ENSG00000217555"
name: "chemokine like factor"
location: "16q21"
module: 135
arm: "-"
pooled_cpm: 37.04
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# CKLF

*chemokine like factor* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.81× (z +6.6, q 3e-08, up in 35 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.53× (z +4.7, q 4e-04, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.253× (z -21.5, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTTN]] (+0.72, fdr 1e-05), [[CMTM1]] (+0.71, fdr 7e-06, ⚠ same locus), [[AP3M2]] (+0.68, fdr 1e-05), [[LPCAT4]] (+0.68, fdr 5e-05); moves opposite to [[TMEM202-AS1]] (-0.66, fdr 2e-04), [[LINC00571]] (-0.66, fdr 1e-04), [[CLIP1]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.81×** | +6.6 | 3e-08 | 35/48 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.62×** | +5.4 | 2e-05 | 33/48 (LoVo, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +4.7 | 4e-04 | 35/48 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.54×** | +4.6 | 6e-04 | 22/37 (A549, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.2 | 0.003 | 27/48 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.45×** | +4.1 | 0.003 | 26/48 (LoVo, NCI-H1573, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.1 | 0.003 | 27/46 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.42×** | +3.9 | 0.007 | 30/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.027 | 23/48 (A549, A498, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.253×** | -21.5 | 0e+00 | 45/47 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.281×** | -14.0 | 4e-42 | 44/47 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -8.1 | 1e-13 | 39/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -7.3 | 4e-11 | 35/47 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.566×** | -6.0 | 2e-07 | 31/48 (COLO 205, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -5.5 | 3e-06 | 31/48 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.593×** | -5.5 | 4e-06 | 33/48 (COLO 205, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.384×** | -5.3 | 7e-06 | 36/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.424×** | -4.8 | 1e-04 | 31/47 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.620×** | -4.6 | 2e-04 | 27/48 (COLO 205, HEC-1-A, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.469×** | -4.2 | 0.001 | 30/47 (CFPAC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.502×** | -3.8 | 0.006 | 25/47 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.709×** | -3.8 | 0.006 | 23/48 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.705×** | -3.7 | 0.009 | 21/47 (COLO 205, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.705×** | -3.6 | 0.014 | 21/48 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.789×** | -3.5 | 0.015 | 21/48 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 120 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0674× (z -27.0) |
| [[MIA PaCa-2 (line)]] | alt | 36.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 35.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -20.1) |
| [[A-427 (line)]] | wt | 48.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 56.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 56.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -19.6) |
| [[HepG2_C3A (line)]] | wt | 95.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -18.6) |
| [[SW 900 (line)]] | alt | 40.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -18.6) |
| [[SW480 (line)]] | alt | 58.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -19.3) |
| [[A-172 (line)]] | wt | 36.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -12.3) |
| [[A498 (line)]] | wt | 35.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.8) |
| [[A549 (line)]] | wt | 16.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.4) |
| [[HOP62 (line)]] | alt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.5) |
| [[HS-578T (line)]] | alt | 27.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.0) |
| [[KATO III (line)]] | alt | 47.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -24.8) |
| [[LoVo (line)]] | wt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -23.9) |
| [[NCI-H2030 (line)]] | alt | 95.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -21.3) |
| [[PANC-1 (line)]] | alt | 40.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.0) |
| [[SW48 (line)]] | wt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.7) |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.8) |
| [[C-33 A (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[H4 (line)]] | wt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0290× (z -17.7) |
| [[HCT15 (line)]] | alt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.6) |
| [[Hs 766T (line)]] | wt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.3) |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -12.5) |
| [[J82 (line)]] | alt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.2) |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -12.4) |
| [[RKO (line)]] | wt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.2) |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0801× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0677× (z -13.5) |
| [[SW 1271 (line)]] | alt | 78.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0507× (z -16.5) |
| [[SW1417 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.1) |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTTN]] | +0.72 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[CMTM1]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | STRING 440; ⚠ same locus (0.1 kb, same strand: neighbours can correlate without regulation) |
| [[AP3M2]] | +0.68 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.68 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[NR2C1]] | +0.68 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[RNF168]] | +0.67 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[L2HGDH]] | +0.67 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CASP2]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[RFC4]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SMYD4]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.65 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[FAM24B]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RBL1]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | -0.66 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.66 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[CLIP1]] | -0.65 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.64 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[PBLD]] | -0.64 | -0.54 / -0.32 | both halves | 1e-04 |  |
| [[PCNX4-DT]] | -0.64 | -0.60 / -0.22 | both halves | 6e-04 |  |
| [[LINC02542]] | -0.63 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | -0.62 | -0.58 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ACYP2]] | -0.62 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[CAPN3]] | -0.62 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | -0.62 | -0.53 / -0.23 | both halves | 5e-04 |  |
| [[CFAP418-AS1]] | -0.61 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[KRCC1]] | -0.61 | -0.65 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CKLF's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BTG3-AS1]] | B | BTG3-AS1 activity strengthens CKLF's drug response | lines that do not express BTG3-AS1 (7) vs lines expressing it (41) | the lines without BTG3-AS1 respond 0.85× as strongly (z diff +0.66); strongest at Idarubicin (hydrochloride) 5 µM: 0.77x vs 0.56x (z diff +2.5) | 0.086 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (4.6, 5.2); signed map (-41.0, -10.2). **Vector** length 105, 31.6% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +6.9 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.1 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.5 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.3 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +5.1 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -21.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -14.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -2.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.6 | -5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.1 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.7 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | chemokine like factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:66,552,563-66,566,251 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UCK-1, CKLF3, CKLF4, HSPC224, C32; previously CKLF1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBR5](https://www.uniprot.org/uniprotkb/Q9UBR5) (Chemokine-like factor):

> May play an important role in inflammation and regeneration of skeletal muscle. Essential for embryonic development (By similarity).; [Isoform 1]: Has chemotactic response in monocytes, neutrophils and lymphocytes. Binds CCR4.

**Summary**, from NCBI Gene [51192](https://www.ncbi.nlm.nih.gov/gene/51192):

> The product of this gene is a cytokine. Cytokines are small proteins that have an essential role in the immune and inflammatory responses. This gene is one of several chemokine-like factor genes located in a cluster on chromosome 16. The protein encoded by this gene is a potent chemoattractant for neutrophils, monocytes and lymphocytes. It also can stimulate the proliferation of skeletal muscle cells. This protein may play important roles in inflammation and in the regeneration of skeletal …

**Accessions** — [HGNC:13253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13253) · Entrez [51192](https://www.ncbi.nlm.nih.gov/gene/51192) · UniProt [Q9UBR5](https://www.uniprot.org/uniprotkb/Q9UBR5) · Ensembl [ENSG00000217555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000217555)

## Data

Gene col 13285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13285); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13285]; `tensor/DDL_lfc|DDL_z.npy` [13285]; `embed/gene_vectors.npy` [13285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13285 or target_col == 13285). Every well: [[CKLF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKLF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
