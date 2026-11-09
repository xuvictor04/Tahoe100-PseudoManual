---
symbol: "TBC1D20"
type: "gene"
col: 4686
ensembl_id: "ENSG00000125875"
name: "TBC1 domain family member 20"
location: "20p13"
module: 40
arm: "+"
pooled_cpm: 75.86
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# TBC1D20

*TBC1 domain family member 20* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.53× (z +7.8, q 3e-12, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.417× (z -15.5, q 0e+00, down in 34 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.541× (z -10.9, q 2e-25, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35E1]] (+0.74, fdr 7e-06), [[MPG]] (+0.74, fdr 7e-06), [[QPCTL]] (+0.73, fdr 7e-06); moves opposite to [[EWSR1]] (-0.64, fdr 3e-05), [[PARVA]] (-0.64, fdr 3e-05), [[PIGO]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PARVA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +7.8 | 3e-12 | 35/48 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.20×** | +4.8 | 4e-04 | 21/48 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.011 | 26/48 (AsPC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.11 | 20/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.2 | 0.11 | 9/48 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.19× | +3.2 | 0.11 | 14/49 (SW 1088, J82, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.11 | 20/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.11 | 19/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.11 | 14/48 (NCI-H2347, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | 1.12× | +3.1 | 0.12 | 7/49 (RPMI-7951, LS 180, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.13 | 17/48 (SW480, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -15.5 | 0e+00 | 34/43 (hTERT-HPNE, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.469×** | -14.0 | 8e-42 | 41/49 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.541×** | -10.9 | 2e-25 | 42/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -10.2 | 2e-22 | 35/45 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.701×** | -9.3 | 2e-18 | 30/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.649×** | -8.0 | 2e-13 | 33/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.735×** | -5.7 | 1e-06 | 29/48 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.9 | 5e-05 | 22/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.796×** | -3.9 | 0.006 | 24/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.869× | -3.7 | 0.015 | 20/48 (HS-578T, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.828×** | -3.5 | 0.026 | 22/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.4 | 0.027 | 1/50 (CHP-212) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.830×** | -3.4 | 0.027 | 23/49 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.825×** | -3.4 | 0.027 | 23/48 (C32, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.837× | -3.1 | 0.073 | 17/47 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Elagolix sodium (drug)]] 0.5 µM |  | 0.849× | -3.0 | 0.089 | 16/48 (SW 1271, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 101 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.3) |
| [[A498 (line)]] | wt | 68.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -21.2) |
| [[NCI-H2347 (line)]] | alt | 84.7 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.289× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 92.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.417× (z -9.3) |
| [[HOP62 (line)]] | alt | 125 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.328× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 84.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0841× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.298× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 74.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.269× (z -12.4) |
| [[SNU-423 (line)]] | alt | 125 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -16.6) |
| [[HS-578T (line)]] | alt | 85.5 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0540× (z -17.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.315× (z -13.0) |
| [[SW 900 (line)]] | alt | 89.9 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.472× (z -10.8) |
| [[A-172 (line)]] | wt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -16.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 75.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.99× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.385× (z -12.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 83.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.400× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 79.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.431× (z -11.8) |
| [[LoVo (line)]] | wt | 87.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.32× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 69.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 96.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -12.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 139 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.65× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -17.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -12.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 70.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 81.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -15.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 97.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -15.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 78.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0831× (z -9.6) |
| [[SW1417 (line)]] | alt | 48.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.1) |
| [[SW48 (line)]] | wt | 77.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0982× (z -16.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35E1]] | +0.74 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[MPG]] | +0.74 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 | pathway: Rab regulation of trafficking; STRING 461 |
| [[SLC31A1]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.71 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TMED9]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[EEF1AKMT4]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[EIF4EBP1]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[GUK1]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[LIN7B]] | +0.69 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SLC17A5]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.64 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[PARVA]] | -0.64 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[PIGO]] | -0.64 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.63 | -0.38 / -0.74 | both halves | 7e-05 |  |
| [[CCDC50]] | -0.62 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[TRIP12]] | -0.62 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[HNRNPH3]] | -0.62 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[TRIM44]] | -0.62 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[CDK6]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[UTP20]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[MCCC2]] | -0.61 | -0.46 / -0.65 | both halves | 2e-05 |  |
| [[LPP]] | -0.60 | -0.40 / -0.61 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVA]] | B | PARVA activity raises TBC1D20's level | lines that do not express PARVA (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without PARVA | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |
| [[AP1S3]] | C | AP1S3 activity lowers TBC1D20's level | lines that do not express AP1S3 (4) vs lines expressing it (46) | 1.47× higher at baseline in the lines without AP1S3 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (6.1, -20.1); signed map (-43.7, 12.6). **Vector** length 139, 41.9% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +7.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.4 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.1 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.1 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.3 | -10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.5 | -14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.4 | -15.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -8.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.7 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:423,596-462,566 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ852M4.2; previously C20orf140 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 8 pathways, smallest: TBC/RABGAPs; COPII-mediated vesicle transport; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BZ9](https://www.uniprot.org/uniprotkb/Q96BZ9) (TBC1 domain family member 20):

> GTPase-activating protein (GAP) specific for Rab1 and Rab2 small GTPase families for which it can accelerate the intrinsic GTP hydrolysis rate by more than five orders of magnitude. Also shows GAP activity for RAB18 GTPase. Promotes RAB18 dissociation from the endoplasmic reticulum (ER) membrane into the cytosol, probably through stimulating RAB18 GTP-hydrolysis. Involved in maintaining endoplasmic reticulum structure.

**Summary**, from NCBI Gene [128637](https://www.ncbi.nlm.nih.gov/gene/128637):

> This gene encodes a protein that belongs to a family of GTPase activator proteins of Rab-like small GTPases. The encoded protein and its cognate GTPase, Rab1, bind the nonstructural protein 5A (NS5A) of the hepatitis C virus (HCV) to mediate viral replication. Depletion of this protein inhibits replication of the virus and HCV infection. Mutations in this gene are associated with Warburg micro syndrome 4. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar …

**Accessions** — [HGNC:16133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16133) · Entrez [128637](https://www.ncbi.nlm.nih.gov/gene/128637) · UniProt [Q96BZ9](https://www.uniprot.org/uniprotkb/Q96BZ9) · Ensembl [ENSG00000125875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125875)

## Data

Gene col 4686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4686); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4686]; `tensor/DDL_lfc|DDL_z.npy` [4686]; `embed/gene_vectors.npy` [4686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4686 or target_col == 4686). Every well: [[TBC1D20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
