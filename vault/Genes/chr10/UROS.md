---
symbol: "UROS"
type: "gene"
col: 12040
ensembl_id: "ENSG00000188690"
name: "uroporphyrinogen III synthase"
location: "10q26.2"
module: 96
arm: "+"
pooled_cpm: 16.77
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# UROS

*uroporphyrinogen III synthase* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.26× (z +15.6, q 0e+00, up in 37 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +4.9, q 6e-05, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.455× (z -10.4, q 2e-22, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TKFC]] (+0.73, fdr 7e-06), [[BPHL]] (+0.71, fdr 7e-06), [[ARPIN]] (+0.70, fdr 1e-05); moves opposite to [[DRD4]] (-0.63, fdr 9e-06), [[MED31]] (-0.59, fdr 1e-05), [[PPP1R32]] (-0.55, fdr 1e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +15.6 | 0e+00 | 37/39 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +14.5 | 1e-45 | 27/27 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +11.1 | 4e-26 | 33/34 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.94×** | +8.4 | 9e-15 | 36/48 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +8.3 | 2e-14 | 33/42 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.70×** | +7.0 | 3e-10 | 33/48 (SW 900, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.60×** | +6.2 | 5e-08 | 27/47 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.9 | 6e-05 | 25/48 (SW480, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.45×** | +4.7 | 2e-04 | 21/48 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.37×** | +4.0 | 0.003 | 20/46 (SNU-423, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.008 | 17/47 (SW480, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +3.6 | 0.012 | 15/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.031 | 10/46 (NCI-H1573, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +3.4 | 0.031 | 17/47 (MIA PaCa-2, J82, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.033 | 8/48 (SW 900, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.070 | 11/48 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.084 | 7/48 (A549, SW480, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +2.9 | 0.091 | 8/48 (A549, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.091 | 12/48 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.092 | 5/48 (LS 180, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.455×** | -10.4 | 2e-22 | 40/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.485×** | -9.1 | 3e-17 | 37/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.517×** | -8.7 | 8e-16 | 33/46 (SHP-77, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -7.2 | 1e-10 | 31/47 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.627×** | -6.1 | 9e-08 | 27/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -5.7 | 1e-06 | 28/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -5.5 | 4e-06 | 22/44 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -4.9 | 7e-05 | 23/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.505×** | -4.7 | 2e-04 | 20/36 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.708×** | -4.5 | 3e-04 | 19/48 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.700×** | -4.4 | 5e-04 | 23/47 (RPMI-7951, C-33 A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.727×** | -4.2 | 0.001 | 18/47 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -4.0 | 0.003 | 20/47 (C-33 A, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.629×** | -3.2 | 0.058 | 17/48 (RKO, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +10.1) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.304× (z -12.1) |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 3 | — | [[Pimozide (drug)]] 0.05 µM 0.144× (z -10.2) |
| [[A-427 (line)]] | wt | 24.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 2 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.0513× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 36.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 30.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.92× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.6) ⚠ cell-cycle shift, explains ~99% of this change |
| [[NCI-H1792 (line)]] | alt | 14.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.58× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.176× (z -10.1) |
| [[A-172 (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +11.7) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[A498 (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0945× (z -8.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +9.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0683× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 19.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -9.1) |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TKFC]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[BPHL]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[ARPIN]] | +0.70 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[IMPACT]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PNPO]] | +0.63 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[SAYSD1]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[COQ2]] | +0.62 | +0.51 / +0.69 | both halves | 1e-05 | STRING 465 |
| [[PIGO]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ZNF252P-1]] | +0.61 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[MLST8]] | +0.61 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[COX11]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRD4]] | -0.63 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[MED31]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PPP1R32]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[BNIPL]] | -0.54 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[HLA-F-AS1]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[LIN52]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RAB43]] | -0.53 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[RAD9A]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ISY1-RAB43]] | -0.52 | -0.24 / -0.63 | both halves | 5e-04 |  |
| [[ZCCHC17]] | -0.52 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ZNHIT1]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[RABGEF1]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises UROS's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-28.1, 22.7); signed map (16.3, -42.1). **Vector** length 63.4, 11.3% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.8 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +14.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +3.4 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.9 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | uroporphyrinogen III synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:125,784,980-125,823,288 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Hallmark sets | FATTY_ACID_METABOLISM, HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P10746](https://www.uniprot.org/uniprotkb/P10746) (Uroporphyrinogen-III synthase):

> Catalyzes cyclization of the linear tetrapyrrole, hydroxymethylbilane, to the macrocyclic uroporphyrinogen III, the branch point for the various sub-pathways leading to the wide diversity of porphyrins. Porphyrins act as cofactors for a multitude of enzymes that perform a variety of processes within the cell such as methionine synthesis (vitamin B12) or oxygen transport (heme).

**Summary**, from NCBI Gene [7390](https://www.ncbi.nlm.nih.gov/gene/7390):

> The protein encoded by this gene catalyzes the fourth step of porphyrin biosynthesis in the heme biosynthetic pathway. Defects in this gene cause congenital erythropoietic porphyria (Gunther's disease). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12592) · Entrez [7390](https://www.ncbi.nlm.nih.gov/gene/7390) · UniProt [P10746](https://www.uniprot.org/uniprotkb/P10746) · Ensembl [ENSG00000188690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188690)

## Data

Gene col 12040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12040); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12040]; `tensor/DDL_lfc|DDL_z.npy` [12040]; `embed/gene_vectors.npy` [12040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12040 or target_col == 12040). Every well: [[UROS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UROS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
