---
symbol: "KLHL23"
type: "gene"
col: 13086
ensembl_id: "ENSG00000213160"
name: "kelch like family member 23"
location: "2q31.1"
module: 18
arm: "+"
pooled_cpm: 35.06
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# KLHL23

*kelch like family member 23* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.59× (z +8.8, q 5e-16, up in 33 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.47× (z +7.7, q 3e-12, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.549× (z -11.8, q 3e-29, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35G1]] (+0.67, fdr 7e-06), [[RNASEH2B]] (+0.61, fdr 2e-05), [[PM20D2]] (+0.60, fdr 2e-05); moves opposite to [[MSRB1]] (-0.55, fdr 3e-04), [[POMP]] (-0.48, fdr 7e-05), [[CHMP5]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FAM169A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +8.8 | 5e-16 | 33/46 (NCI-H1573, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +8.0 | 3e-13 | 22/39 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +7.7 | 3e-12 | 34/46 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.3 | 5e-08 | 22/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 1e-07 | 28/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.23×** | +5.7 | 9e-07 | 17/47 (J82, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +5.6 | 1e-06 | 22/47 (PANC-1, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.8 | 1e-04 | 22/47 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.7 | 2e-04 | 23/45 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +3.9 | 0.005 | 15/43 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.057 | 10/47 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.057 | 13/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.057 | 8/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.1 | 0.091 | 8/47 (HepG2/C3A, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -11.8 | 3e-29 | 32/46 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.327×** | -11.5 | 4e-28 | 38/47 (A-427, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.348×** | -10.9 | 3e-25 | 37/47 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.566×** | -10.6 | 5e-24 | 39/47 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -10.3 | 5e-23 | 32/46 (NCI-H23, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.592×** | -10.3 | 6e-23 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.632×** | -9.0 | 1e-17 | 37/47 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.739×** | -5.9 | 2e-07 | 23/47 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.568×** | -5.8 | 4e-07 | 28/41 (HEC-1-A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.762×** | -5.1 | 2e-05 | 23/47 (NCI-H23, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **0.769×** | -5.0 | 4e-05 | 20/46 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.787×** | -4.7 | 1e-04 | 25/46 (SNU-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.859× | -4.2 | 0.001 | 18/46 (HEC-1-A, COLO 205, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.756×** | -3.9 | 0.004 | 11/47 (C-33 A, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.842× | -3.4 | 0.029 | 20/47 (NCI-H460, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 64.6 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.402× (z -10.2) |
| [[C-33 A (line)]] | alt | 145 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -23.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 45.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.231× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 56.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -9.0) |
| [[PANC-1 (line)]] | alt | 25.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -11.9) |
| [[SW480 (line)]] | alt | 53.8 | 0 | 4 | — | [[TAK-901 (drug)]] 5 µM 0.151× (z -12.0) |
| [[LoVo (line)]] | wt | 52.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +11.8) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 0.5 µM 0.478× (z -8.6) |
| [[A-427 (line)]] | wt | 57.7 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0970× (z -12.4) |
| [[BT-474 (line)]] | alt | 34.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -13.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.265× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 50.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 56.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.199× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 77.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HOP62 (line)]] | alt | 26.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +21.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.288× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -14.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0261× (z -11.6) |
| [[SNU-423 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35G1]] | +0.67 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[RNASEH2B]] | +0.61 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[PM20D2]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[GCFC2]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SNX5]] | +0.54 | +0.62 / +0.29 | both halves | 3e-04 |  |
| [[TXNRD3]] | +0.54 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | +0.54 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[CENPV]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PAXIP1]] | +0.53 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[SNHG26]] | +0.53 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[ZC3HAV1L]] | +0.53 | +0.34 / +0.32 | both halves | 2e-04 |  |
| [[ANKRD18A]] | +0.51 | +0.57 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSRB1]] | -0.55 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[POMP]] | -0.48 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[CHMP5]] | -0.47 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[COX5B]] | -0.46 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[DCTN3]] | -0.46 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[CCNK]] | -0.45 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[RNF181]] | -0.45 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[VRK3]] | -0.45 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[TOX4]] | -0.45 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[MRPL55]] | -0.45 | -0.54 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[PSMD13]] | -0.44 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[SNX29]] | -0.44 | -0.36 / -0.25 | both halves | 4e-04 |  |
| [[PMM1]] | -0.44 | -0.34 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | FAM169A activity raises KLHL23's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without FAM169A | 0.025 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[NUP210]] | B | NUP210 activity raises KLHL23's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without NUP210 | 0.028 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[FTCDNL1]] | B | FTCDNL1 activity raises KLHL23's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without FTCDNL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[ULK2]] | B | ULK2 activity raises KLHL23's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.21× lower at baseline in the lines without ULK2 | 0.066 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-2.3, 6.6); signed map (22.2, -33.5). **Vector** length 83.6, 18.2% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.5 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.9 | +7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.8 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +0.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -10.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -9.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -11.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -11.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,694,488-169,776,989 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2610, FLJ37812, MGC22679 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q8NBE8](https://www.uniprot.org/uniprotkb/Q8NBE8) carries no function annotation.

**Summary**, from NCBI Gene [151230](https://www.ncbi.nlm.nih.gov/gene/151230):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27506) · Entrez [151230](https://www.ncbi.nlm.nih.gov/gene/151230) · UniProt [Q8NBE8](https://www.uniprot.org/uniprotkb/Q8NBE8) · Ensembl [ENSG00000213160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213160)

## Data

Gene col 13086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13086); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13086]; `tensor/DDL_lfc|DDL_z.npy` [13086]; `embed/gene_vectors.npy` [13086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13086 or target_col == 13086). Every well: [[KLHL23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
