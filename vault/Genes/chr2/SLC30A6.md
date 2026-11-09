---
symbol: "SLC30A6"
type: "gene"
col: 7649
ensembl_id: "ENSG00000152683"
name: "solute carrier family 30 member 6"
location: "2p22.3"
module: 142
arm: "+"
pooled_cpm: 51.45
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# SLC30A6

*solute carrier family 30 member 6* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.60× (z +7.2, q 3e-10, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change.
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.454× (z -14.2, q 4e-43, down in 45 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.403× (z -8.5, q 1e-15, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR89A]] (+0.77, fdr 7e-06), [[RARS2]] (+0.72, fdr 7e-06), [[XPNPEP3]] (+0.71, fdr 7e-06); moves opposite to [[TBL1XR1]] (-0.66, fdr 1e-05), [[AHR]] (-0.62, fdr 7e-06), [[TMEM14C]] (-0.61, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ID2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.60×** | +7.2 | 3e-10 | 39/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.19× | +3.2 | 0.27 | 20/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.27 | 20/48 (NCI-H1573, C32, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.454×** | -14.2 | 4e-43 | 45/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.458×** | -14.0 | 3e-42 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.605×** | -12.8 | 4e-35 | 34/47 (A-427, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.579×** | -9.8 | 1e-20 | 38/49 (A-427, NCI-H460, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.592×** | -9.1 | 1e-17 | 34/47 (COLO 205, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.600×** | -8.9 | 8e-17 | 37/48 (NCI-H460, H4, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -8.5 | 1e-15 | 41/49 (A-427, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.615×** | -8.1 | 4e-14 | 33/44 (A-427, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.588×** | -7.9 | 2e-13 | 39/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.637×** | -6.7 | 1e-09 | 30/48 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.699×** | -6.2 | 3e-08 | 26/42 (HCT15, SW480, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.556×** | -5.5 | 2e-06 | 26/48 (A-427, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.754×** | -5.1 | 2e-05 | 29/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.774×** | -4.6 | 2e-04 | 23/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -4.3 | 6e-04 | 19/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.010 | 18/48 (NCI-H460, AN3 CA, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.826×** | -3.4 | 0.019 | 19/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.823×** | -3.4 | 0.022 | 23/48 (SK-MEL-2, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.2 | 0 | 12 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -19.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 72.5 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 59.1 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -21.6) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0394× (z -19.2) |
| [[HOP62 (line)]] | alt | 57.1 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 57.5 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -17.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 72.9 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.286× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 57.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 49.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -16.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[KATO III (line)]] | alt | 72.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 44.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 45.7 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -13.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 72.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -20.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[MIA PaCa-2 (line)]] | alt | 68.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SHP-77 (line)]] | alt | 56.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 49.1 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -13.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 48.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 46.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 55.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 42.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 32.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0963× (z -14.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.3) ⚠ cell-cycle shift, explains ~69% of this change |
| [[HT-29 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 36.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.384× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.343× (z -9.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H1792 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H2030 (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.335× (z -9.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H23 (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 0.05 µM 0.0568× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 61.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-423 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.1) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A-172 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89A]] | +0.77 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[RARS2]] | +0.72 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[XPNPEP3]] | +0.71 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[GPR89B]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[ZCCHC17]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[CCDC32]] | +0.69 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[ORC3]] | +0.69 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[ZBTB49]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RABEPK]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[NUP214]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CWF19L1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[RINT1]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBL1XR1]] | -0.66 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[AHR]] | -0.62 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[TMEM14C]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ALCAM]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[BMI1]] | -0.59 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[STIM2]] | -0.58 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[ID2-AS1]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[KAT6A]] | -0.57 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[JUNB]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PLCB4]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CXADR]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | B | ID2-AS1 activity raises SLC30A6's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without ID2-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, -5.0); signed map (-44.8, 4.2). **Vector** length 99.3, 26.6% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | +8.1 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +7.4 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.4 | +1.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.9 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -5.3 | -12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -4.3 | -6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 30 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:32,165,841-32,224,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31101, ZNT6 |
| Gene groups (HGNC) | Solute carrier family 30 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NXT4](https://www.uniprot.org/uniprotkb/Q6NXT4) (Zinc transporter 6):

> Has probably no intrinsic transporter activity but together with SLC30A5 forms a functional zinc ion:proton antiporter heterodimer, mediating zinc entry into the lumen of organelles along the secretory pathway. As part of that zinc ion:proton antiporter, contributes to zinc ion homeostasis within the early secretory pathway and regulates the activation and folding of enzymes like alkaline phosphatases and enzymes involved in phosphatidylinositol glycan anchor biosynthesis.

**Summary**, from NCBI Gene [55676](https://www.ncbi.nlm.nih.gov/gene/55676):

> This gene encodes a member of a family of proteins that function as zinc transporters. This protein can regulate subcellular levels of zinc in the Golgi and vesicles. Expression of this gene is altered in the Alzheimer's disease brain plaques. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:19305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19305) · Entrez [55676](https://www.ncbi.nlm.nih.gov/gene/55676) · UniProt [Q6NXT4](https://www.uniprot.org/uniprotkb/Q6NXT4) · Ensembl [ENSG00000152683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152683)

## Data

Gene col 7649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7649); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7649]; `tensor/DDL_lfc|DDL_z.npy` [7649]; `embed/gene_vectors.npy` [7649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7649 or target_col == 7649). Every well: [[SLC30A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC30A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
