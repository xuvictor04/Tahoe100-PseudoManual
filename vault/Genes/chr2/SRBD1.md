---
symbol: "SRBD1"
type: "gene"
col: 900
ensembl_id: "ENSG00000068784"
name: "S1 RNA binding domain 1"
location: "2p21"
module: 5
arm: "+"
pooled_cpm: 103.77
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SRBD1

*S1 RNA binding domain 1* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 1.26× (z +4.5, q 0.003, up in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM: 1.22× (z +3.9, q 0.010, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 1.64×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.11×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.463× (z -14.6, q 3e-45, down in 39 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.547× (z -11.9, q 2e-30, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNOT10]] (+0.61, fdr 7e-06), [[SMARCAD1]] (+0.60, fdr 1e-05), [[DDX18]] (+0.59, fdr 1e-05); moves opposite to [[SHC2]] (-0.54, fdr 2e-05), [[KIAA1522]] (-0.52, fdr 4e-05), [[PRKCI]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 900.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 1.64×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.11×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.26×** | +4.5 | 0.003 | 31/48 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.25×** | +4.2 | 0.005 | 24/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.23×** | +4.2 | 0.005 | 23/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.23×** | +4.2 | 0.005 | 21/48 (A549, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.010 | 19/48 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.093 | 17/48 (HOP62, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 1.37× | +3.2 | 0.10 | 21/49 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.2 | 0.11 | 19/48 (NCI-H2347, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.15 | 18/48 (SK-MEL-2, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.463×** | -14.6 | 3e-45 | 39/47 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -13.7 | 2e-40 | 42/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.529×** | -12.5 | 1e-33 | 43/49 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -12.1 | 1e-31 | 36/44 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.547×** | -11.9 | 2e-30 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.576×** | -10.0 | 1e-21 | 38/45 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -8.7 | 4e-16 | 38/48 (NCI-H2030, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -8.6 | 4e-16 | 38/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -7.9 | 2e-13 | 34/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -6.9 | 3e-10 | 34/48 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.800×** | -6.2 | 3e-08 | 27/48 (NCI-H1792, A498, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.731×** | -6.2 | 4e-08 | 32/48 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.738×** | -6.0 | 9e-08 | 32/48 (SW480, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.765×** | -5.1 | 2e-05 | 26/48 (PANC-1, A498, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.787×** | -4.4 | 3e-04 | 29/48 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.032 | 20/48 (NCI-H23, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.851× | -3.2 | 0.046 | 15/48 (AsPC-1, SNU-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.852× | -3.0 | 0.069 | 14/47 (RPMI-7951, A-172, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.897× | -3.0 | 0.069 | 8/49 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.808×** | -3.0 | 0.071 | 20/48 (NCI-H23, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.814×** | -2.9 | 0.089 | 8/49 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.858× | -2.8 | 0.098 | 15/48 (NCI-H1573, NCI-H661, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.866× | -2.8 | 0.099 | 16/48 (SHP-77, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 103 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -17.4) |
| [[PANC-1 (line)]] | alt | 135 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.494× (z -10.0) |
| [[HOP62 (line)]] | alt | 99.1 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -15.1) |
| [[KATO III (line)]] | alt | 148 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -11.2) |
| [[A498 (line)]] | wt | 128 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 108 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.393× (z -11.6) |
| [[SW480 (line)]] | alt | 123 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -18.6) |
| [[LS 180 (line)]] | wt | 90.6 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 138 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -15.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 183 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.504× (z -8.5) |
| [[C32 (line)]] | wt | 92.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.391× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 94.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -19.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 176 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.332× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.448× (z -9.4) |
| [[SHP-77 (line)]] | alt | 119 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -13.8) |
| [[SW1417 (line)]] | alt | 121 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -13.2) |
| [[H4 (line)]] | wt | 105 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -11.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 58.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.324× (z -9.5) |
| [[HCT15 (line)]] | alt | 136 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.227× (z -13.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 95.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.463× (z -9.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 89.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -11.0) |
| [[J82 (line)]] | alt | 65.0 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.389× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H23 (line)]] | alt | 266 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -28.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 72.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -14.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 81.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.408× (z -9.1) |
| [[SW 1088 (line)]] | alt | 113 | 0 | 3 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.101× (z -10.0) |
| [[SW 900 (line)]] | alt | 70.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.374× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 88.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -13.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 99.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -18.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 94.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.448× (z -8.8) |
| [[SNU-1 (line)]] | wt | 91.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -15.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 50.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -8.8) |
| [[COLO 205 (line)]] | alt | 97.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.303× (z -9.0) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.300× (z -10.1) ⚠ toxic |
| [[HT-29 (line)]] | alt | 94.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -12.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 70.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0874× (z -11.0) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0831× (z -13.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 67.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -9.3) |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT10]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SMARCAD1]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[DDX18]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[TTI1]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ELP3]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ORC5]] | +0.57 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CPSF3]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[RPA2]] | +0.54 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[DHRS7B]] | +0.54 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PARG]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[POLE3]] | +0.53 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[NUP35]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHC2]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[KIAA1522]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[PRKCI]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LZTS3]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[KRAS]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[PGM2L1]] | -0.49 | -0.53 / -0.37 | both halves | 9e-05 |  |
| [[CACFD1]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[DDAH2]] | -0.48 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[LLGL2]] | -0.48 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[FBXO2]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TP53INP2]] | -0.47 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[UBE2H]] | -0.47 | -0.36 / -0.54 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity lowers SRBD1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 1.4% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.354). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-21.6, -41.2); signed map (-29.7, -51.1). **Vector** length 102, 31.0% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.0 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +3.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -14.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | S1 RNA binding domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:45,388,680-45,612,165 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10379 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5C6](https://www.uniprot.org/uniprotkb/Q8N5C6) (S1 RNA-binding domain-containing protein 1):

> DNA- and histone-binding protein that localizes to the central axes of mitotic chromosomes. Promotes chromosome segregation by facilitating TOP2A recruitment to mitotic chromosomes, thereby preventing anaphase failure. During prophase, safeguards the decatenation process to avoid the formation of difficult-to-resolve DNA structures, preventing chromosome missegregation. Also contributes to the regulation of nucleus pulposus cell senescence.

**Summary**, from NCBI Gene [55133](https://www.ncbi.nlm.nih.gov/gene/55133):

> Predicted to enable mRNA binding activity. Predicted to be a structural constituent of ribosome. Predicted to be involved in translation. Predicted to be located in chromosome; cytoplasm; and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25521) · Entrez [55133](https://www.ncbi.nlm.nih.gov/gene/55133) · UniProt [Q8N5C6](https://www.uniprot.org/uniprotkb/Q8N5C6) · Ensembl [ENSG00000068784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068784)

## Data

Gene col 900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 900); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 900]; `tensor/DDL_lfc|DDL_z.npy` [900]; `embed/gene_vectors.npy` [900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 900 or target_col == 900). Every well: [[SRBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
