---
symbol: "FBXL5"
type: "gene"
col: 4004
ensembl_id: "ENSG00000118564"
name: "F-box and leucine rich repeat protein 5"
location: "4p15.32"
module: 198
arm: "+"
pooled_cpm: 93.0
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# FBXL5

*F-box and leucine rich repeat protein 5* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.54× (z +8.4, q 3e-14, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.473× (z -14.0, q 9e-42, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.675× (z -10.8, q 7e-25, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTWD1]] (+0.64, fdr 7e-06), [[XPA]] (+0.58, fdr 2e-05), [[MRPL39]] (+0.57, fdr 3e-05); moves opposite to [[FERMT3]] (-0.59, fdr 1e-05), [[CDC37]] (-0.55, fdr 2e-05), [[LRRC59]] (-0.51, fdr 3e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DEPDC7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +8.4 | 3e-14 | 32/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.2 | 2e-10 | 32/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +6.2 | 9e-08 | 32/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 5e-05 | 28/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.006 | 20/48 (NCI-H23, J82, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.056 | 17/47 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4004.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.473×** | -14.0 | 9e-42 | 39/44 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.558×** | -11.3 | 2e-27 | 43/49 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -10.8 | 7e-25 | 37/49 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.584×** | -10.4 | 2e-23 | 40/48 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.605×** | -9.8 | 1e-20 | 41/48 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.582×** | -9.7 | 2e-20 | 30/45 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -8.6 | 8e-16 | 37/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -6.3 | 2e-08 | 31/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.564×** | -5.8 | 4e-07 | 33/45 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.769×** | -5.1 | 2e-05 | 27/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -5.0 | 3e-05 | 27/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.777×** | -4.7 | 1e-04 | 25/50 (A-172, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.788×** | -4.5 | 4e-04 | 24/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.4 | 4e-04 | 2/50 (AN3 CA, SW 1088) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.802×** | -4.1 | 0.002 | 23/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.848× | -3.1 | 0.065 | 16/48 (NCI-H460, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 163 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 156 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -20.5) |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 175 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 149 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.353× (z -12.5) |
| [[HOP62 (line)]] | alt | 114 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.6) |
| [[A-172 (line)]] | wt | 110 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -13.6) |
| [[A549 (line)]] | wt | 129 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.413× (z -10.2) |
| [[SNU-423 (line)]] | alt | 102 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.1) |
| [[C32 (line)]] | wt | 124 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.331× (z -9.6) |
| [[J82 (line)]] | alt | 89.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 63.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 176 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -11.4) |
| [[SW480 (line)]] | alt | 65.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.94× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -12.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 69.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 126 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.335× (z -10.1) |
| [[Hs 766T (line)]] | wt | 85.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.6) |
| [[KATO III (line)]] | alt | 65.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.63× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.10× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 79.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 81.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -10.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -12.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -18.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 77.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -11.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 95.3 | 0 | 1 | — | [[Alpelisib (drug)]] 5 µM 0.0751× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 90.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 78.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 76.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +9.1) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[SHP-77 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.157× (z -8.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 93.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -15.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTWD1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[XPA]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MRPL39]] | +0.57 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[POLH]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[DDB2]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 | pathway: Neddylation |
| [[TP53TG1]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[RWDD3]] | +0.53 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[RCHY1]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[NSL1]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[LSM6]] | +0.52 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[NDUFV2]] | +0.51 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[LSM14A]] | +0.51 | +0.54 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FERMT3]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[CDC37]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[LRRC59]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TUBA8]] | -0.51 | -0.58 / -0.38 | both halves | 7e-05 | pathway: Chaperonin-mediated protein folding |
| [[SFXN5]] | -0.51 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[VCP]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 | pathway: Neddylation |
| [[MSANTD1]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[EIF3I]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SPTBN5]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MAP1B]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[DNAJB6]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ETF1]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DEPDC7]] | B | DEPDC7 activity lowers FBXL5's level | lines that do not express DEPDC7 (13) vs lines expressing it (37) | 1.29× higher at baseline in the lines without DEPDC7 | 0.059 | ⚠ within organs, on part of the lines |
| [[TOP2A]] | B | TOP2A activity raises FBXL5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.7, -3.5); signed map (-22.4, -9.5). **Vector** length 106, 29.5% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.9 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.8 | +6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | +2.3 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.1 | -6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.1 | -5.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.1 | -5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -2.7 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:15,604,381-15,681,679 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBL4, FBL5, FLR1; previously CC2D2A-AS1 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 9 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Iron uptake and transport; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKA1](https://www.uniprot.org/uniprotkb/Q9UKA1) (F-box/LRR-repeat protein 5):

> Component of some SCF (SKP1-cullin-F-box) protein ligase complex that plays a central role in iron homeostasis by promoting the ubiquitination and subsequent degradation of IREB2/IRP2. The C-terminal domain of FBXL5 contains a redox-sensitive [2Fe-2S] cluster that, upon oxidation, promotes binding to IRP2 to effect its oxygen-dependent degradation. Under iron deficiency conditions, the N-terminal hemerythrin-like (Hr) region, which contains a diiron metal center, cannot bind iron and undergoes …

**Summary**, from NCBI Gene [26234](https://www.ncbi.nlm.nih.gov/gene/26234):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13602) · Entrez [26234](https://www.ncbi.nlm.nih.gov/gene/26234) · UniProt [Q9UKA1](https://www.uniprot.org/uniprotkb/Q9UKA1) · Ensembl [ENSG00000118564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118564)

## Data

Gene col 4004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4004); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4004]; `tensor/DDL_lfc|DDL_z.npy` [4004]; `embed/gene_vectors.npy` [4004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4004 or target_col == 4004). Every well: [[FBXL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
