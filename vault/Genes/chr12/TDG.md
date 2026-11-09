---
symbol: "TDG"
type: "gene"
col: 6301
ensembl_id: "ENSG00000139372"
name: "thymine DNA glycosylase"
location: "12q23.3"
module: 89
arm: "+"
pooled_cpm: 58.62
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# TDG

*thymine DNA glycosylase* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +14.1, q 3e-42, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.760× (z -7.6, q 1e-11, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF444]] (+0.63, fdr 4e-05), [[TMEM216]] (+0.61, fdr 1e-05), [[EXO5-DT]] (+0.60, fdr 1e-05); moves opposite to [[KNTC1]] (-0.58, fdr 1e-05), [[EPB41L2]] (-0.55, fdr 3e-05), [[RBBP7]] (-0.54, fdr 2e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +14.1 | 3e-42 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +13.3 | 8e-38 | 37/48 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +12.1 | 3e-31 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +11.2 | 7e-27 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +10.5 | 8e-24 | 45/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +9.5 | 2e-19 | 41/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +8.5 | 1e-15 | 36/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +7.4 | 1e-11 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.2 | 4e-11 | 36/47 (RKO, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.4 | 8e-09 | 37/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +6.3 | 1e-08 | 32/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +5.3 | 6e-06 | 28/48 (NCI-H460, SW480, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.1 | 1e-05 | 26/48 (SNU-423, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.26×** | +4.7 | 1e-04 | 22/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 1e-03 | 20/48 (NCI-H460, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +4.2 | 1e-03 | 21/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.001 | 20/48 (MIA PaCa-2, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.005 | 19/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.021 | 18/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.024 | 18/48 (NCI-H1792, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -7.6 | 1e-11 | 34/49 (AsPC-1, CHP-212, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.710×** | -6.7 | 8e-09 | 20/41 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -5.7 | 3e-06 | 29/50 (AN3 CA, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.810×** | -4.3 | 0.003 | 19/48 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.827×** | -3.9 | 0.012 | 21/48 (SNU-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.828×** | -3.8 | 0.012 | 13/48 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.855× | -3.2 | 0.10 | 9/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.857× | -3.1 | 0.10 | 8/48 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.858× | -3.1 | 0.10 | 13/48 (KATO III, HS-578T, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.10 | 12/49 (Panc 03.27, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 79.3 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 66.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.4) | — |
| [[SW480 (line)]] | alt | 55.6 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.97× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 82.9 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.19× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 83.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -11.5) |
| [[KATO III (line)]] | alt | 54.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.69× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[LoVo (line)]] | wt | 74.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.81× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 63.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.80× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.0 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.95× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.71× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 38.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.86× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 58.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 67.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 65.6 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.90× (z +10.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 38.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.91× (z +18.2) | — |
| [[A549 (line)]] | wt | 56.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 75.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -9.0) |
| [[C32 (line)]] | wt | 29.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.24× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 54.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 56.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 59.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 53.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.66× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 53.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.71× (z +15.1) | — |
| [[J82 (line)]] | alt | 60.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 59.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +14.6) | — |
| [[Panc 03.27 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -16.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 44.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.88× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 57.2 | 0 | 1 | — | [[Pasireotide (acetate) (drug)]] 0.5 µM 0.0502× (z -11.0) |
| [[SW1417 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -11.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 63.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.45× (z +12.2) | — |
| [[A-172 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF444]] | +0.63 | +0.43 / +0.69 | both halves | 4e-05 |  |
| [[TMEM216]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[EXO5-DT]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[SPOP]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[SMN2]] | +0.59 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SLC30A5]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZNF383]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TIMM29]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TRIM4]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ZNF573]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PSMD5]] | +0.57 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[TVP23B]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KNTC1]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[RBBP7]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 | pathway: Epigenetic regulation of gene expression |
| [[NEMP1]] | -0.51 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[IQGAP1]] | -0.50 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[MCM6]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TDG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.4, -7.0); signed map (-13.1, -13.0). **Vector** length 86.9, 21.4% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.2 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.1 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +14.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +12.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.8 | -0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +1.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.9 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | thymine DNA glycosylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:103,965,822-103,988,874 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DNA glycosylases |
| Reactome | 13 pathways, smallest: TET1,2,3 and TDG demethylate DNA; Displacement of DNA glycosylase by APEX1; Cleavage of the damaged pyrimidine |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13569](https://www.uniprot.org/uniprotkb/Q13569) (G/T mismatch-specific thymine DNA glycosylase):

> DNA glycosylase that plays a key role in active DNA demethylation: specifically recognizes and binds 5-formylcytosine (5fC) and 5-carboxylcytosine (5caC) in the context of CpG sites and mediates their excision through base-excision repair (BER) to install an unmethylated cytosine. Cannot remove 5-hydroxymethylcytosine (5hmC). According to an alternative model, involved in DNA demethylation by mediating DNA glycolase activity toward 5-hydroxymethyluracil (5hmU) produced by deamination of 5hmC. …

**Summary**, from NCBI Gene [6996](https://www.ncbi.nlm.nih.gov/gene/6996):

> The protein encoded by this gene belongs to the TDG/mug DNA glycosylase family. Thymine-DNA glycosylase (TDG) removes thymine moieties from G/T mismatches by hydrolyzing the carbon-nitrogen bond between the sugar-phosphate backbone of DNA and the mispaired thymine. With lower activity, this enzyme also removes thymine from C/T and T/T mispairings. TDG can also remove uracil and 5-bromouracil from mispairings with guanine. This enzyme plays a central role in cellular defense against genetic …

**Accessions** — [HGNC:11700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11700) · Entrez [6996](https://www.ncbi.nlm.nih.gov/gene/6996) · UniProt [Q13569](https://www.uniprot.org/uniprotkb/Q13569) · Ensembl [ENSG00000139372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139372)

## Data

Gene col 6301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6301); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6301]; `tensor/DDL_lfc|DDL_z.npy` [6301]; `embed/gene_vectors.npy` [6301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6301 or target_col == 6301). Every well: [[TDG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
