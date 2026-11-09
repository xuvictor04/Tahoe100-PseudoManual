---
symbol: "TXNDC12"
type: "gene"
col: 3952
ensembl_id: "ENSG00000117862"
name: "thioredoxin domain containing 12"
location: "1p32.3"
module: 63
arm: "+"
pooled_cpm: 66.63
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# TXNDC12

*thioredoxin domain containing 12* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +11.7, q 8e-29, up in 29 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.30× (z +5.9, q 4e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.588× (z -17.0, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOT1]] (+0.65, fdr 7e-06), [[SLC31A1]] (+0.65, fdr 7e-06), [[MTHFD2]] (+0.64, fdr 1e-05); moves opposite to [[TRIM47]] (-0.65, fdr 1e-05), [[METTL18]] (-0.58, fdr 3e-05), [[SDSL]] (-0.57, fdr 4e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TRIP6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[IARS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.71×** | +11.7 | 8e-29 | 29/42 (HEC-1-A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.56×** | +10.1 | 2e-21 | 40/48 (A549, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.46×** | +8.6 | 2e-15 | 31/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.45×** | +8.4 | 9e-15 | 31/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.42×** | +7.9 | 3e-13 | 34/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.9 | 4e-07 | 32/48 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.17× | +5.0 | 4e-05 | 25/48 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +4.7 | 2e-04 | 22/48 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +4.6 | 2e-04 | 23/48 (NCI-H2030, Panc 03.27, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.23×** | +4.6 | 3e-04 | 23/49 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.22×** | +4.2 | 0.001 | 20/44 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.12× | +3.7 | 0.012 | 7/48 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.013 | 13/48 (A-427, C-33 A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.5 | 0.022 | 19/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.16× | +3.4 | 0.022 | 20/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.4 | 0.024 | 17/48 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.046 | 0/49 | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.062 | 14/48 (HOP62, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.588×** | -17.0 | 0e+00 | 44/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.524×** | -14.1 | 2e-42 | 44/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.560×** | -13.1 | 4e-37 | 42/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.611×** | -11.2 | 8e-27 | 43/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.699×** | -8.1 | 5e-14 | 34/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.772×** | -5.6 | 2e-06 | 24/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.814×** | -4.7 | 3e-04 | 24/48 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.826×** | -4.2 | 0.002 | 23/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.832×** | -3.9 | 0.007 | 19/47 (LoVo, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.891× | -3.6 | 0.015 | 11/48 (RKO, PANC-1, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.847× | -3.6 | 0.020 | 17/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.857× | -3.5 | 0.020 | 13/47 (SNU-423, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.852× | -3.5 | 0.020 | 17/49 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.764×** | -3.2 | 0.057 | 10/49 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.765×** | -3.2 | 0.057 | 18/45 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.065 | 5/48 (Panc 03.27, J82, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.909× | -3.1 | 0.070 | 5/48 (SNU-423, A-427, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.870× | -3.0 | 0.072 | 16/48 (A-427, NCI-H23, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 99.8 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -20.7) |
| [[A-172 (line)]] | wt | 39.3 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Harringtonine (drug)]] 5 µM 0.431× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 57.3 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 144 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -24.8) |
| [[A498 (line)]] | wt | 71.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -17.1) |
| [[HT-29 (line)]] | alt | 74.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -17.2) |
| [[KATO III (line)]] | alt | 93.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.5) |
| [[RKO (line)]] | wt | 75.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -19.4) |
| [[C-33 A (line)]] | alt | 80.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 55.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -9.7) |
| [[A549 (line)]] | wt | 41.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[AsPC-1 (line)]] | alt | 35.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HepG2_C3A (line)]] | wt | 66.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -18.0) |
| [[HS-578T (line)]] | alt | 63.3 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.2) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 95.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 34.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[AN3 CA (line)]] | alt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -8.6) |
| [[C32 (line)]] | wt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CFPAC-1 (line)]] | alt | 62.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -8.7) |
| [[H4 (line)]] | wt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.3) |
| [[HCT15 (line)]] | alt | 82.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.0) |
| [[HOP62 (line)]] | alt | 57.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.446× (z -8.6) |
| [[J82 (line)]] | alt | 63.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -11.7) |
| [[LoVo (line)]] | wt | 54.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[LOX-IMVI (line)]] | wt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2030 (line)]] | alt | 80.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 47.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SHP-77 (line)]] | alt | 64.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.4) |
| [[SNU-423 (line)]] | alt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -8.7) |
| [[SW 900 (line)]] | alt | 46.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.8) |
| [[BT-474 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 73.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOT1]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.64 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SOCS7]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SLC1A5]] | +0.60 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[ASNS]] | +0.59 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[SEL1L]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MTFR1]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[TM9SF3]] | +0.59 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[ODF2]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LONP1]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.65 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[METTL18]] | -0.58 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[SDSL]] | -0.57 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ZNF747]] | -0.56 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[TRIP6]] | -0.56 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[ZNF620]] | -0.55 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[MYL5]] | -0.55 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[CPLANE1]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ZFHX2]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[NSMCE3]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD31]] | -0.54 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[SYNPO]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity lowers TXNDC12's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.39× higher at baseline in the lines without TRIP6 | 0.005 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[SYCP2L]] | B | SYCP2L activity raises TXNDC12's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without SYCP2L | 0.074 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[PSMB5]] | B | PSMB5 activity raises TXNDC12's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IARS1]] | C | TXNDC12's natural level weakens IARS1's drug response | TXNDC12's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.05; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -24.8); signed map (-45.3, 8.5). **Vector** length 125, 36.2% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.2 | +7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.0 | +4.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.0 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.0 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.8 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.2 | -14.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -11.1 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.1 | -13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.4 | -17.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.8 | -8.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.2 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin domain containing 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,020,131-52,055,772 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TLP19, ERP18, ERP19, hAG-1, AGR1, PDIA16 |
| Gene groups (HGNC) | Protein disulfide isomerases; Thioredoxin domain containing ; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95881](https://www.uniprot.org/uniprotkb/O95881) (Thioredoxin domain-containing protein 12):

> Protein-disulfide reductase of the endoplasmic reticulum that promotes disulfide bond formation in client proteins through its thiol-disulfide oxidase activity.

**Summary**, from NCBI Gene [51060](https://www.ncbi.nlm.nih.gov/gene/51060):

> This gene encodes a member of the thioredoxin superfamily. Members of this family are characterized by a conserved active motif called the thioredoxin fold that catalyzes disulfide bond formation and isomerization. This protein localizes to the endoplasmic reticulum and has a single atypical active motif. The encoded protein is mainly involved in catalyzing native disulfide bond formation and displays activity similar to protein-disulfide isomerases. This protein may play a role in defense …

**Accessions** — [HGNC:24626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24626) · Entrez [51060](https://www.ncbi.nlm.nih.gov/gene/51060) · UniProt [O95881](https://www.uniprot.org/uniprotkb/O95881) · Ensembl [ENSG00000117862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117862)

## Data

Gene col 3952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3952); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3952]; `tensor/DDL_lfc|DDL_z.npy` [3952]; `embed/gene_vectors.npy` [3952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3952 or target_col == 3952). Every well: [[TXNDC12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNDC12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
