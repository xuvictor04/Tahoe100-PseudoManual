---
symbol: "STAG3L5P-1"
type: "gene"
col: 16496
ensembl_id: "ENSG00000290682"
name: ""
location: ""
module: 67
arm: "+"
pooled_cpm: 75.77
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# STAG3L5P-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +13.2, q 5e-37, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.540× (z -10.8, q 1e-24, down in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.709× (z -6.0, q 3e-07, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PILRB]] (+0.71, fdr 7e-06, ⚠ same locus), [[CHEK2]] (+0.57, fdr 3e-05), [[MPHOSPH9]] (+0.56, fdr 1e-05), [[IFT122]] (+0.56, fdr 2e-05); moves opposite to [[PAM]] (-0.44, fdr 2e-04), [[RNF6]] (-0.44, fdr 5e-04), [[RCAN1]] (-0.44, fdr 3e-04).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +13.2 | 5e-37 | 38/48 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +9.0 | 6e-17 | 40/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +7.5 | 2e-11 | 38/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +6.1 | 2e-07 | 29/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.0 | 2e-07 | 32/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.0 | 3e-07 | 34/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.8 | 7e-07 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 3e-05 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.68×** | +4.8 | 1e-04 | 34/49 (SW480, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.5 | 3e-04 | 23/48 (C32, HOP62, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.012 | 24/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.012 | 24/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.013 | 20/48 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.018 | 6/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.020 | 17/49 (HOP62, A-172, …) | top dose only |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.093 | 15/49 (SW480, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.100 | 14/48 (RKO, COLO 205, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.540×** | -10.8 | 1e-24 | 34/49 (A-427, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -6.2 | 1e-07 | 26/44 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -6.0 | 3e-07 | 32/48 (A498, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.658×** | -5.9 | 6e-07 | 26/45 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.717×** | -5.9 | 6e-07 | 30/48 (SW 1271, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -5.4 | 5e-06 | 0/49 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.779×** | -4.4 | 9e-04 | 28/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.665×** | -3.8 | 0.012 | 25/47 (HCT15, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.827×** | -3.3 | 0.052 | 20/48 (A-427, AN3 CA, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.833×** | -3.2 | 0.075 | 16/48 (NCI-H1792, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.1 | 11 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +24.9) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 93.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -10.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 61.9 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 64.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 116 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +19.0) | — |
| [[NCI-H23 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -26.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 67.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0790× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.369× (z -9.9) |
| [[A498 (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 58.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 58.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -15.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 72.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -18.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 81.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -9.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 81.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 70.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +18.2) | — |
| [[RKO (line)]] | wt | 87.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -22.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 96.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -10.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 84.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.199× (z -9.4) |
| [[BT-474 (line)]] | alt | 85.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.4) | — |
| [[CFPAC-1 (line)]] | alt | 50.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.8) | — |
| [[H4 (line)]] | wt | 91.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +16.1) | — |
| [[HEC-1-A (line)]] | alt | 69.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 64.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 69.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 75.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 55.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 54.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.3) | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0963× (z -11.3) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRB]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.3 kb, same strand: neighbours can correlate without regulation) |
| [[CHEK2]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[MPHOSPH9]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[IFT122]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[MIS18BP1]] | +0.55 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[STIL]] | +0.51 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CEP85]] | +0.51 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[AURKB]] | +0.50 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[TOP2A]] | +0.50 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[CEP70]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[TTK]] | +0.50 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[CNTROB]] | +0.49 | +0.51 / +0.27 | both halves | 3e-04 |  |
| [[KIF2C]] | +0.49 | +0.52 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAM]] | -0.44 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[RNF6]] | -0.44 | -0.24 / -0.38 | both halves | 5e-04 |  |
| [[RCAN1]] | -0.44 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[ZNF343]] | -0.43 | -0.42 / -0.23 | both halves | 5e-04 |  |
| [[GRPEL1]] | -0.42 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[PLAC8L1]] | -0.42 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[EAF1]] | -0.41 | -0.27 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises STAG3L5P-1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without NEURL1B | 0.046 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.6, -53.9); signed map (-46.2, -39.0). **Vector** length 88.4, 20.5% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.2 | +7.5 |
|  | [[NG25 (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +13.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.3 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | -1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | +1.8 |

## What is on record

> [!warning] No registry record
> STAG3L5P-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16496); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16496]; `tensor/DDL_lfc|DDL_z.npy` [16496]; `embed/gene_vectors.npy` [16496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16496 or target_col == 16496). Every well: [[STAG3L5P-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAG3L5P-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
