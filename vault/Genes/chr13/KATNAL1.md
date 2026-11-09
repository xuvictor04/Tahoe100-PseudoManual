---
symbol: "KATNAL1"
type: "gene"
col: 2271
ensembl_id: "ENSG00000102781"
name: "katanin catalytic subunit A1 like 1"
location: "13q12.3"
module: 175
arm: "+"
pooled_cpm: 44.19
n_lines_expressing: 43
n_dd_up: 14
n_dd_down: 40
n_dd_up_clean: 13
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 12
direction_downstream: 39
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# KATNAL1

*katanin catalytic subunit A1 like 1* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.43× (z +6.2, q 3e-07, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.182× (z -43.4, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD36B]] (+0.65, fdr 7e-06), [[HACE1]] (+0.61, fdr 7e-06), [[ANKRD36]] (+0.60, fdr 1e-05); moves opposite to [[SMIM31]] (-0.54, fdr 5e-05), [[POU5F1B]] (-0.52, fdr 3e-05), [[SRMS]] (-0.51, fdr 4e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SMIM31]] → it (grade B ⚠); 39 go from it, the strongest it → [[SMIM31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.43×** | +6.2 | 3e-07 | 24/40 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +5.7 | 3e-06 | 22/40 (SK-MEL-2, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.35×** | +5.3 | 2e-05 | 19/41 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +4.7 | 5e-04 | 20/41 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 0.001 | 17/41 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Neratinib (drug)]] 5 µM |  | **1.27×** | +4.4 | 0.001 | 21/41 (C32, C-33 A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.003 | 18/41 (C32, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.007 | 15/41 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.026 | 11/41 (PANC-1, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.028 | 10/41 (SW480, C-33 A, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.14× | +3.3 | 0.039 | 3/41 (A-427, SW 900, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.039 | 11/41 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 1.14× | +3.3 | 0.040 | 7/41 (J82, RPMI-7951, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.3 | 0.041 | 10/41 (HS-578T, RKO, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.049 | 8/41 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.049 | 9/41 (C32, SHP-77, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.060 | 7/40 (A549, HS-578T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2271.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.182×** | -43.4 | 0e+00 | 40/41 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.239×** | -25.8 | 0e+00 | 38/41 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.248×** | -24.1 | 0e+00 | 38/41 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.498×** | -17.8 | 0e+00 | 31/41 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.469×** | -13.6 | 4e-40 | 35/41 (Hs 766T, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.489×** | -12.9 | 6e-36 | 34/41 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.255×** | -12.7 | 9e-35 | 38/41 (HEC-1-A, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.530×** | -11.4 | 2e-28 | 31/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.532×** | -11.4 | 4e-28 | 33/41 (A-172, HOP62, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -10.8 | 3e-25 | 28/41 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.599×** | -9.2 | 2e-18 | 33/41 (A-172, SW 1088, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.623×** | -8.5 | 7e-16 | 31/41 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.627×** | -8.1 | 3e-14 | 27/41 (NCI-H460, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.647×** | -7.8 | 2e-13 | 30/41 (NCI-H460, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.649×** | -7.8 | 3e-13 | 30/41 (A-172, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.739×** | -7.7 | 6e-13 | 25/41 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -7.4 | 4e-12 | 28/41 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.721×** | -5.9 | 1e-07 | 25/41 (Panc 03.27, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.770×** | -4.7 | 7e-05 | 19/41 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.621×** | -4.4 | 2e-04 | 17/41 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.773×** | -4.4 | 3e-04 | 20/41 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.630×** | -4.3 | 4e-04 | 21/41 (LOX-IMVI, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.817×** | -3.6 | 0.005 | 15/41 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 72.7 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -30.4) |
| [[A-172 (line)]] | wt | 194 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -19.5) |
| [[NCI-H460 (line)]] | wt | 28.7 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0928× (z -32.4) |
| [[A549 (line)]] | wt | 47.6 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -30.3) |
| [[HOP62 (line)]] | alt | 73.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -34.4) |
| [[HS-578T (line)]] | alt | 63.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -26.0) |
| [[MIA PaCa-2 (line)]] | alt | 42.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -23.4) |
| [[Hs 766T (line)]] | wt | 40.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -18.6) |
| [[LOX-IMVI (line)]] | wt | 73.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0284× (z -31.7) |
| [[C32 (line)]] | wt | 51.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.8) |
| [[J82 (line)]] | alt | 87.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -25.8) |
| [[NCI-H23 (line)]] | alt | 42.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -23.3) |
| [[RPMI-7951 (line)]] | alt | 73.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -23.3) |
| [[SW480 (line)]] | alt | 37.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -21.7) |
| [[PANC-1 (line)]] | alt | 40.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -26.3) |
| [[A498 (line)]] | wt | 83.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -12.4) |
| [[HCT15 (line)]] | alt | 60.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -18.4) |
| [[NCI-H1792 (line)]] | alt | 35.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0823× (z -27.8) |
| [[Panc 03.27 (line)]] | alt | 42.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -18.6) |
| [[SW 1088 (line)]] | alt | 103 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0283× (z -12.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0405× (z -11.1) |
| [[SW48 (line)]] | wt | 22.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.7) |
| [[A-427 (line)]] | wt | 41.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.243× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -19.5) |
| [[H4 (line)]] | wt | 57.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -25.0) |
| [[NCI-H2030 (line)]] | alt | 36.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -21.2) |
| [[NCI-H2347 (line)]] | alt | 36.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -20.5) |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -14.0) |
| [[SNU-423 (line)]] | alt | 55.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -22.4) |
| [[SW 900 (line)]] | alt | 36.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -17.8) |
| [[AN3 CA (line)]] | alt | 62.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 44.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -14.5) |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1271 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0716× (z -16.7) |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.87 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD36B]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[HACE1]] | +0.61 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD36]] | +0.60 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[STX2]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TRAM2]] | +0.57 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[FAM161A]] | +0.57 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[NTAN1]] | +0.57 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[UBE2Q2P1]] | +0.56 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.56 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[STARD9]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SGCE]] | +0.54 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[TMEM14A]] | +0.54 | +0.48 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM31]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[POU5F1B]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SRMS]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TNFSF14]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NTMT1]] | -0.50 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TNFRSF14-AS1]] | -0.50 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[SLC20A2]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SLC30A7]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[COLEC10]] | -0.49 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[SEPTIN9-DT]] | -0.48 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[LINC01277]] | -0.48 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[STYXL1]] | -0.48 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 7, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM31]] | B | SMIM31 activity lowers KATNAL1's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 3.21× higher at baseline in the lines without SMIM31 | 0.001 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[CERCAM]] | B | CERCAM activity raises KATNAL1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 4.24× lower at baseline in the lines without CERCAM | 0.006 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[TNFSF15]] | B | TNFSF15 activity lowers KATNAL1's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 2.95× higher at baseline in the lines without TNFSF15 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[BVES]] | B | BVES activity raises KATNAL1's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.81× lower at baseline in the lines without BVES | 0.073 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[TOP2A]] | B | TOP2A activity raises KATNAL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GNB4]] | B | GNB4 activity raises KATNAL1's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 2.67× lower at baseline in the lines without GNB4 | 0.099 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1 |
| [[TCF7L1]] | B | TCF7L1 activity raises KATNAL1's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 3.07× lower at baseline in the lines without TCF7L1 | 0.0995 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[STARD9]] | C | STARD9 activity raises KATNAL1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 5.12× lower at baseline in the lines without STARD9 | 7e-04 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent; co-absent with the target |
| [[GGH]] | C | GGH activity raises KATNAL1's level | lines that do not express GGH (5) vs lines expressing it (45) | 4.13× lower at baseline in the lines without GGH | 0.002 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent; co-absent with the target |
| [[DZIP1L]] | C | DZIP1L activity raises KATNAL1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 4.75× lower at baseline in the lines without DZIP1L | 0.008 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent; co-absent with the target |
| [[FSD1L]] | C | FSD1L activity raises KATNAL1's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.67× lower at baseline in the lines without FSD1L | 0.040 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[KIF3C]] | C | KIF3C activity raises KATNAL1's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 4.61× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; co-absent with the target; its own permutation p |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 35, C 4. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM31]] | B | KATNAL1 activity lowers SMIM31's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 7.55× higher at baseline in the lines without KATNAL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[CBX1]] | B | KATNAL1 activity raises CBX1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without KATNAL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[SEC22C]] | B | KATNAL1 activity raises SEC22C's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without KATNAL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[RPA1]] | B | KATNAL1 activity raises RPA1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without KATNAL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[ALG9]] | B | KATNAL1 activity raises ALG9's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.52× lower at baseline in the lines without KATNAL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[HACE1]] | B | KATNAL1 activity raises HACE1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.64× lower at baseline in the lines without KATNAL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[ECI2]] | B | KATNAL1 activity raises ECI2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without KATNAL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[SKP2]] | B | KATNAL1 activity raises SKP2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without KATNAL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[POT1]] | B | KATNAL1 activity raises POT1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without KATNAL1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[ESD]] | B | KATNAL1 activity raises ESD's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without KATNAL1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[CDS2]] | B | KATNAL1 activity raises CDS2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without KATNAL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[SEMA4F]] | B | KATNAL1 activity raises SEMA4F's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without KATNAL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.7, -10.1); signed map (-36.8, -10.4). **Vector** length 96.7, 27.1% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | -2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -17.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -24.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.5 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -25.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -7.7 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | katanin catalytic subunit A1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:30,202,630-30,307,551 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2599 |
| Gene groups (HGNC) | AAA ATPases; Katanin catalytic subunit family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW62](https://www.uniprot.org/uniprotkb/Q9BW62) (Katanin p60 ATPase-containing subunit A-like 1):

> Regulates microtubule dynamics in Sertoli cells, a process that is essential for spermiogenesis and male fertility. Severs microtubules in an ATP-dependent manner, promoting rapid reorganization of cellular microtubule arrays (By similarity). Has microtubule-severing activity in vitro.

**Summary**, from NCBI Gene [84056](https://www.ncbi.nlm.nih.gov/gene/84056):

> Enables identical protein binding activity and microtubule severing ATPase activity. Involved in microtubule severing. Located in cytosol and microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28361) · Entrez [84056](https://www.ncbi.nlm.nih.gov/gene/84056) · UniProt [Q9BW62](https://www.uniprot.org/uniprotkb/Q9BW62) · Ensembl [ENSG00000102781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102781)

## Data

Gene col 2271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2271); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2271]; `tensor/DDL_lfc|DDL_z.npy` [2271]; `embed/gene_vectors.npy` [2271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2271 or target_col == 2271). Every well: [[KATNAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KATNAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
