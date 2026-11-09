---
symbol: "SCRN1"
type: "gene"
col: 5832
ensembl_id: "ENSG00000136193"
name: "secernin 1"
location: "7p14.3"
module: 54
arm: "-"
pooled_cpm: 80.92
n_lines_expressing: 42
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SCRN1

*secernin 1* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +12.4, q 2e-32, up in 36 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.37× (z +6.0, q 3e-07, up in 30 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.210× (z -29.5, q 0e+00, down in 40 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4G2]] (+0.73, fdr 1e-05), [[DDX6]] (+0.71, fdr 1e-05), [[ARMT1]] (+0.70, fdr 1e-05); moves opposite to [[TOMM5]] (-0.70, fdr 1e-05), [[RPS26]] (-0.68, fdr 5e-05), [[RPL22L1]] (-0.67, fdr 2e-05, ⚠ RPL22L1 in the vector space only through flagged drug-doses), [[SNU13]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[PTPA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +12.4 | 2e-32 | 36/41 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +12.3 | 2e-32 | 32/37 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +6.1 | 2e-07 | 24/38 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.0 | 3e-07 | 30/40 (SW480, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 1e-06 | 25/40 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.7 | 1e-06 | 25/40 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 6e-05 | 25/40 (A549, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +4.7 | 1e-04 | 22/40 (A549, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.1 | 0.003 | 15/40 (LS 180, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.067 | 12/40 (NCI-H2030, A-427, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.0 | 0.13 | 7/40 (AsPC-1, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.210×** | -29.5 | 0e+00 | 40/40 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.242×** | -26.8 | 0e+00 | 40/40 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.268×** | -24.9 | 0e+00 | 40/40 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.458×** | -14.8 | 0e+00 | 38/40 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.669×** | -10.7 | 1e-24 | 30/40 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.595×** | -9.8 | 1e-20 | 37/40 (HepG2/C3A, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.431×** | -8.3 | 8e-15 | 34/41 (A-172, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.687×** | -6.8 | 8e-10 | 29/39 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.578×** | -5.4 | 4e-06 | 26/41 (Panc 03.27, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -5.0 | 3e-05 | 23/40 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.621×** | -4.7 | 1e-04 | 25/40 (Panc 03.27, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.794×** | -4.3 | 7e-04 | 23/40 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.679×** | -3.8 | 0.006 | 18/40 (Panc 03.27, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.701×** | -3.5 | 0.018 | 18/37 (H4, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.830×** | -3.5 | 0.018 | 18/40 (HepG2/C3A, AsPC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.761×** | -3.5 | 0.020 | 20/40 (LOX-IMVI, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.836× | -3.3 | 0.024 | 15/40 (H4, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 5 µM |  | 0.882× | -3.3 | 0.026 | 3/41 (NCI-H2122, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 99.9 | 5 (3 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.132× (z -29.6) |
| [[A-172 (line)]] | wt | 181 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.134× (z -28.0) |
| [[J82 (line)]] | alt | 81.1 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +11.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 89.5 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -19.2) |
| [[NCI-H2347 (line)]] | alt | 90.9 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -18.8) |
| [[HepG2_C3A (line)]] | wt | 83.1 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 225 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -23.6) |
| [[A-427 (line)]] | wt | 93.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +11.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -18.4) |
| [[A549 (line)]] | wt | 72.4 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -19.4) |
| [[AN3 CA (line)]] | alt | 176 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.205× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 243 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -19.8) |
| [[HOP62 (line)]] | alt | 88.8 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -19.1) |
| [[Hs 766T (line)]] | wt | 97.7 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -20.5) |
| [[HT-29 (line)]] | alt | 49.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -24.3) |
| [[PANC-1 (line)]] | alt | 118 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -17.4) |
| [[RPMI-7951 (line)]] | alt | 146 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -16.3) |
| [[BT-474 (line)]] | alt | 126 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -20.3) |
| [[H4 (line)]] | wt | 194 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -18.1) |
| [[HS-578T (line)]] | alt | 93.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 70.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.283× (z -10.4) |
| [[LS 180 (line)]] | wt | 48.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.238× (z -13.8) |
| [[SNU-423 (line)]] | alt | 85.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -19.1) |
| [[SW 900 (line)]] | alt | 73.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -19.6) |
| [[SW1417 (line)]] | alt | 51.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 80.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -21.4) |
| [[CFPAC-1 (line)]] | alt | 77.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -18.9) |
| [[HCT15 (line)]] | alt | 91.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.253× (z -12.1) |
| [[LoVo (line)]] | wt | 30.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +11.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.362× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 57.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 62.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 73.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.360× (z -10.3) |
| [[SHP-77 (line)]] | alt | 127 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +8.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.271× (z -10.0) |
| [[C-33 A (line)]] | alt | 55.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -10.7) |
| [[CHP-212 (line)]] | wt | 128 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.173× (z -9.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.272× (z -8.8) |
| [[SW 1088 (line)]] | alt | 113 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0581× (z -10.0) |
| [[SW 1271 (line)]] | alt | 128 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.163× (z -9.4) |
| [[A498 (line)]] | wt | 9.15 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 44.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | +0.73 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[DDX6]] | +0.71 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ARMT1]] | +0.70 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ZNF532]] | +0.70 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZNF564]] | +0.68 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[FLII]] | +0.67 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[HNRNPK]] | +0.67 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.66 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[NCOA4]] | +0.66 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.66 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PRKAR1A]] | +0.65 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[BMI1]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM5]] | -0.70 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[RPS26]] | -0.68 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[RPL22L1]] ⚠ | -0.67 | -0.48 / -0.68 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNU13]] | -0.67 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.65 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ETHE1]] | -0.65 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.65 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SNRPD2]] | -0.65 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[RPL17]] | -0.64 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.63 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RPS14]] | -0.62 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[RPL35]] ⚠ | -0.62 | -0.43 / -0.59 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.62 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[RABGEF1P1]] | -0.62 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPA]] | B | SCRN1 activity lowers PTPA's level | lines that do not express SCRN1 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without SCRN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PPFIA4 |
| [[BMI1]] | B | SCRN1 activity raises BMI1's level | lines that do not express SCRN1 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without SCRN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PPFIA4 |
| [[ELK4]] | B | SCRN1 activity lowers ELK4's level | lines that do not express SCRN1 (8) vs lines expressing it (42) | 1.29× higher at baseline in the lines without SCRN1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PPFIA4 |
| [[HEXB]] | B | SCRN1 activity lowers HEXB's level | lines that do not express SCRN1 (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without SCRN1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PPFIA4 |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.1, 2.5); signed map (17.3, -31.3). **Vector** length 123, 35.6% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +12.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.4 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -10.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -24.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.0 | -14.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -9.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -2.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | secernin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:29,920,104-29,990,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0193 |
| Gene groups (HGNC) | Secernin family |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12765](https://www.uniprot.org/uniprotkb/Q12765) (Secernin-1):

> Regulates exocytosis in mast cells. Increases both the extent of secretion and the sensitivity of mast cells to stimulation with calcium (By similarity).

**Summary**, from NCBI Gene [9805](https://www.ncbi.nlm.nih.gov/gene/9805):

> This gene likely encodes a member of the secernin family of proteins. A similar protein in rat functions in regulation of exocytosis in mast cells. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:22192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22192) · Entrez [9805](https://www.ncbi.nlm.nih.gov/gene/9805) · UniProt [Q12765](https://www.uniprot.org/uniprotkb/Q12765) · Ensembl [ENSG00000136193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136193)

## Data

Gene col 5832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5832); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5832]; `tensor/DDL_lfc|DDL_z.npy` [5832]; `embed/gene_vectors.npy` [5832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5832 or target_col == 5832). Every well: [[SCRN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCRN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
