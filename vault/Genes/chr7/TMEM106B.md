---
symbol: "TMEM106B"
type: "gene"
col: 2762
ensembl_id: "ENSG00000106460"
name: "transmembrane protein 106B"
location: "7p21.3"
module: 25
arm: "+"
pooled_cpm: 76.12
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TMEM106B

*transmembrane protein 106B* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.34× (z +17.6, q 0e+00, up in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 1.32× (z +5.4, q 8e-06, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.751× (z -6.0, q 1e-06, down in 26 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.643× (z -5.8, q 2e-06, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBTPS2]] (+0.72, fdr 7e-06), [[TWF1]] (+0.65, fdr 1e-05), [[LIN7C]] (+0.65, fdr 2e-05); moves opposite to [[ZBTB7A]] (-0.62, fdr 3e-05), [[DMPK]] (-0.58, fdr 1e-05), [[IL9RP3]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +17.6 | 0e+00 | 43/49 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +15.2 | 0e+00 | 38/42 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +14.8 | 0e+00 | 43/44 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +6.7 | 2e-09 | 27/47 (NCI-H2030, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.32×** | +5.4 | 8e-06 | 31/48 (SW480, A-427, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.3 | 1e-05 | 27/48 (HEC-1-A, J82, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +5.0 | 5e-05 | 24/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.20× | +4.7 | 2e-04 | 26/48 (NCI-H2347, RKO, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.7 | 2e-04 | 23/47 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 4e-04 | 22/48 (SW480, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.002 | 19/48 (A498, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +4.0 | 0.003 | 12/48 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.006 | 23/48 (LoVo, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 1.20× | +3.6 | 0.011 | 16/48 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.021 | 19/47 (SW480, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.025 | 14/49 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.029 | 7/48 (SW1417, NCI-H23, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.055 | 10/48 (NCI-H23, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.071 | 11/48 (AsPC-1, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.085 | 12/49 (LoVo, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.751×** | -6.0 | 1e-06 | 26/48 (RKO, C-33 A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.643×** | -5.8 | 2e-06 | 35/48 (SW 1271, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.770×** | -5.4 | 1e-05 | 26/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.698×** | -4.7 | 3e-04 | 27/49 (HCT15, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.793×** | -4.6 | 6e-04 | 23/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.743×** | -3.9 | 0.008 | 20/49 (NCI-H661, HS-578T, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.833×** | -3.8 | 0.011 | 17/48 (SW480, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.826×** | -3.8 | 0.011 | 19/47 (LOX-IMVI, SW480, …) | all doses, flat |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.752×** | -3.7 | 0.011 | 19/48 (MIA PaCa-2, A498, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.837× | -3.6 | 0.021 | 20/48 (NCI-H460, RPMI-7951, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.770×** | -3.4 | 0.030 | 15/49 (PANC-1, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.590×** | -3.4 | 0.031 | 15/48 (SW480, LS 180, …) | two highest doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bergenin (drug)]] 0.5 µM |  | 0.852× | -3.3 | 0.040 | 12/48 (MIA PaCa-2, SW 1271, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.863× | -3.1 | 0.092 | 18/48 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 62.3 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +12.9) | — |
| [[SW480 (line)]] | alt | 69.2 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 111 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +17.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 51.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +21.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +9.0) | — |
| [[A498 (line)]] | wt | 116 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +17.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 49.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.63× (z +13.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 46.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.14× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 67.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +15.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 37.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 56.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 84.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.69× (z +17.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.76× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 83.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 117 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 81.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -11.4) |
| [[PANC-1 (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +15.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 69.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.02× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 73.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +12.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +11.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 49.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.366× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 63.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.12× (z +14.5) | — |
| [[C-33 A (line)]] | alt | 97.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 57.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +9.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 46.5 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.366× (z -9.3) |
| [[LS 180 (line)]] | wt | 65.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +10.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 55.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.54× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.62× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 90.2 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0565× (z -10.2) |
| [[SW48 (line)]] | wt | 77.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +9.6) | — |
| [[A-427 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBTPS2]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TWF1]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.65 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[ALG10B]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[HINT3]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[STRADB]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ERLIN2]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CFL2]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.60 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[EEF1A1]] | +0.59 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[ERAP1]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.59 | +0.47 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB7A]] | -0.62 | -0.43 / -0.72 | both halves | 3e-05 |  |
| [[DMPK]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[IL9RP3]] | -0.58 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SLC66A2]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NUDT22]] | -0.56 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[RABGEF1P1]] | -0.55 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[CSNK1G2]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[EXOSC4]] | -0.54 | -0.16 / -0.63 | ⚠ one half (not replicated) | 0.001 |  |
| [[RBM38]] | -0.54 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[TRIM11]] | -0.54 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[IL17RA]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[MILIP]] | -0.53 | -0.21 / -0.62 | both halves | 7e-04 |  |
| [[ZNF324]] | -0.53 | -0.24 / -0.59 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TMEM106B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.8, -18.3); signed map (-16.7, -38.6). **Vector** length 132, 38.3% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +14.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +5.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +17.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +15.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +5.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +3.7 | +3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.3 | +4.0 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -6.5 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.6 | -5.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -4.3 | -4.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.2 | -3.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -3.9 | -3.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 106B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:12,211,270-12,243,367 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33727, FLJ11273 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUM4](https://www.uniprot.org/uniprotkb/Q9NUM4) (Transmembrane protein 106B):

> In neurons, involved in the transport of late endosomes/lysosomes. May be involved in dendrite morphogenesis and maintenance by regulating lysosomal trafficking. May act as a molecular brake for retrograde transport of late endosomes/lysosomes, possibly via its interaction with MAP6 (By similarity). In motoneurons, may mediate the axonal transport of lysosomes and axonal sorting at the initial segment (By similarity). It remains unclear whether TMEM106B affects the transport of moving lysosomes …

**Summary**, from NCBI Gene [54664](https://www.ncbi.nlm.nih.gov/gene/54664):

> Enables ATPase binding activity. Involved in dendrite morphogenesis and lysosome localization. Located in endosome and lysosomal membrane. Implicated in hypomyelinating leukodystrophy 16. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22407) · Entrez [54664](https://www.ncbi.nlm.nih.gov/gene/54664) · UniProt [Q9NUM4](https://www.uniprot.org/uniprotkb/Q9NUM4) · Ensembl [ENSG00000106460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106460)

## Data

Gene col 2762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2762); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2762]; `tensor/DDL_lfc|DDL_z.npy` [2762]; `embed/gene_vectors.npy` [2762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2762 or target_col == 2762). Every well: [[TMEM106B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM106B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
