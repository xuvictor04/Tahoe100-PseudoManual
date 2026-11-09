---
symbol: "ATG13"
type: "gene"
col: 10586
ensembl_id: "ENSG00000175224"
name: "autophagy related 13"
location: "11p11.2"
module: 187
arm: "+"
pooled_cpm: 65.35
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# ATG13

*autophagy related 13* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.66× (z +9.6, q 2e-19, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.361× (z -14.5, q 1e-44, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.349× (z -7.8, q 6e-13, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HBP1]] (+0.59, fdr 4e-05), [[KLHDC2]] (+0.58, fdr 2e-04), [[INPP5K]] (+0.58, fdr 1e-05); moves opposite to [[GNPNAT1]] (-0.50, fdr 8e-05), [[NOC3L]] (-0.47, fdr 3e-05), [[MPHOSPH6]] (-0.45, fdr 6e-05).
> It is in [[Module 187]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.66×** | +9.6 | 2e-19 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.63×** | +9.6 | 2e-19 | 44/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +5.2 | 3e-05 | 30/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 0.001 | 30/48 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 0.001 | 27/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.003 | 28/49 (A498, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.361×** | -14.5 | 1e-44 | 48/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.556×** | -8.3 | 2e-14 | 43/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.563×** | -8.2 | 6e-14 | 43/48 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.572×** | -7.9 | 3e-13 | 39/49 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.349×** | -7.8 | 6e-13 | 46/48 (AsPC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.584×** | -7.6 | 2e-12 | 40/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.376×** | -7.3 | 3e-11 | 38/48 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.600×** | -7.0 | 2e-10 | 33/42 (HEC-1-A, SW48, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.403×** | -6.7 | 1e-09 | 41/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.717×** | -6.7 | 2e-09 | 32/49 (AsPC-1, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.417×** | -6.5 | 4e-09 | 41/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.727×** | -6.4 | 7e-09 | 37/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.435×** | -6.2 | 3e-08 | 40/48 (A-427, A498, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.691×** | -5.2 | 6e-06 | 35/48 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -5.2 | 8e-06 | 31/48 (A-427, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.794×** | -4.6 | 1e-04 | 26/48 (MIA PaCa-2, CHP-212, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.758×** | -3.7 | 0.005 | 29/48 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.011 | 25/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -3.4 | 0.014 | 24/48 (MIA PaCa-2, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.795×** | -3.2 | 0.026 | 23/49 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.645×** | -3.2 | 0.033 | 25/49 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.664×** | -3.0 | 0.048 | 18/47 (H4, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 72.0 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.206× (z -14.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.116× (z -10.3) |
| [[A498 (line)]] | wt | 94.4 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.351× (z -11.5) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 83.1 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -13.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0911× (z -10.3) |
| [[SW480 (line)]] | alt | 76.6 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.59× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.361× (z -11.3) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 78.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[AsPC-1 (line)]] | alt | 85.9 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.218× (z -13.8) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 69.2 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.47× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.249× (z -13.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 77.4 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 68.1 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -12.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 79.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 52.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[HT-29 (line)]] | alt | 87.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -9.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 59.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H460 (line)]] | wt | 39.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -11.9) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 52.3 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.297× (z -12.3) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 89.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[COLO 205 (line)]] | alt | 88.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.94× (z +8.9) | — |
| [[KATO III (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.264× (z -10.4) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 75.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.347× (z -9.3) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 66.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H661 (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[RKO (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.282× (z -9.5) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.249× (z -8.6) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 84.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.101× (z -8.6) |
| [[SW 900 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.204× (z -10.9) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 72.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HBP1]] | +0.59 | +0.42 / +0.69 | both halves | 4e-05 |  |
| [[KLHDC2]] | +0.58 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[INPP5K]] | +0.58 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[OTUD5]] | +0.57 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[IKZF5]] | +0.57 | +0.31 / +0.70 | both halves | 2e-04 |  |
| [[WDTC1]] | +0.57 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[TBC1D15]] | +0.56 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[UBN2]] | +0.56 | +0.24 / +0.65 | both halves | 5e-04 |  |
| [[MBTPS1]] | +0.55 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[WIPI2]] | +0.54 | +0.51 / +0.63 | both halves | 1e-05 | same gene group; pathway: Autophagy; STRING 854 |
| [[STX5]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ZER1]] | +0.52 | +0.39 / +0.59 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPNAT1]] | -0.50 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[NOC3L]] | -0.47 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[MPHOSPH6]] | -0.45 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[MYO1B]] | -0.44 | -0.24 / -0.39 | both halves | 4e-04 |  |
| [[ARF6]] | -0.44 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[CRYBG3]] | -0.43 | -0.21 / -0.49 | both halves | 6e-04 |  |
| [[SUPT3H]] | -0.43 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[INTS13]] | -0.43 | -0.22 / -0.48 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.8, -46.5); signed map (-16.1, 9.4). **Vector** length 92.5, 27.2% of its response variance represented; |z| ≥ 3 in 1,179 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.3 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +4.7 | -5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +4.6 | -7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +9.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.1 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | -0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | -0.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.3 | -14.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.6 | -7.8 |
|  | [[EX229 (drug)]] 5 µM |  | -7.3 | -7.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.3 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.3 | -6.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,617,527-46,674,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0652 |
| Gene groups (HGNC) | Autophagy related |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [O75143](https://www.uniprot.org/uniprotkb/O75143) (Autophagy-related protein 13):

> Autophagy factor required for autophagosome formation and mitophagy. Target of the TOR kinase signaling pathway that regulates autophagy through the control of the phosphorylation status of ATG13 and ULK1, and the regulation of the ATG13-ULK1-RB1CC1 complex. Through its regulation of ULK1 activity, plays a role in the regulation of the kinase activity of mTORC1 and cell proliferation.

**Summary**, from NCBI Gene [9776](https://www.ncbi.nlm.nih.gov/gene/9776):

> The protein encoded by this gene is an autophagy factor and a target of the TOR kinase signaling pathway. The encoded protein is essential for autophagosome formation and mitophagy. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:29091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29091) · Entrez [9776](https://www.ncbi.nlm.nih.gov/gene/9776) · UniProt [O75143](https://www.uniprot.org/uniprotkb/O75143) · Ensembl [ENSG00000175224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175224)

## Data

Gene col 10586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10586); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10586]; `tensor/DDL_lfc|DDL_z.npy` [10586]; `embed/gene_vectors.npy` [10586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10586 or target_col == 10586). Every well: [[ATG13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
