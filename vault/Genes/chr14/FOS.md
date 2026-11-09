---
symbol: "FOS"
type: "gene"
col: 9938
ensembl_id: "ENSG00000170345"
name: "Fos proto-oncogene, AP-1 transcription factor subunit"
location: "14q24.3"
module: 109
arm: "+"
pooled_cpm: 91.97
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# FOS

*Fos proto-oncogene, AP-1 transcription factor subunit* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.05× (z +15.5, q 0e+00, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.88× (z +5.3, q 2e-05, up in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (C32 30.8×, SK-MEL-2 25.8×, NCI-H2347 21.8×, AsPC-1 15.8×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Auranofin (drug)]] 5 µM in 4 lines (SK-MEL-2 14.1×, HEC-1-A 13.0×, HCT15 5.91×, A-427 7.70×); [[Harringtonine (drug)]] 5 µM in 2 lines (C32 23.3×, SK-MEL-2 33.4×; ⚠ cell-cycle shift, explains ~43% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.233× (z -7.0, q 2e-09, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOSB]] (+0.89, fdr 7e-06), [[EGR1]] (+0.79, fdr 7e-06), [[EGR2]] (+0.72, fdr 7e-06); moves opposite to [[C8orf76]] (-0.62, fdr 1e-05), [[CCNY-AS1]] (-0.60, fdr 1e-05), [[RWDD3]] (-0.58, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR4A2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (C32 30.8×, SK-MEL-2 25.8×, NCI-H2347 21.8×, AsPC-1 15.8×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Auranofin (drug)]] 5 µM in 4 lines (SK-MEL-2 14.1×, HEC-1-A 13.0×, HCT15 5.91×, A-427 7.70×); [[Harringtonine (drug)]] 5 µM in 2 lines (C32 23.3×, SK-MEL-2 33.4×; ⚠ cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **9.05×** | +15.5 | 0e+00 | 45/47 (C32, SK-MEL-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **4.19×** | +6.8 | 2e-09 | 37/47 (C32, SK-MEL-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **3.77×** | +6.6 | 8e-09 | 38/48 (SK-MEL-2, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.97×** | +5.4 | 9e-06 | 43/47 (SK-MEL-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.88×** | +5.3 | 2e-05 | 31/47 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.63×** | +4.8 | 1e-04 | 33/47 (C32, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.44×** | +4.1 | 0.004 | 29/42 (HEC-1-A, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **2.33×** | +4.0 | 0.004 | 26/41 (NCI-H460, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.22×** | +4.0 | 0.005 | 39/47 (H4, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.042 | 35/47 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.63×** | +3.3 | 0.042 | 34/48 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.93×** | +3.3 | 0.053 | 25/47 (NCI-H460, AsPC-1, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9938.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.233×** | -7.0 | 2e-09 | 44/46 (SW48, SHP-77, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.269×** | -6.3 | 6e-08 | 45/49 (SW48, HCT15, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.269×** | -6.3 | 6e-08 | 41/46 (A-427, HCT15, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.424×** | -6.0 | 3e-07 | 46/47 (SHP-77, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.300×** | -5.5 | 4e-06 | 46/47 (NCI-H23, SW48, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.490×** | -5.0 | 5e-05 | 42/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.383×** | -4.8 | 1e-04 | 45/48 (SW48, SHP-77, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.497×** | -4.3 | 0.001 | 38/47 (SHP-77, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.432×** | -4.2 | 0.002 | 36/46 (NCI-H2347, CHP-212, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.457×** | -3.9 | 0.006 | 33/47 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.236×** | -3.8 | 0.009 | 35/45 (SW48, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.479×** | -3.7 | 0.012 | 32/47 (HT-29, KATO III, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.484×** | -3.6 | 0.013 | 32/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.493×** | -3.5 | 0.017 | 31/46 (LS 180, Hs 766T, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.506×** | -3.4 | 0.025 | 36/48 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.272×** | -3.4 | 0.025 | 34/47 (HCT15, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.516×** | -3.2 | 0.045 | 31/47 (HT-29, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.90 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.0 | 10 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 40.2× (z +18.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 212 | 4 (4 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +14.0) ⚠ cell-cycle shift, explains ~32% of this change | [[Trametinib (drug)]] 5 µM 0.0608× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 32.0 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +20.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 14.1× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 34.5 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.2× (z +16.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 94.2 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +20.2) ⚠ cell-cycle shift, explains ~32% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.137× (z -8.9) |
| [[A-427 (line)]] | wt | 52.6 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +10.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.70× (z +9.9) | [[Cobimetinib (drug)]] 5 µM 0.128× (z -9.6) |
| [[C32 (line)]] | wt | 204 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.8× (z +24.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +17.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 13.0× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 138 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +19.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 234 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -9.8) |
| [[KATO III (line)]] | alt | 174 | 0 | 3 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.299× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 58.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +15.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 103 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +14.6) ⚠ cell-cycle shift, explains ~32% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0982× (z -9.0) |
| [[HS-578T (line)]] | alt | 41.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +14.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 132 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +13.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 48.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 72.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +12.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[BT-474 (line)]] | alt | 82.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 144 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +17.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 245 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +10.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 162 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.91× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 72.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +14.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 90.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +9.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +16.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +10.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +11.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 43.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +13.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 75.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +9.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +14.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +13.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +11.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +12.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 40.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +10.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 80.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +12.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 160 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.184× (z -9.0) |
| [[SNU-423 (line)]] | alt | 57.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +14.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW 1271 (line)]] | alt | 73.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +8.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 162 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +12.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +11.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 209 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOSB]] | +0.89 | +0.92 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[EGR1]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 995 |
| [[EGR2]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 963 |
| [[IER2]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 796 |
| [[HES1]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 454 |
| [[SYAP1]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[FAM222A]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[EGR3]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 941 |
| [[JUNB]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[NR4A1]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 933 |
| [[BTBD19]] | +0.65 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TIPARP]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf76]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | -0.60 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[NIPSNAP3A]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TRAPPC13]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SNX4]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[EIF4ENIF1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[MIR762HG]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TRPC4AP]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[DENND10]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ILKAP]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ZNF398]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR4A2]] | B | NR4A2 activity raises FOS's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without NR4A2 | 0.013 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises FOS's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without SEMA4A | 0.024 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[ARC]] | B | ARC activity raises FOS's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without ARC | 0.026 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -0.4); signed map (6.1, 28.5). **Vector** length 167, 64.7% of its response variance represented; |z| ≥ 3 in 1,465 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.1 | +15.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.9 | +5.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.7 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.6 | +4.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +3.6 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +1.1 |
|  | [[Demeclocycline (drug)]] 0.05 µM |  | +3.5 | +1.6 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -11.6 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -9.7 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.9 | -7.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -6.8 | -6.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -6.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | Fos proto-oncogene, AP-1 transcription factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,278,826-75,282,230 (+) |
| Ensembl biotype | protein_coding |
| Also known as | c-fos, AP-1 |
| Gene groups (HGNC) | Fos transcription factor family |
| Hallmark sets | UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, HYPOXIA, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 52 pathways, smallest: Activation of the AP-1 family of transcription factors; NPAS4 regulates expression of target genes; Estrogen-dependent nuclear events downstream of ESR-membrane signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P01100](https://www.uniprot.org/uniprotkb/P01100) (Protein c-Fos):

> Nuclear phosphoprotein which forms a tight but non-covalently linked complex with the JUN/AP-1 transcription factor. In the heterodimer, FOS and JUN/AP-1 basic regions each seems to interact with symmetrical DNA half sites. On TGF-beta activation, forms a multimeric SMAD3/SMAD4/JUN/FOS complex at the AP1/SMAD-binding site to regulate TGF-beta-mediated signaling. Has a critical function in regulating the development of cells destined to form and maintain the skeleton. It is thought to have an …

**Summary**, from NCBI Gene [2353](https://www.ncbi.nlm.nih.gov/gene/2353):

> The Fos gene family consists of 4 members: FOS, FOSB, FOSL1, and FOSL2. These genes encode leucine zipper proteins that can dimerize with proteins of the JUN family, thereby forming the transcription factor complex AP-1. As such, the FOS proteins have been implicated as regulators of cell proliferation, differentiation, and transformation. In some cases, expression of the FOS gene has also been associated with apoptotic cell death. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3796) · Entrez [2353](https://www.ncbi.nlm.nih.gov/gene/2353) · UniProt [P01100](https://www.uniprot.org/uniprotkb/P01100) · Ensembl [ENSG00000170345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170345)

## Data

Gene col 9938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9938); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9938]; `tensor/DDL_lfc|DDL_z.npy` [9938]; `embed/gene_vectors.npy` [9938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9938 or target_col == 9938). Every well: [[FOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
