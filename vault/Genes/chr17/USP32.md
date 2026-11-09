---
symbol: "USP32"
type: "gene"
col: 10008
ensembl_id: "ENSG00000170832"
name: "ubiquitin specific peptidase 32"
location: "17q23.3"
module: 120
arm: "+"
pooled_cpm: 211.59
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# USP32

*ubiquitin specific peptidase 32* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.38× (z +9.5, q 2e-18, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.499× (z -15.8, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.763× (z -6.1, q 9e-08, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAPGEF6]] (+0.51, fdr 4e-05), [[USP28]] (+0.48, fdr 3e-05), [[SCAPER]] (+0.47, fdr 1e-04); moves opposite to [[TXNDC15]] (-0.51, fdr 7e-05), [[SUGT1P3]] (-0.46, fdr 1e-04), [[PIGC]] (-0.45, fdr 1e-04).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.38×** | +9.5 | 2e-18 | 39/49 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +6.0 | 7e-07 | 29/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.6 | 5e-06 | 28/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +5.3 | 1e-05 | 17/48 (HT-29, A549, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.2 | 3e-05 | 27/48 (A-172, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.7 | 0.020 | 16/48 (NCI-H460, SK-MEL-2, …) | top dose only | composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.031 | 25/49 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.031 | 17/48 (BT-474, A498, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.036 | 16/48 (BT-474, H4, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.33× | +3.1 | 0.12 | 19/48 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.32× | +3.0 | 0.12 | 13/48 (AsPC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.10× | +3.0 | 0.12 | 7/49 (AsPC-1, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.499×** | -15.8 | 0e+00 | 45/49 (SNU-423, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -13.5 | 4e-39 | 39/44 (SK-MEL-2, HCT15, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.510×** | -13.4 | 7e-39 | 45/45 (A549, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.592×** | -11.4 | 3e-28 | 42/47 (HepG2/C3A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.819×** | -6.4 | 2e-08 | 25/49 (BT-474, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -6.1 | 9e-08 | 34/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.777×** | -5.7 | 8e-07 | 32/48 (Panc 03.27, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.698×** | -3.9 | 0.006 | 25/38 (A549, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.770×** | -3.9 | 0.007 | 30/48 (RKO, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.786×** | -3.6 | 0.020 | 25/47 (RKO, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.020 | 25/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.896× | -3.5 | 0.021 | 6/48 (RKO, A-427, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.726×** | -3.5 | 0.021 | 25/47 (C32, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.897× | -3.5 | 0.021 | 14/49 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.901× | -3.3 | 0.031 | 11/48 (RKO, C32, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.868× | -3.2 | 0.046 | 19/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.905× | -3.2 | 0.046 | 8/49 (C32, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.872× | -3.1 | 0.059 | 13/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.061 | 14/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.872× | -3.0 | 0.082 | 16/48 (NCI-H1573, RKO, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.878× | -2.9 | 0.086 | 13/48 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.820×** | -2.9 | 0.086 | 21/48 (RKO, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.879× | -2.9 | 0.086 | 8/49 (COLO 205, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.879× | -2.9 | 0.086 | 17/48 (CFPAC-1, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 354 | 1 | 9 (9 ⚠) | [[TAK-901 (drug)]] 5 µM 5.22× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -19.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 324 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.474× (z -9.8) |
| [[SNU-423 (line)]] | alt | 320 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.472× (z -10.1) |
| [[HOP62 (line)]] | alt | 220 | 2 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.515× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 202 | 3 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +21.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.84× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -14.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 480 | 3 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.62× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -30.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 194 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.11× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.520× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 201 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.48× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 209 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -16.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 148 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.23× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.495× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 216 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -16.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 329 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 206 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.459× (z -9.4) ⚠ toxic |
| [[J82 (line)]] | alt | 221 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 129 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.466× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 333 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.444× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 212 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 244 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.73× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -17.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 330 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -15.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 287 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -13.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 547 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -17.9) ⚠ cell-cycle shift, explains ~6% of this change |
| [[H4 (line)]] | wt | 231 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -13.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 97.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 320 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 198 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.441× (z -11.0) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 343 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 199 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -23.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 190 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -25.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.417× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 200 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.400× (z -12.0) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 185 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -13.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 126 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.563× (z -8.5) ⚠ toxic |
| [[A498 (line)]] | wt | 177 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.37× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 217 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -13.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 205 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.659× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.371× (z -11.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.570× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 1088 (line)]] | alt | 139 | 0 | 1 | — | [[Proglumide (drug)]] 0.5 µM 0.130× (z -9.2) |
| [[SW 900 (line)]] | alt | 214 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.461× (z -9.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -11.6) ⚠ toxic |
| [[SW48 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 278 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF6]] | +0.51 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[USP28]] | +0.48 | +0.43 / +0.46 | both halves | 3e-05 | same gene group; STRING 550 |
| [[SCAPER]] | +0.47 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[RALGAPA2]] | +0.46 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[NEDD4L]] | +0.45 | +0.36 / +0.39 | both halves | 9e-05 |  |
| [[GSK3B]] | +0.45 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[TMEM251]] | +0.44 | +0.34 / +0.37 | both halves | 1e-04 |  |
| [[KDM4C]] | +0.44 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[HS2ST1]] | +0.44 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[ZFYVE28]] | +0.44 | +0.40 / +0.43 | both halves | 4e-05 |  |
| [[DENND1A]] | +0.43 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[HK1]] | +0.42 | +0.40 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC15]] | -0.51 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[SUGT1P3]] | -0.46 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[PIGC]] | -0.45 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[CDC23]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[PGAP3]] | -0.44 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[RNF139-DT]] | -0.43 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[CLCC1]] | -0.42 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[FHIP2A]] | -0.42 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[RAE1]] | -0.42 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SETMAR]] | -0.41 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[SMPDL3A]] | -0.41 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[NIPSNAP3A]] | -0.40 | -0.31 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.164). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.1, 18.2); signed map (-35.8, 33.4). **Vector** length 111, 37.2% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +9.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.9 | +5.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.6 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | +0.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.3 | -11.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.3 | -6.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:60,177,327-60,422,470 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-60, USP10 |
| Gene groups (HGNC) | Ubiquitin specific peptidases; EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFA0](https://www.uniprot.org/uniprotkb/Q8NFA0) (Ubiquitin carboxyl-terminal hydrolase 32):

> Deubiquitinase that can remove conjugated ubiquitin from target proteins, such as RAB7A and LAMTOR1. Acts as a positive regulator of the mTORC1 signaling by mediating deubiquitination of LAMTOR1, thereby promoting the association between LAMTOR1 and the lysosomal V-ATPase complex and subsequent activation of the mTORC1 complex.

**Summary**, from NCBI Gene [84669](https://www.ncbi.nlm.nih.gov/gene/84669):

> Enables cysteine-type deubiquitinase activity. Involved in positive regulation of TORC1 signaling. Is active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19143) · Entrez [84669](https://www.ncbi.nlm.nih.gov/gene/84669) · UniProt [Q8NFA0](https://www.uniprot.org/uniprotkb/Q8NFA0) · Ensembl [ENSG00000170832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170832)

## Data

Gene col 10008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10008); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10008]; `tensor/DDL_lfc|DDL_z.npy` [10008]; `embed/gene_vectors.npy` [10008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10008 or target_col == 10008). Every well: [[USP32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
