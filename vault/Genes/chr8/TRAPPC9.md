---
symbol: "TRAPPC9"
type: "gene"
col: 9504
ensembl_id: "ENSG00000167632"
name: "trafficking protein particle complex subunit 9"
location: "8q24.3"
module: 36
arm: "+"
pooled_cpm: 171.42
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TRAPPC9

*trafficking protein particle complex subunit 9* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.65× (z +11.9, q 1e-29, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.286× (z -15.2, q 0e+00, down in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.288× (z -15.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMDS]] (+0.60, fdr 3e-05), [[SPATA5]] (+0.58, fdr 2e-05), [[HDAC4]] (+0.58, fdr 8e-06); moves opposite to [[ZNF226]] (-0.59, fdr 2e-05), [[ZNF821]] (-0.58, fdr 1e-05), [[BTN2A3P]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.65×** | +11.9 | 1e-29 | 46/48 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +10.1 | 1e-21 | 47/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +8.5 | 4e-15 | 45/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +6.2 | 7e-08 | 42/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 0.001 | 36/48 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +3.8 | 0.012 | 36/49 (AsPC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +3.6 | 0.028 | 27/48 (A498, A549, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.32× | +3.0 | 0.18 | 29/48 (SW 900, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.286×** | -15.2 | 0e+00 | 47/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.288×** | -15.1 | 0e+00 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.305×** | -13.9 | 2e-41 | 46/48 (PANC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.490×** | -12.2 | 3e-32 | 43/48 (A549, Panc 03.27, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.431×** | -10.2 | 2e-22 | 45/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.473×** | -9.1 | 9e-18 | 42/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.483×** | -8.5 | 2e-15 | 46/47 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.552×** | -7.2 | 4e-11 | 39/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.331×** | -7.0 | 1e-10 | 45/49 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.572×** | -6.8 | 6e-10 | 34/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -6.0 | 1e-07 | 36/48 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.641×** | -5.2 | 1e-05 | 32/47 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.652×** | -4.8 | 7e-05 | 29/45 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.479×** | -4.7 | 1e-04 | 33/45 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **0.700×** | -4.3 | 6e-04 | 27/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.736×** | -3.7 | 0.005 | 27/48 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -3.0 | 0.057 | 24/48 (J82, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.769×** | -3.0 | 0.062 | 26/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.709×** | -3.0 | 0.062 | 24/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.707×** | -3.0 | 0.062 | 25/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 391 | 0 | 14 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 135 | 0 | 14 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 170 | 1 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.6) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 114 | 3 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.93× (z +12.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -14.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 228 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.248× (z -15.4) |
| [[PANC-1 (line)]] | alt | 138 | 1 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -20.8) |
| [[SW480 (line)]] | alt | 179 | 1 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.07× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.299× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -13.3) |
| [[HOP62 (line)]] | alt | 98.1 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.96× (z +14.9) | [[Digitoxin (drug)]] 5 µM 0.189× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -11.1) |
| [[HT-29 (line)]] | alt | 617 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -16.3) |
| [[J82 (line)]] | alt | 103 | 1 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.132× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 205 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -20.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.138× (z -9.8) |
| [[SW 900 (line)]] | alt | 104 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.34× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -16.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.274× (z -10.8) |
| [[SNU-1 (line)]] | wt | 101 | 1 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.99× (z +9.9) | [[Digitoxin (drug)]] 0.5 µM 0.233× (z -10.4) |
| [[SW1417 (line)]] | alt | 206 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -19.0) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -14.9) |
| [[A-427 (line)]] | wt | 234 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0478× (z -17.3) |
| [[A549 (line)]] | wt | 185 | 1 (1 ⚠) | 5 (5 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +8.8) ⚠ cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -24.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[BT-474 (line)]] | alt | 383 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -17.2) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -16.1) |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -13.6) |
| [[HS-578T (line)]] | alt | 127 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.58× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.133× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -11.7) |
| [[LoVo (line)]] | wt | 284 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.279× (z -14.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -14.4) |
| [[LS 180 (line)]] | wt | 250 | 3 (2 ⚠) | 3 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.28× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.165× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -18.8) |
| [[NCI-H2030 (line)]] | alt | 251 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -9.0) |
| [[A-172 (line)]] | wt | 82.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.9) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 112 | 2 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +10.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.03× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -18.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[CFPAC-1 (line)]] | alt | 71.2 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.73× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.8) ⚠ cell-cycle shift, explains ~63% of this change |
| [[COLO 205 (line)]] | alt | 185 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -9.2) |
| [[KATO III (line)]] | alt | 197 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 77.8 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.82× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.240× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -9.6) |
| [[SHP-77 (line)]] | alt | 274 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.230× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 73.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.62× (z +14.6) | — |
| [[C32 (line)]] | wt | 160 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 170 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -18.8) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SNU-423 (line)]] | alt | 58.6 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.38× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.9) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -10.4) |
| [[Hs 766T (line)]] | wt | 116 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.21× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.239× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 60.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.14× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 96.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.50× (z +10.7) | [[Harringtonine (drug)]] 5 µM 0.257× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 83.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.93× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.196× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 225 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0651× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -8.6) |
| [[SW48 (line)]] | wt | 158 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -11.0) |
| [[AN3 CA (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 230 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 78.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.217× (z -12.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMDS]] | +0.60 | +0.43 / +0.56 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[SPATA5]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[HDAC4]] | +0.58 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[IQCH]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[VPS13D]] | +0.57 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[RNGTT]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[IPO7]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[VTI1A]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[HERC2]] | +0.55 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[EIPR1]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RANBP17]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF226]] | -0.59 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ZNF821]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[BTN2A3P]] | -0.58 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[IFT46]] | -0.57 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.56 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[DNAJC27]] | -0.55 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CLK4]] | -0.54 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[BTN2A1]] | -0.53 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[BPNT1]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZNF675]] | -0.53 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[ZSCAN16-AS1]] | -0.53 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[ATP23]] | -0.53 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TRAPPC9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.441). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-2.7, -32.6); signed map (-17.0, -54.9). **Vector** length 100, 43.1% of its response variance represented; |z| ≥ 3 in 1,358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +11.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +8.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.9 | -8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -6.7 | -12.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.0 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:139,727,725-140,458,579 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IKBKBBP, NIBP, KIAA1882, T1, TRS120, MRT13 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 8 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q05](https://www.uniprot.org/uniprotkb/Q96Q05) (Trafficking protein particle complex subunit 9):

> Functions as an activator of NF-kappa-B through increased phosphorylation of the IKK complex. May function in neuronal cells differentiation. May play a role in vesicular transport from endoplasmic reticulum to Golgi.

**Summary**, from NCBI Gene [83696](https://www.ncbi.nlm.nih.gov/gene/83696):

> This gene encodes a protein that likely plays a role in NF-kappa-B signaling. Mutations in this gene have been associated with autosomal-recessive cognitive disability. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:30832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30832) · Entrez [83696](https://www.ncbi.nlm.nih.gov/gene/83696) · UniProt [Q96Q05](https://www.uniprot.org/uniprotkb/Q96Q05) · Ensembl [ENSG00000167632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167632)

## Data

Gene col 9504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9504); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9504]; `tensor/DDL_lfc|DDL_z.npy` [9504]; `embed/gene_vectors.npy` [9504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9504 or target_col == 9504). Every well: [[TRAPPC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
