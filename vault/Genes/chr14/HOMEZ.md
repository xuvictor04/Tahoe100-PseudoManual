---
symbol: "HOMEZ"
type: "gene"
col: 16470
ensembl_id: "ENSG00000290292"
name: "homeobox and leucine zipper encoding"
location: "14q11.2"
module: 23
arm: "+"
pooled_cpm: 7.21
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 21
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# HOMEZ

*homeobox and leucine zipper encoding* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +11.3, q 7e-27, up in 31 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.443× (z -10.6, q 2e-23, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRANCR]] (+0.64, fdr 2e-05), [[CFAP43]] (+0.64, fdr 1e-05), [[C11orf71]] (+0.64, fdr 3e-05); moves opposite to [[SMC5]] (-0.60, fdr 4e-05), [[AP3M2]] (-0.60, fdr 3e-05), [[DGKD]] (-0.59, fdr 5e-05).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +11.3 | 7e-27 | 31/42 (BT-474, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.3 | 9e-08 | 19/40 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +5.3 | 2e-05 | 17/46 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +5.3 | 2e-05 | 17/37 (SNU-423, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.1 | 3e-05 | 17/47 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.7 | 3e-04 | 16/45 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +4.6 | 3e-04 | 17/40 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 3e-04 | 10/47 (NCI-H2030, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +4.4 | 5e-04 | 12/44 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 7e-04 | 10/44 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 9e-04 | 13/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.42×** | +4.2 | 0.001 | 8/47 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.001 | 17/44 (C-33 A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 13/46 (A549, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.25×** | +4.1 | 0.002 | 8/46 (RKO, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.002 | 11/45 (HEC-1-A, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.006 | 9/48 (SK-MEL-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.443×** | -10.6 | 2e-23 | 36/45 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -10.2 | 7e-22 | 28/43 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -8.3 | 1e-14 | 29/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.323×** | -7.7 | 2e-12 | 28/44 (LoVo, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.342×** | -7.3 | 3e-11 | 28/40 (NCI-H1573, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.577×** | -7.2 | 8e-11 | 28/47 (HS-578T, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.578×** | -6.9 | 6e-10 | 23/39 (HCT15, C32, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.603×** | -6.2 | 3e-08 | 24/43 (H4, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.621×** | -6.2 | 3e-08 | 23/45 (SW 900, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.675×** | -5.1 | 2e-05 | 19/45 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.735×** | -4.0 | 0.003 | 14/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.737×** | -4.0 | 0.003 | 14/47 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.767×** | -3.5 | 0.023 | 16/45 (HCT15, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 11.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0618× (z -12.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 6.63 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0730× (z -10.6) |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.05 µM 0.0806× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 9.38 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0469× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0240× (z -10.4) |
| [[A498 (line)]] | wt | 2.97 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0667× (z -10.3) |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.128× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0727× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 9.15 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0589× (z -10.7) |
| [[J82 (line)]] | alt | 5.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -10.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 7.51 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.144× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 8.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 6.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 4.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 7.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.65 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 7.22 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0749× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRANCR]] | +0.64 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[CFAP43]] | +0.64 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[C11orf71]] | +0.64 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[C3orf38]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[N4BP2L1]] | +0.63 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[OXA1L-DT]] | +0.63 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[KRCC1]] | +0.62 | +0.72 / +0.39 | both halves | 5e-05 |  |
| [[DNAI4]] | +0.62 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | +0.61 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[THAP2]] | +0.61 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[ZNF213]] | +0.61 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[INTS6-AS1]] | +0.61 | +0.66 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC5]] | -0.60 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[AP3M2]] | -0.60 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[DGKD]] | -0.59 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[MCOLN2]] | -0.58 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[GNA12]] | -0.57 | -0.65 / -0.32 | both halves | 1e-04 |  |
| [[RTTN]] | -0.56 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[NAPG]] | -0.56 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[LRRC20]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[RNF216]] | -0.55 | -0.64 / -0.31 | both halves | 2e-04 |  |
| [[PARP1]] | -0.54 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[SPATA5]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[HERC2P9]] | -0.54 | -0.52 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (2.1, 16.3); signed map (25.9, -10.9). **Vector** length 61.7, 9.17% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +11.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +4.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.3 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.0 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | homeobox and leucine zipper encoding |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,272,422-23,299,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1443 |
| Gene groups (HGNC) | ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX15](https://www.uniprot.org/uniprotkb/Q8IX15) (Homeobox and leucine zipper protein Homez):

> May function as a transcriptional regulator.

**Summary**, from NCBI Gene [57594](https://www.ncbi.nlm.nih.gov/gene/57594):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20164) · Entrez [57594](https://www.ncbi.nlm.nih.gov/gene/57594) · UniProt [Q8IX15](https://www.uniprot.org/uniprotkb/Q8IX15) · Ensembl [ENSG00000290292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000290292)

## Data

Gene col 16470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16470); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16470]; `tensor/DDL_lfc|DDL_z.npy` [16470]; `embed/gene_vectors.npy` [16470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16470 or target_col == 16470). Every well: [[HOMEZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOMEZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
