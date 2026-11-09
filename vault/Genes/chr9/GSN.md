---
symbol: "GSN"
type: "gene"
col: 7249
ensembl_id: "ENSG00000148180"
name: "gelsolin"
location: "9q33.2"
module: 5
arm: "-"
pooled_cpm: 57.08
n_lines_expressing: 47
n_dd_up: 31
n_dd_down: 17
n_dd_up_clean: 26
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# GSN

*gelsolin* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.80× (z +10.6, q 1e-23, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.508× (z -12.3, q 6e-32, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A2]] (+0.61, fdr 3e-05), [[TPPP]] (+0.57, fdr 1e-05), [[MAPK3]] (+0.56, fdr 3e-05); moves opposite to [[SLFNL1-AS1]] (-0.59, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.55, fdr 1e-05), [[TRAPPC12]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[CXADR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **1.80×** | +10.6 | 1e-23 | 36/46 (HEC-1-A, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +9.4 | 2e-18 | 30/45 (LS 180, LoVo, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.2 | 8e-18 | 28/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.56×** | +8.0 | 1e-13 | 33/45 (SNU-423, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.0 | 1e-13 | 23/36 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.52×** | +7.6 | 2e-12 | 26/45 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +7.1 | 1e-10 | 28/45 (J82, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.0 | 2e-07 | 26/45 (A498, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +5.5 | 2e-06 | 25/45 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 2e-05 | 23/45 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +4.7 | 1e-04 | 23/46 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.61×** | +4.5 | 3e-04 | 19/44 (KATO III, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +4.4 | 6e-04 | 22/45 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 9e-04 | 21/45 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.2 | 9e-04 | 18/45 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +4.2 | 1e-03 | 17/45 (A549, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.001 | 18/46 (HEC-1-A, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 21/45 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.508×** | -12.3 | 6e-32 | 39/45 (C32, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.542×** | -11.1 | 3e-26 | 40/45 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -9.6 | 1e-19 | 36/45 (C32, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -9.1 | 2e-17 | 33/45 (C32, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.645×** | -8.0 | 2e-13 | 29/45 (C32, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.651×** | -7.8 | 7e-13 | 29/45 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -7.7 | 2e-12 | 24/44 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -6.0 | 1e-07 | 26/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -6.0 | 1e-07 | 25/45 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.737×** | -5.5 | 2e-06 | 27/45 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.738×** | -5.5 | 2e-06 | 27/45 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.731×** | -5.4 | 4e-06 | 26/45 (HT-29, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.761×** | -5.0 | 3e-05 | 21/44 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -4.8 | 5e-05 | 4/46 (RKO, C-33 A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.604×** | -4.8 | 7e-05 | 20/45 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.848× | -4.2 | 9e-04 | 15/46 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.810×** | -3.7 | 0.008 | 16/44 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.708×** | -3.3 | 0.032 | 9/45 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.068 | 16/44 (MIA PaCa-2, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 345 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -31.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -20.0) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -11.8) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.418× (z -10.6) |
| [[HT-29 (line)]] | alt | 227 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -19.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.229× (z -10.7) |
| [[SW480 (line)]] | alt | 48.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -10.0) |
| [[Hs 766T (line)]] | wt | 103 | 2 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 3.54× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -10.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[COLO 205 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -12.8) |
| [[H4 (line)]] | wt | 62.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.240× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 47.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.8) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.392× (z -9.6) |
| [[LoVo (line)]] | wt | 39.6 | 1 | 1 | [[Selinexor (drug)]] 5 µM 2.24× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -9.1) |
| [[LS 180 (line)]] | wt | 40.2 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.63× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[PANC-1 (line)]] | alt | 47.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 96.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.402× (z -9.4) |
| [[AN3 CA (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -19.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[AsPC-1 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 75.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.93× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 39.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.276× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.305× (z -9.1) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -11.6) ⚠ cell-cycle shift, explains ~10% of this change |
| [[RKO (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -9.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 66.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -9.9) |
| [[SW1417 (line)]] | alt | 70.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -8.7) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.64 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A2]] | +0.61 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[TPPP]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MAPK3]] | +0.56 | +0.43 / +0.46 | both halves | 3e-05 | pathway: Apoptosis |
| [[PPDPF]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[DDR1]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CAPN5]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[AMOT]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CGN]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[CTNND1]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[EDN2]] | +0.52 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CXADR]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[FLVCR2]] | +0.52 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLFNL1-AS1]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TRAPPC12]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CUTC]] | -0.52 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[UGGT2]] | -0.52 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[SCLY]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GPR135]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ST3GAL3]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[EP400P1]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ATR]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SPOPL-DT]] | -0.51 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[GBX2-AS1]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXADR]] | C | GSN activity raises CXADR's level | lines that do not express GSN (3) vs lines expressing it (47) | 7.28× lower at baseline in the lines without GSN | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYH16, PER3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[TRIP10]] | C | GSN activity raises TRIP10's level | lines that do not express GSN (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without GSN | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYH16, PER3, IGF2BP2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (19.6, 0.4); signed map (48.4, 6.1). **Vector** length 109, 30.0% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.1 | +9.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.2 | +7.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.5 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.1 | -3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.5 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | -4.1 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -4.0 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -2.0 | +0.8 |
|  | [[Brimonidine (drug)]] 5 µM |  | -1.8 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | gelsolin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:121,207,794-121,332,843 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313L0718 |
| Gene groups (HGNC) | Gelsolin/villins |
| Hallmark sets | COAGULATION, MYOGENESIS, APOPTOSIS, MITOTIC_SPINDLE |
| Reactome | 11 pathways, smallest: Caspase-mediated cleavage of cytoskeletal proteins; Apoptotic cleavage of cellular proteins; Sensory processing of sound by outer hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [P06396](https://www.uniprot.org/uniprotkb/P06396) (Gelsolin):

> Calcium-regulated, actin-modulating protein that binds to the plus (or barbed) ends of actin monomers or filaments, preventing monomer exchange (end-blocking or capping). It can promote the assembly of monomers into filaments (nucleation) as well as sever filaments already formed. Plays a role in ciliogenesis.

**Summary**, from NCBI Gene [2934](https://www.ncbi.nlm.nih.gov/gene/2934):

> The protein encoded by this gene binds to the "plus" ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4620) · Entrez [2934](https://www.ncbi.nlm.nih.gov/gene/2934) · UniProt [P06396](https://www.uniprot.org/uniprotkb/P06396) · Ensembl [ENSG00000148180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148180)

## Data

Gene col 7249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7249); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7249]; `tensor/DDL_lfc|DDL_z.npy` [7249]; `embed/gene_vectors.npy` [7249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7249 or target_col == 7249). Every well: [[GSN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
