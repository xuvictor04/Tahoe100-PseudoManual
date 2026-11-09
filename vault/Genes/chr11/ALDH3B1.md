---
symbol: "ALDH3B1"
type: "gene"
col: 115
ensembl_id: "ENSG00000006534"
name: "aldehyde dehydrogenase 3 family member B1"
location: "11q13.2"
module: 81
arm: "+"
pooled_cpm: 9.0
n_lines_expressing: 41
n_dd_up: 22
n_dd_down: 36
n_dd_up_clean: 18
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 12
direction_downstream: 48
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# ALDH3B1

*aldehyde dehydrogenase 3 family member B1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.21× (z +7.3, q 1e-10, up in 11 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 2.46× (z +4.5, q 9e-04, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.300× (z -11.5, q 5e-28, down in 31 of 38 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.446× (z -10.9, q 2e-25, down in 28 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDLIM1]] (+0.62, fdr 7e-06), [[VAPA]] (+0.62, fdr 8e-06), [[TNS3]] (+0.60, fdr 1e-05); moves opposite to [[TMEM158]] (-0.61, fdr 1e-05), [[KIAA1549L]] (-0.59, fdr 1e-05), [[ANTXR2]] (-0.56, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CDCP1]] → it (grade B ⚠); 48 go from it, the strongest it → [[MYOF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.3 | 1e-10 | 11/20 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.7 | 4e-06 | 18/28 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **2.46×** | +4.5 | 9e-04 | 16/30 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 9e-04 | 18/38 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +4.4 | 9e-04 | 11/24 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.91×** | +4.4 | 9e-04 | 19/34 (NCI-H460, NCI-H2347, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 0.001 | 18/38 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 0.001 | 15/38 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +4.2 | 0.002 | 16/38 (J82, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 14/34 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.54×** | +4.1 | 0.002 | 13/35 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.005 | 17/38 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 13/39 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.62×** | +3.7 | 0.010 | 12/37 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.010 | 13/37 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.013 | 13/38 (Panc 03.27, NCI-H2347, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.013 | 14/39 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.96×** | +3.4 | 0.023 | 13/31 (J82, A549, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.300×** | -11.5 | 5e-28 | 31/38 (Hs 766T, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.446×** | -10.9 | 2e-25 | 28/34 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.354×** | -10.0 | 4e-21 | 31/37 (SW1417, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.487×** | -9.8 | 2e-20 | 25/37 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.377×** | -9.4 | 1e-18 | 30/37 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.385×** | -9.1 | 6e-18 | 33/38 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.387×** | -9.1 | 8e-18 | 26/33 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.399×** | -8.8 | 9e-17 | 27/36 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.441×** | -7.9 | 3e-13 | 25/36 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.462×** | -7.4 | 8e-12 | 24/35 (HCT15, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.517×** | -6.1 | 6e-08 | 23/35 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.586×** | -5.1 | 1e-05 | 17/33 (LS 180, Panc 03.27, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.580×** | -5.0 | 2e-05 | 21/32 (Hs 766T, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.599×** | -4.9 | 4e-05 | 22/34 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.606×** | -4.8 | 6e-05 | 21/38 (SW1417, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.559×** | -4.4 | 3e-04 | 16/35 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -4.3 | 6e-04 | 16/36 (HT-29, SW1417, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.733×** | -4.2 | 8e-04 | 18/39 (Panc 03.27, MIA PaCa-2, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.656×** | -4.0 | 0.002 | 20/37 (Hs 766T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -3.9 | 0.003 | 17/37 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -3.5 | 0.009 | 16/34 (Hs 766T, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.66 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 24.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -20.2) |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 8 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.118× (z -13.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.7) |
| [[A549 (line)]] | wt | 43.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.2) |
| [[Hs 766T (line)]] | wt | 26.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0819× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0325× (z -14.0) |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0841× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 11.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -10.5) |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.9) |
| [[HS-578T (line)]] | alt | 6.85 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0575× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 13.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 8.16 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.08× (z +10.1) ⚠ position not correctable | — |
| [[NCI-H1573 (line)]] | alt | 6.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -10.6) |
| [[PANC-1 (line)]] | alt | 4.32 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.259× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.4) |
| [[SW480 (line)]] | alt | 4.90 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0470× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[VAPA]] | +0.62 | +0.58 / +0.57 | both halves | 8e-06 | pathway: Sphingolipid metabolism |
| [[TNS3]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[B4GALT1]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[PLAC8]] | +0.56 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[GPRIN2]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MUC1]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[HAVCR1]] | +0.53 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[AKR1C3]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[EPS8]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[PLA2R1]] | +0.53 | +0.51 / +0.37 | both halves | 7e-05 |  |
| [[ARAF]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[KIAA1549L]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ANTXR2]] | -0.56 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SNX14]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ZNF710]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[PYGL]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[BLZF2P]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CSNK1E]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SPRY4-AS1]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[UBASH3B]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CORO2B]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ARHGAP22]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | CDCP1 activity raises ALDH3B1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without CDCP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[MYOF]] | B | MYOF activity raises ALDH3B1's level | lines that do not express MYOF (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without MYOF | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[DPP4]] | B | DPP4 activity raises ALDH3B1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without DPP4 | 0.029 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[PDLIM1]] | B | PDLIM1 activity raises ALDH3B1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.26× lower at baseline in the lines without PDLIM1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[TOP2A]] | B | TOP2A activity raises ALDH3B1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PDK4]] | B | PDK4 activity strengthens ALDH3B1's drug response | lines that do not express PDK4 (20) vs lines expressing it (19) | the lines without PDK4 respond 0.60× as strongly (z diff +2.07); strongest at Digitoxin 5 µM: 0.47x vs 0.23x (z diff +3.4) | 0.063 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA; target measured in part of the lines; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers ALDH3B1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[TM4SF4]] | B | TM4SF4 activity raises ALDH3B1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.31× lower at baseline in the lines without TM4SF4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[POU5F1]] | B | POU5F1 activity raises ALDH3B1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without POU5F1 | 0.089 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6 |
| [[AKR1C3]] | B | AKR1C3 activity raises ALDH3B1's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without AKR1C3 | 0.090 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[SPTLC3]] | B | SPTLC3 activity raises ALDH3B1's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without SPTLC3 | 0.091 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[TNS3]] | C | TNS3 activity raises ALDH3B1's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 3.11× lower at baseline in the lines without TNS3 | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX; co-absent with the target |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 47, C 1. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOF]] | B | ALDH3B1 activity raises MYOF's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.82× lower at baseline in the lines without ALDH3B1 | 0.007 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[PBX3]] | B | ALDH3B1 activity lowers PBX3's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.89× higher at baseline in the lines without ALDH3B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ITGA2]] | B | ALDH3B1 activity raises ITGA2's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 4.41× lower at baseline in the lines without ALDH3B1 | 0.010 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[B4GALT1]] | B | ALDH3B1 activity raises B4GALT1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.14× lower at baseline in the lines without ALDH3B1 | 0.013 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ORAI1]] | B | ALDH3B1 activity lowers ORAI1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 1.43× higher at baseline in the lines without ALDH3B1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[CDCP1]] | B | ALDH3B1 activity raises CDCP1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 4.25× lower at baseline in the lines without ALDH3B1 | 0.024 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[B4GALT6]] | B | ALDH3B1 activity lowers B4GALT6's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 1.78× higher at baseline in the lines without ALDH3B1 | 0.034 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| cells under [[Mebendazole (drug)]] 5 µM | B | ALDH3B1 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.61× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[SPTLC3]] | B | ALDH3B1 activity raises SPTLC3's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.33× lower at baseline in the lines without ALDH3B1 | 0.041 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| cells under [[Infigratinib (drug)]] 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.82× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | B | ALDH3B1 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.26× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.74× the cells of the other lines | 0.049 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction -0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.6, 4.3); signed map (50.9, 13.5). **Vector** length 84.4, 20.7% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +4.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.4 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.1 | +4.5 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.3 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.3 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 3 family member B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:68,008,578-68,029,282 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ALDH7 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 5 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P43353](https://www.uniprot.org/uniprotkb/P43353) (Aldehyde dehydrogenase family 3 member B1):

> Oxidizes medium and long chain saturated and unsaturated fatty aldehydes generated in the plasma membrane into non-toxic fatty acids. May have a protective role against the cytotoxicity induced by lipid peroxidation. Short-chain fatty aldehydes are not good substrates. Can use both NADP(+) and NAD(+) as electron acceptor in vitro, however in vivo preference will depend on their tissue levels. Low activity towards acetaldehyde and 3,4-dihydroxyphenylacetaldehyde. Able to metabolize aromatic …

**Summary**, from NCBI Gene [221](https://www.ncbi.nlm.nih.gov/gene/221):

> This gene encodes a member of the aldehyde dehydrogenase protein family. Aldehyde dehydrogenases are a family of isozymes that may play a major role in the detoxification of aldehydes generated by alcohol metabolism and lipid peroxidation. The encoded protein is able to oxidize long-chain fatty aldehydes in vitro, and may play a role in protection from oxidative stress. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:410) · Entrez [221](https://www.ncbi.nlm.nih.gov/gene/221) · UniProt [P43353](https://www.uniprot.org/uniprotkb/P43353) · Ensembl [ENSG00000006534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006534)

## Data

Gene col 115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 115); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 115]; `tensor/DDL_lfc|DDL_z.npy` [115]; `embed/gene_vectors.npy` [115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 115 or target_col == 115). Every well: [[ALDH3B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH3B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
