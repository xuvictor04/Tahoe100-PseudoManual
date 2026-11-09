---
symbol: "APPL1"
type: "gene"
col: 8076
ensembl_id: "ENSG00000157500"
name: "adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 1"
location: "3p14.3"
module: 57
arm: "+"
pooled_cpm: 85.42
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# APPL1

*adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 1* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.47× (z +10.0, q 1e-20, up in 35 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 1.98×, LoVo 2.15×, PANC-1 1.88×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 3.23×, LOX-IMVI 2.21×, SK-MEL-2 1.97×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.492× (z -25.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS35]] (+0.67, fdr 7e-06), [[PPP2R5D]] (+0.62, fdr 1e-05), [[SETD3]] (+0.61, fdr 1e-05); moves opposite to [[SRRM2-AS1]] (-0.56, fdr 1e-04), [[NANOS3]] (-0.51, fdr 4e-05), [[ARMC5]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8076.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 1.98×, LoVo 2.15×, PANC-1 1.88×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 3.23×, LOX-IMVI 2.21×, SK-MEL-2 1.97×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +10.0 | 1e-20 | 35/49 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +9.1 | 2e-17 | 32/44 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.18× | +4.4 | 0.002 | 20/48 (KATO III, LoVo, …) | all doses, flat |  |
| [[Lapatinib ditosylate (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.064 | 16/48 (A498, SHP-77, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.14 | 8/48 (AsPC-1, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.492×** | -25.9 | 0e+00 | 44/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.581×** | -13.5 | 6e-39 | 39/48 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.390×** | -12.7 | 9e-35 | 46/49 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -10.8 | 8e-25 | 37/48 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.660×** | -10.7 | 9e-25 | 37/48 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.489×** | -9.6 | 5e-20 | 41/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -9.6 | 5e-20 | 40/48 (HCT15, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -8.1 | 4e-14 | 31/47 (A498, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -6.2 | 5e-08 | 33/48 (SNU-423, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.787×** | -5.6 | 1e-06 | 29/48 (SW48, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.806×** | -5.6 | 1e-06 | 26/48 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.810×** | -5.4 | 3e-06 | 25/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.713×** | -4.6 | 2e-04 | 25/45 (NCI-H1792, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.883× | -4.5 | 2e-04 | 13/48 (HOP62, SNU-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.834× | -4.5 | 3e-04 | 23/47 (J82, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.842× | -4.4 | 3e-04 | 20/48 (C32, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.864× | -3.4 | 0.019 | 15/47 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.875× | -3.3 | 0.025 | 13/48 (SNU-1, HepG2/C3A, …) | top dose only |  |
| [[Cilostazol (drug)]] 5 µM |  | 0.877× | -3.2 | 0.029 | 9/48 (SNU-1, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -19.3) |
| [[SNU-1 (line)]] | wt | 125 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -16.6) |
| [[HOP62 (line)]] | alt | 83.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -16.7) |
| [[SNU-423 (line)]] | alt | 117 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -22.5) |
| [[SW480 (line)]] | alt | 112 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +13.0) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 5 µM 0.275× (z -12.8) |
| [[A498 (line)]] | wt | 60.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -14.9) |
| [[C32 (line)]] | wt | 85.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 78.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 39.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -13.7) |
| [[RKO (line)]] | wt | 93.9 | 0 | 4 | — | [[TAK-901 (drug)]] 5 µM 0.151× (z -12.8) |
| [[SW 900 (line)]] | alt | 77.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -14.7) |
| [[A-172 (line)]] | wt | 80.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -23.1) |
| [[Hs 766T (line)]] | wt | 89.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -22.5) |
| [[HS-578T (line)]] | alt | 99.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -20.7) |
| [[Panc 03.27 (line)]] | alt | 100 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -18.2) |
| [[RPMI-7951 (line)]] | alt | 130 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -22.8) |
| [[SK-MEL-2 (line)]] | alt | 126 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -19.9) |
| [[A-427 (line)]] | wt | 130 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 50.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -16.7) |
| [[HCT15 (line)]] | alt | 136 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -13.6) |
| [[J82 (line)]] | alt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -22.5) |
| [[LoVo (line)]] | wt | 74.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -11.5) |
| [[LS 180 (line)]] | wt | 80.3 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.218× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 100 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.414× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 89.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -16.7) |
| [[PANC-1 (line)]] | alt | 74.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.614× (z -10.0) |
| [[SW48 (line)]] | wt | 147 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -12.8) |
| [[A549 (line)]] | wt | 65.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -10.1) |
| [[AN3 CA (line)]] | alt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -10.6) |
| [[COLO 205 (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 60.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.7) |
| [[KATO III (line)]] | alt | 91.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 90.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 70.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -13.6) |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.195× (z -8.7) |
| [[SW1417 (line)]] | alt | 61.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -10.3) |
| [[BT-474 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS35]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[PPP2R5D]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SETD3]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CPNE3]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SCAMP1]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD36]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[AKTIP]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[UBAC1]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[IARS2]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MYH10]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CBX1]] | +0.56 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[CCSAP]] | +0.56 | +0.63 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRM2-AS1]] | -0.56 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[NANOS3]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ARMC5]] | -0.51 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ZNF513]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[FIZ1]] | -0.50 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SALL1]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[AGER]] | -0.49 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[SP140]] | -0.48 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[MMRN2]] | -0.48 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[SLC13A3]] | -0.48 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[SLC9A8]] | -0.48 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[MMP25-AS1]] | -0.48 | -0.57 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises APPL1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without KATNAL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.1, -53.4); signed map (-49.0, -13.4). **Vector** length 100, 25.9% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -25.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,227,726-57,278,105 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APPL |
| Gene groups (HGNC) | BAR-PH domain containing |
| Reactome | 4 pathways, smallest: Caspase activation via Dependence Receptors in the absence of ligand; Caspase activation via extrinsic apoptotic signalling pathway; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKG1](https://www.uniprot.org/uniprotkb/Q9UKG1) (DCC-interacting protein 13-alpha):

> Multifunctional adapter protein that binds to various membrane receptors, nuclear factors and signaling proteins to regulate many processes, such as cell proliferation, immune response, endosomal trafficking and cell metabolism. Regulates signaling pathway leading to cell proliferation through interaction with RAB5A and subunits of the NuRD/MeCP1 complex. Functions as a positive regulator of innate immune response via activation of AKT1 signaling pathway by forming a complex with APPL1 and …

**Summary**, from NCBI Gene [26060](https://www.ncbi.nlm.nih.gov/gene/26060):

> The protein encoded by this gene has been shown to be involved in the regulation of cell proliferation, and in the crosstalk between the adiponectin signalling and insulin signalling pathways. The encoded protein binds many other proteins, including RAB5A, DCC, AKT2, PIK3CA, adiponectin receptors, and proteins of the NuRD/MeCP1 complex. This protein is found associated with endosomal membranes, but can be released by EGF and translocated to the nucleus. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24035) · Entrez [26060](https://www.ncbi.nlm.nih.gov/gene/26060) · UniProt [Q9UKG1](https://www.uniprot.org/uniprotkb/Q9UKG1) · Ensembl [ENSG00000157500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157500)

## Data

Gene col 8076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8076); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8076]; `tensor/DDL_lfc|DDL_z.npy` [8076]; `embed/gene_vectors.npy` [8076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8076 or target_col == 8076). Every well: [[APPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
