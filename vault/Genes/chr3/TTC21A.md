---
symbol: "TTC21A"
type: "gene"
col: 9583
ensembl_id: "ENSG00000168026"
name: "tetratricopeptide repeat domain 21A"
location: "3p22.2"
module: 4
arm: "-"
pooled_cpm: 12.24
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 28
n_dd_up_clean: 23
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TTC21A

*tetratricopeptide repeat domain 21A* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +16.3, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.423× (z -12.4, q 2e-32, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIRT2]] (+0.71, fdr 7e-06), [[MED19]] (+0.66, fdr 7e-06), [[HADHB]] (+0.63, fdr 9e-06); moves opposite to [[TMEM33]] (-0.71, fdr 1e-05), [[TMX3]] (-0.67, fdr 7e-06), [[SLC35B4]] (-0.65, fdr 8e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, none with an alert; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +16.3 | 0e+00 | 41/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.31×** | +11.5 | 4e-28 | 36/48 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +10.0 | 4e-21 | 35/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +9.1 | 1e-17 | 31/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +8.3 | 2e-14 | 34/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +7.8 | 8e-13 | 25/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +6.4 | 1e-08 | 24/46 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +4.8 | 1e-04 | 14/48 (HEC-1-A, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.002 | 14/47 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.002 | 12/48 (SW480, A-172, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.003 | 17/46 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.005 | 12/48 (HEC-1-A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.005 | 12/48 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.006 | 14/48 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.011 | 14/47 (SW480, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.423×** | -12.4 | 2e-32 | 40/48 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.433×** | -11.6 | 2e-28 | 33/41 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.468×** | -10.9 | 2e-25 | 34/47 (A-172, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.460×** | -10.7 | 2e-24 | 38/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.477×** | -10.6 | 2e-24 | 23/35 (NCI-H1792, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -10.0 | 2e-21 | 33/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.507×** | -9.8 | 1e-20 | 36/47 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.518×** | -9.0 | 1e-17 | 31/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.552×** | -7.9 | 2e-13 | 19/29 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.633×** | -6.6 | 3e-09 | 23/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.633×** | -6.3 | 2e-08 | 23/48 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -5.8 | 3e-07 | 24/47 (A549, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.470×** | -5.7 | 6e-07 | 25/48 (HS-578T, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -5.3 | 4e-06 | 19/44 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.690×** | -5.3 | 4e-06 | 23/48 (SNU-1, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -4.4 | 3e-04 | 20/48 (HT-29, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.749×** | -4.1 | 9e-04 | 15/47 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.748×** | -3.9 | 0.003 | 12/45 (A549, H4, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.755×** | -3.8 | 0.004 | 18/47 (C32, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -9.1) |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0586× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.159× (z -11.0) |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.171× (z -11.0) |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.185× (z -9.3) |
| [[SW480 (line)]] | alt | 10.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -13.4) |
| [[A-172 (line)]] | wt | 28.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0679× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.150× (z -13.7) |
| [[A549 (line)]] | wt | 14.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.256× (z -8.6) |
| [[HOP62 (line)]] | alt | 12.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -9.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 6.92 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +11.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -11.5) ⚠ toxic |
| [[C32 (line)]] | wt | 14.6 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.118× (z -10.9) |
| [[LoVo (line)]] | wt | 9.62 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.162× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.178× (z -11.0) |
| [[A498 (line)]] | wt | 9.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0965× (z -14.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 5.69 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0696× (z -11.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 6.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0481× (z -18.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -8.7) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0431× (z -8.5) |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[MED19]] | +0.66 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[HADHB]] | +0.63 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[PMM1]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RNASE4]] | +0.62 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[CDK7]] | +0.62 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[HCFC1R1]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[WBP1]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.60 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[KDM5B]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM33]] | -0.71 | -0.56 / -0.71 | both halves | 1e-05 |  |
| [[TMX3]] | -0.67 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[SLC35B4]] | -0.65 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[VMA21]] | -0.65 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.64 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[CCT5]] | -0.64 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[WDR77]] | -0.62 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.61 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[ANKRD52]] | -0.61 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NUP155]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[NAA50]] | -0.59 | -0.58 / -0.60 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TTC21A's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.2, -31.6); signed map (-14.5, 2.9). **Vector** length 81.7, 17.5% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +7.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.1 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.3 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.6 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -4.6 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 21A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:39,107,680-39,138,903 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STI2, IFT139A, Thm2 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; MicroRNA protein coding host genes; IFT-A complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDW8](https://www.uniprot.org/uniprotkb/Q8NDW8) (Tetratricopeptide repeat protein 21A):

> Intraflagellar transport (IFT)-associated protein required for spermatogenesis. Required for sperm flagellar formation and intraflagellar transport.

**Summary**, from NCBI Gene [199223](https://www.ncbi.nlm.nih.gov/gene/199223):

> Involved in flagellated sperm motility and spermatid development. Predicted to be located in cilium. Predicted to be part of intraciliary transport particle A. Implicated in spermatogenic failure 37. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30761) · Entrez [199223](https://www.ncbi.nlm.nih.gov/gene/199223) · UniProt [Q8NDW8](https://www.uniprot.org/uniprotkb/Q8NDW8) · Ensembl [ENSG00000168026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168026)

## Data

Gene col 9583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9583); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9583]; `tensor/DDL_lfc|DDL_z.npy` [9583]; `embed/gene_vectors.npy` [9583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9583 or target_col == 9583). Every well: [[TTC21A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC21A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
