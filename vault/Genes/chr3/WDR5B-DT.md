---
symbol: "WDR5B-DT"
type: "gene"
col: 15739
ensembl_id: "ENSG00000272758"
name: "WDR5B divergent transcript"
location: "3q21.1"
module: 38
arm: "+"
pooled_cpm: 25.46
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 30
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# WDR5B-DT

*WDR5B divergent transcript* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.09× (z +9.5, q 1e-18, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.444× (z -14.7, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD200R1]] (+0.71, fdr 7e-06), [[LRRC23]] (+0.68, fdr 7e-06), [[PYGM]] (+0.64, fdr 7e-06); moves opposite to [[SMC6]] (-0.59, fdr 1e-05), [[IDH3A]] (-0.52, fdr 2e-05), [[NSMCE4A]] (-0.51, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +9.5 | 1e-18 | 37/48 (LoVo, A-172, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.29×** | +5.6 | 7e-06 | 19/33 (A-172, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.34×** | +5.4 | 2e-05 | 28/48 (Panc 03.27, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.96×** | +4.5 | 9e-04 | 23/46 (SHP-77, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.012 | 22/48 (SW1417, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.34×** | +3.8 | 0.014 | 20/48 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.035 | 16/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +3.4 | 0.053 | 16/38 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.055 | 16/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.074 | 9/48 (J82, SHP-77, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.27× | +3.0 | 0.14 | 7/48 (LS 180, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.444×** | -14.7 | 0e+00 | 38/47 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.404×** | -11.6 | 1e-28 | 38/46 (C-33 A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.396×** | -11.4 | 6e-28 | 39/47 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.424×** | -11.0 | 6e-26 | 38/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.411×** | -10.9 | 8e-26 | 40/45 (C-33 A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -9.6 | 7e-20 | 36/47 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.478×** | -9.5 | 3e-19 | 37/48 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.567×** | -7.3 | 3e-11 | 36/47 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.603×** | -6.5 | 6e-09 | 29/45 (SK-MEL-2, J82, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.606×** | -6.4 | 8e-09 | 28/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.625×** | -6.0 | 1e-07 | 32/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.626×** | -6.0 | 1e-07 | 31/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.628×** | -6.0 | 1e-07 | 28/48 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.657×** | -5.4 | 3e-06 | 29/48 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -4.2 | 8e-04 | 20/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -4.1 | 0.001 | 16/47 (C-33 A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Carbamazepine (drug)]] 0.5 µM |  | **0.733×** | -4.0 | 0.002 | 20/47 (C-33 A, C32, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.764×** | -3.4 | 0.017 | 12/48 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.760×** | -3.4 | 0.020 | 18/45 (LS 180, SW1417, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.767×** | -3.2 | 0.030 | 17/47 (PANC-1, C32, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.616×** | -3.2 | 0.030 | 13/48 (A-427, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.773×** | -3.1 | 0.043 | 15/47 (SK-MEL-2, HOP62, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 50.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 54.3 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -12.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.4) |
| [[C-33 A (line)]] | alt | 53.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0266× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.7) |
| [[COLO 205 (line)]] | alt | 43.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -13.9) |
| [[J82 (line)]] | alt | 27.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 31.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.230× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.2) |
| [[KATO III (line)]] | alt | 28.7 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.238× (z -9.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.4) |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.5) |
| [[SHP-77 (line)]] | alt | 30.4 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.66× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.7) |
| [[SNU-423 (line)]] | alt | 32.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -14.1) |
| [[SW480 (line)]] | alt | 22.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.338× (z -9.1) |
| [[C32 (line)]] | wt | 53.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -13.0) |
| [[H4 (line)]] | wt | 51.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0743× (z -11.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.5) |
| [[HS-578T (line)]] | alt | 32.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.2) |
| [[A-172 (line)]] | wt | 24.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.11× (z +10.6) | — |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -9.5) |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -10.3) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 39.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0518× (z -10.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -9.0) |
| [[Hs 766T (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 25.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.98× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -10.0) |
| [[LoVo (line)]] | wt | 20.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.84× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -8.8) |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -11.2) |
| [[SW48 (line)]] | wt | 16.6 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.111× (z -8.6) |
| [[A498 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD200R1]] | +0.71 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LRRC23]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[PYGM]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CCDC181]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ECD]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[FAM209A]] | +0.62 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[LRP2BP]] | +0.61 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[EMC1-AS1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ARL9]] | +0.60 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[LDHC]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[VWCE]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC6]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[IDH3A]] | -0.52 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[NSMCE4A]] | -0.51 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[EFR3A]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.5, -18.7); signed map (14.2, 11.3). **Vector** length 121, 34.2% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.2 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.7 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.6 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.7 | -10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -14.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.7 | -9.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -11.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.8 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -0.5 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | WDR5B divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q21.1 — chr3:122,416,200-122,443,180 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55192) · Entrez [102723582](https://www.ncbi.nlm.nih.gov/gene/102723582) · Ensembl [ENSG00000272758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272758)

## Data

Gene col 15739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15739); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15739]; `tensor/DDL_lfc|DDL_z.npy` [15739]; `embed/gene_vectors.npy` [15739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15739 or target_col == 15739). Every well: [[WDR5B-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR5B-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
