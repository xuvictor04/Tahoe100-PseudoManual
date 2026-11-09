---
symbol: "BUD23"
type: "gene"
col: 984
ensembl_id: "ENSG00000071462"
name: "BUD23 rRNA methyltransferase and ribosome maturation factor"
location: "7q11.23"
module: 16
arm: "-"
pooled_cpm: 56.68
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# BUD23

*BUD23 rRNA methyltransferase and ribosome maturation factor* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (22 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +11.9, q 5e-30, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.673× (z -4.2, q 0.013, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN15]] (+0.61, fdr 1e-05), [[SMG1P2]] (+0.61, fdr 1e-05), [[MAD1L1]] (+0.58, fdr 3e-05); moves opposite to [[UBQLN2]] (-0.63, fdr 3e-05), [[CLK4]] (-0.62, fdr 3e-05), [[GOPC]] (-0.62, fdr 3e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TFR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 22 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +11.9 | 5e-30 | 47/48 (KATO III, A-172, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.76×** | +11.3 | 4e-27 | 46/48 (C32, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.40×** | +9.7 | 5e-20 | 46/48 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **2.38×** | +9.6 | 1e-19 | 39/47 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.34×** | +9.4 | 4e-19 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.24×** | +9.0 | 3e-17 | 48/48 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.06×** | +8.0 | 8e-14 | 48/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.15×** | +7.9 | 2e-13 | 37/44 (A-172, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **2.09×** | +7.8 | 3e-13 | 29/41 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.83×** | +6.7 | 1e-09 | 43/48 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +5.6 | 9e-07 | 41/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.66×** | +5.6 | 1e-06 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.6 | 1e-06 | 35/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.69×** | +5.6 | 1e-06 | 36/49 (A-427, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +5.5 | 2e-06 | 41/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +5.4 | 3e-06 | 40/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +5.3 | 3e-06 | 31/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +4.3 | 4e-04 | 35/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.81×** | +3.4 | 0.013 | 23/48 (NCI-H1792, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.016 | 27/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.019 | 27/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.74×** | +3.2 | 0.026 | 25/48 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.037 | 23/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.042 | 18/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +2.9 | 0.058 | 19/48 (CFPAC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.44×** | +2.9 | 0.058 | 20/48 (NCI-H460, LOX-IMVI, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +2.9 | 0.058 | 20/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.673×** | -4.2 | 0.013 | 29/47 (SW 900, A-427, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.530×** | -3.7 | 0.061 | 33/49 (SW 900, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.798×** | -3.5 | 0.084 | 28/48 (NCI-H23, SW 900, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.555×** | -3.4 | 0.084 | 30/49 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.744×** | -3.3 | 0.093 | 25/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.711×** | -3.3 | 0.093 | 27/49 (MIA PaCa-2, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.758× | -3.1 | 0.17 | 21/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.1 | 9 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.78× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.97× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 45.0 | 8 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +11.9) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H1792 (line)]] | alt | 44.8 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.7) | — |
| [[SW480 (line)]] | alt | 51.3 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.93× (z +9.7) | — |
| [[KATO III (line)]] | alt | 82.3 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.6) | — |
| [[LoVo (line)]] | wt | 57.6 | 5 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 69.7 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +12.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[AsPC-1 (line)]] | alt | 57.5 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.47× (z +11.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 30.7 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.8) | — |
| [[A-172 (line)]] | wt | 49.2 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.98× (z +11.1) | — |
| [[A549 (line)]] | wt | 40.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[H4 (line)]] | wt | 44.9 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.70× (z +10.2) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A498 (line)]] | wt | 91.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[C32 (line)]] | wt | 74.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.82× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 53.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.13× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 58.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 44.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[NCI-H23 (line)]] | alt | 55.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.22× (z +9.0) | — |
| [[A-427 (line)]] | wt | 59.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 61.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.33× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 79.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.87× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 48.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 47.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 93.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.86× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 54.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.10× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN15]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SMG1P2]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MAD1L1]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[DNAJC5]] | +0.58 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[PTDSS1]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 450 |
| [[SLC27A4]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MFN1]] | +0.57 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[PMPCA]] | +0.56 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SERGEF]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[NCLN]] | +0.55 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[CORO7]] | +0.54 | +0.33 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN2]] | -0.63 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[CLK4]] | -0.62 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[GOPC]] | -0.62 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[CFL2]] | -0.59 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[COPS5]] | -0.57 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.56 | -0.30 / -0.62 | both halves | 2e-04 |  |
| [[VPS72]] | -0.56 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[TAB2]] | -0.56 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SMARCE1]] | -0.55 | -0.29 / -0.63 | both halves | 2e-04 |  |
| [[NDUFA5]] | -0.55 | -0.43 / -0.53 | both halves | 4e-05 |  |
| [[CHURC1]] | -0.54 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[XRN1]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFR2]] | B | TFR2 activity raises BUD23's level | lines that do not express TFR2 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without TFR2 | 0.031 | ⚠ within organs, on part of the lines; also absent: KRTAP5-AS1, EFNA2, AP1G2; maybe low, not absent |
| [[WNK2]] | B | WNK2 activity raises BUD23's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.20× lower at baseline in the lines without WNK2 | 0.073 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.5, 8.1); signed map (-47.1, 23.8). **Vector** length 58.6, 16.6% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +11.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +1.8 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.4 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.7 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.7 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | BUD23 rRNA methyltransferase and ribosome maturation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,683,597-73,698,212 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC19709, MGC2022, MGC5140, PP3381, WBMT, MERM1; previously WBSCR22 |
| Gene groups (HGNC) | Ribosome biogenesis factors; 7BS N7-guanosine RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O43709](https://www.uniprot.org/uniprotkb/O43709) (18S rRNA):

> S-adenosyl-L-methionine-dependent methyltransferase that specifically methylates the N(7) position of a guanine in 18S rRNA. Requires the methyltransferase adapter protein TRM112 for full rRNA methyltransferase activity. Involved in the pre-rRNA processing steps leading to small-subunit rRNA production independently of its RNA-modifying catalytic activity. Important for biogenesis end export of the 40S ribosomal subunit independent on its methyltransferase activity. Locus-specific steroid …

**Summary**, from NCBI Gene [114049](https://www.ncbi.nlm.nih.gov/gene/114049):

> This gene encodes a protein containing a nuclear localization signal and an S-adenosyl-L-methionine binding motif typical of methyltransferases, suggesting that the encoded protein may act on DNA methylation. This gene is deleted in Williams syndrome, a multisystem developmental disorder caused by the deletion of contiguous genes at 7q11.23. Alternatively spliced transcript variants have been found. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:16405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16405) · Entrez [114049](https://www.ncbi.nlm.nih.gov/gene/114049) · UniProt [O43709](https://www.uniprot.org/uniprotkb/O43709) · Ensembl [ENSG00000071462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071462)

## Data

Gene col 984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 984); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 984]; `tensor/DDL_lfc|DDL_z.npy` [984]; `embed/gene_vectors.npy` [984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 984 or target_col == 984). Every well: [[BUD23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BUD23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
