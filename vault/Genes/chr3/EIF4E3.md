---
symbol: "EIF4E3"
type: "gene"
col: 8687
ensembl_id: "ENSG00000163412"
name: "eukaryotic translation initiation factor 4E family member 3"
location: "3p13"
module: 159
arm: "+"
pooled_cpm: 10.48
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# EIF4E3

*eukaryotic translation initiation factor 4E family member 3* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +10.3, q 5e-22, up in 27 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.339× (z -22.7, q 0e+00, down in 36 of 38 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.426× (z -12.6, q 4e-34, down in 26 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP7B]] (+0.67, fdr 1e-05), [[BLVRA]] (+0.65, fdr 7e-06), [[SGTB]] (+0.64, fdr 7e-06); moves opposite to [[AFG1L]] (-0.57, fdr 4e-05), [[RBM23]] (-0.57, fdr 1e-05), [[ZFX]] (-0.56, fdr 1e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAPG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +10.3 | 5e-22 | 27/42 (SW480, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +7.4 | 4e-11 | 27/40 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +6.2 | 8e-08 | 22/41 (SW480, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.34×** | +6.0 | 2e-07 | 15/43 (A-172, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +5.8 | 7e-07 | 18/42 (SW 900, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.45×** | +5.3 | 1e-05 | 18/40 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +5.0 | 4e-05 | 6/41 (LS 180, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +5.0 | 5e-05 | 16/41 (SW 900, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.7 | 2e-04 | 13/43 (RKO, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.002 | 19/41 (SW 900, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.002 | 8/42 (RKO, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.028 | 4/40 (A-427, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.339×** | -22.7 | 0e+00 | 36/38 (HOP62, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.388×** | -13.5 | 7e-39 | 30/40 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.426×** | -12.6 | 4e-34 | 26/39 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.446×** | -12.0 | 9e-31 | 34/42 (HOP62, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.453×** | -11.7 | 1e-29 | 31/40 (HOP62, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.505×** | -9.7 | 3e-20 | 28/36 (NCI-H460, C-33 A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.309×** | -9.1 | 1e-17 | 26/40 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.599×** | -7.6 | 2e-12 | 22/41 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -6.8 | 8e-10 | 21/37 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.647×** | -6.5 | 6e-09 | 19/40 (NCI-H460, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.629×** | -6.4 | 8e-09 | 21/41 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.658×** | -6.2 | 3e-08 | 16/41 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.676×** | -5.4 | 3e-06 | 19/41 (SW48, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.734×** | -4.6 | 2e-04 | 15/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.725×** | -4.5 | 3e-04 | 12/41 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.633×** | -3.5 | 0.014 | 6/40 (H4, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.017 | 10/41 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.020 | 9/39 (C32, SW480, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.675×** | -3.0 | 0.059 | 5/37 (A549, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.813×** | -3.0 | 0.074 | 8/41 (LoVo, A549, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.870× | -2.9 | 0.078 | 4/42 (COLO 205, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.7 | 1 (1 ⚠) | 9 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -21.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0708× (z -20.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.4) |
| [[A-172 (line)]] | wt | 13.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -8.7) |
| [[A549 (line)]] | wt | 27.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -22.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0715× (z -18.8) |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0498× (z -27.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 6.75 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0633× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0637× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -17.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -16.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -12.5) |
| [[KATO III (line)]] | alt | 21.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 18.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0814× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0225× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 8.88 | 0 | 2 | — | [[Canagliflozin (drug)]] 0.05 µM 0.106× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -15.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 6.10 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0916× (z -9.2) |
| [[A498 (line)]] | wt | 6.37 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 8.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -12.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 3.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 4.47 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0534× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 7.53 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 7.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 3.36 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 6.05 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.42× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP7B]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[BLVRA]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SGTB]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[HEBP1]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SVIL-AS1-1]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[RALGPS1]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SEMA4F]] | +0.60 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[SERAC1]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[RGS10]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[EXTL3]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SLC15A4]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFG1L]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[RBM23]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ZFX]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[COQ7]] | -0.55 | -0.49 / -0.56 | both halves | 2e-05 |  |
| [[ZNF644]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ARHGAP24]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[TASOR]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ZBTB1]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[HCG11]] | -0.52 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[MCPH1]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[BCLAF1]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SRCAP]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAPG]] | B | CAPG activity strengthens EIF4E3's drug response | lines that do not express CAPG (14) vs lines expressing it (28) | the lines without CAPG respond 0.56× as strongly (z diff +1.52); strongest at Homoharringtonine 5 µM: 0.41x vs 0.22x (z diff +3.1) | 0.094 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.2, 2.3); signed map (-38.3, -4.8). **Vector** length 73.0, 13.7% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +6.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.1 | -13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.7 | -22.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -7.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -4.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4E family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:71,675,414-71,754,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39820 |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 7 pathways, smallest: ISG15 antiviral mechanism; Dengue Virus Genome Translation and Replication; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5X7](https://www.uniprot.org/uniprotkb/Q8N5X7) (Eukaryotic translation initiation factor 4E type 3):

> Recognizes and binds the 7-methylguanosine-containing mRNA cap during an early step in the initiation of protein synthesis. May act as an inhibitor of EIF4E1 activity (By similarity).

**Summary**, from NCBI Gene [317649](https://www.ncbi.nlm.nih.gov/gene/317649):

> EIF4E3 belongs to the EIF4E family of translational initiation factors that interact with the 5-prime cap structure of mRNA and recruit mRNA to the ribosome (Joshi et al., 2004 [PubMed 15153109]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:31837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31837) · Entrez [317649](https://www.ncbi.nlm.nih.gov/gene/317649) · UniProt [Q8N5X7](https://www.uniprot.org/uniprotkb/Q8N5X7) · Ensembl [ENSG00000163412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163412)

## Data

Gene col 8687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8687); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8687]; `tensor/DDL_lfc|DDL_z.npy` [8687]; `embed/gene_vectors.npy` [8687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8687 or target_col == 8687). Every well: [[EIF4E3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4E3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
