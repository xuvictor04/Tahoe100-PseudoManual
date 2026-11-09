---
symbol: "ATAD2B"
type: "gene"
col: 4119
ensembl_id: "ENSG00000119778"
name: "ATPase family AAA domain containing 2B"
location: "2p24.1-p23.3"
module: 46
arm: "+"
pooled_cpm: 118.89
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ATAD2B

*ATPase family AAA domain containing 2B* — 2p24.1-p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +21.2, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.464× (z -16.5, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.494× (z -15.8, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF11]] (+0.70, fdr 7e-06), [[MACROH2A2]] (+0.68, fdr 1e-05), [[ACOT2]] (+0.67, fdr 2e-05); moves opposite to [[FCHO1]] (-0.64, fdr 6e-05), [[GNAI3]] (-0.63, fdr 4e-05), [[FCHSD1]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +21.2 | 0e+00 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.20×** | +17.7 | 0e+00 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +14.9 | 0e+00 | 45/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +13.7 | 9e-41 | 37/49 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +12.8 | 1e-35 | 44/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +12.0 | 3e-31 | 47/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +11.5 | 8e-29 | 43/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +11.0 | 5e-26 | 39/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +9.7 | 3e-20 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.6 | 3e-09 | 33/50 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.3 | 1e-08 | 29/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +5.1 | 2e-05 | 29/47 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +5.0 | 3e-05 | 28/49 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 1e-04 | 26/48 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.004 | 12/48 (A-427, Hs 766T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.039 | 17/47 (LoVo, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -16.5 | 0e+00 | 41/44 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.486×** | -16.1 | 0e+00 | 44/49 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.494×** | -15.8 | 0e+00 | 43/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.515×** | -13.7 | 1e-40 | 40/45 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.549×** | -13.4 | 7e-39 | 40/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.619×** | -10.7 | 8e-25 | 44/48 (C32, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.662×** | -9.2 | 3e-18 | 36/48 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.765×** | -8.5 | 2e-15 | 37/48 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.757×** | -6.2 | 3e-08 | 30/49 (C-33 A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.767×** | -5.9 | 2e-07 | 32/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.810×** | -4.7 | 1e-04 | 25/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.772×** | -4.1 | 0.002 | 22/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.797×** | -3.6 | 0.013 | 23/47 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.865× | -3.2 | 0.050 | 11/48 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.864× | -3.1 | 0.065 | 19/47 (SW1417, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 135 | 8 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +18.4) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 146 | 9 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -16.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 107 | 6 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.448× (z -10.2) |
| [[LoVo (line)]] | wt | 108 | 5 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 272 | 4 (1 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +20.7) | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -20.8) |
| [[NCI-H460 (line)]] | wt | 152 | 3 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.442× (z -13.6) |
| [[A549 (line)]] | wt | 168 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.7) | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -13.8) |
| [[BT-474 (line)]] | alt | 110 | 8 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 99.3 | 4 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.471× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 258 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.369× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 128 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -23.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 66.0 | 7 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 102 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.563× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 123 | 2 | 5 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.441× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 67.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.7) | — |
| [[HepG2_C3A (line)]] | wt | 159 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -12.2) |
| [[HT-29 (line)]] | alt | 101 | 3 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.3) | [[Auranofin (drug)]] 5 µM 0.414× (z -11.4) |
| [[RKO (line)]] | wt | 164 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -10.7) |
| [[SHP-77 (line)]] | alt | 130 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -12.4) |
| [[SW1417 (line)]] | alt | 173 | 1 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -15.1) |
| [[C-33 A (line)]] | alt | 148 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 83.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 141 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -11.5) |
| [[LS 180 (line)]] | wt | 129 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.466× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 89.2 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +14.6) | — |
| [[A-427 (line)]] | wt | 177 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -19.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 77.7 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.442× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 70.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 110 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 103 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -14.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 130 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 79.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 88.5 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.8) | — |
| [[A-172 (line)]] | wt | 103 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.97× (z +8.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.448× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 191 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.322× (z -9.5) |
| [[COLO 205 (line)]] | alt | 80.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 99.0 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.84× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 50.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.3) | — |
| [[C32 (line)]] | wt | 112 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.301× (z -13.3) |
| [[H4 (line)]] | wt | 59.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +9.0) | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 76.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 125 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.3) | — |
| [[SW 1088 (line)]] | alt | 73.1 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 5 µM 0.0669× (z -9.1) |
| [[CHP-212 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF11]] | +0.70 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MACROH2A2]] | +0.68 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ACOT2]] | +0.67 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[C2orf42]] | +0.67 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[MED13]] | +0.67 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[RNF146]] | +0.66 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[ARID1B]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[FBXW4]] | +0.65 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ARID2]] | +0.65 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[DECR1]] | +0.65 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TDRD3]] | +0.64 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[CREBBP]] | +0.64 | +0.37 / +0.55 | both halves | 9e-05 | same gene group |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | -0.64 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[GNAI3]] | -0.63 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[FCHSD1]] | -0.60 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[SH3PXD2B]] | -0.59 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ATP1A3]] | -0.59 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[SLC27A1]] | -0.58 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[AIF1L]] | -0.57 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[CDK18]] | -0.56 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[BAIAP3]] | -0.56 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[AMPD2]] | -0.55 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[EDA]] | -0.55 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[GIPR]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATAD2B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[STAC]] | B | STAC activity lowers ATAD2B's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.19× higher at baseline in the lines without STAC | 0.079 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[C2orf42]] | C | C2orf42's natural level strengthens ATAD2B's drug response | C2orf42's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.44; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.5, 14.2); signed map (25.9, -22.8). **Vector** length 127, 45.8% of its response variance represented; |z| ≥ 3 in 1,414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.2 | +13.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.7 | +11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +12.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.2 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.8 | -10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -9.4 | -13.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -9.4 | -15.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.1 | -9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.1 | -8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ATPase family AAA domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1-p23.3 — chr2:23,748,664-23,927,123 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1240 |
| Gene groups (HGNC) | AAA ATPases; Bromodomain containing |
| Matched by | ensembl_id |

UniProt [Q9ULI0](https://www.uniprot.org/uniprotkb/Q9ULI0) carries no function annotation.

**Summary**, from NCBI Gene [54454](https://www.ncbi.nlm.nih.gov/gene/54454):

> The protein encoded by this gene belongs to the AAA ATPase family. This family member includes an N-terminal bromodomain. It has been found to be localized to the nucleus, partly to replication sites, consistent with a chromatin-related function. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:29230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29230) · Entrez [54454](https://www.ncbi.nlm.nih.gov/gene/54454) · UniProt [Q9ULI0](https://www.uniprot.org/uniprotkb/Q9ULI0) · Ensembl [ENSG00000119778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119778)

## Data

Gene col 4119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4119); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4119]; `tensor/DDL_lfc|DDL_z.npy` [4119]; `embed/gene_vectors.npy` [4119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4119 or target_col == 4119). Every well: [[ATAD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATAD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
