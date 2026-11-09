---
symbol: "ZFPM2-AS1"
type: "gene"
col: 14728
ensembl_id: "ENSG00000251003"
name: "ZFPM2 antisense RNA 1"
location: "8q23.1"
module: 92
arm: "+"
pooled_cpm: 247.65
n_lines_expressing: 34
n_dd_up: 35
n_dd_down: 36
n_dd_up_clean: 31
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 13
direction_downstream: 17
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ZFPM2-AS1

*ZFPM2 antisense RNA 1* — 8q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.6× (z +64.4, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.370× (z -22.6, q 0e+00, down in 32 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRL4]] (+0.67, fdr 1e-05), [[BACH1]] (+0.64, fdr 1e-05), [[IL31RA]] (+0.62, fdr 1e-05); moves opposite to [[GLT8D1]] (-0.54, fdr 2e-05), [[ABHD12]] (-0.53, fdr 6e-05), [[PTPRA]] (-0.51, fdr 1e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 17 go from it, the strongest it → [[LINC00460]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.6×** | +64.4 | 0e+00 | 32/32 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.58×** | +37.6 | 0e+00 | 32/32 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **6.08×** | +33.5 | 0e+00 | 32/32 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.17×** | +32.5 | 0e+00 | 31/32 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +26.1 | 0e+00 | 32/32 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **3.79×** | +24.8 | 0e+00 | 32/32 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **3.49×** | +23.2 | 0e+00 | 32/32 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.81×** | +17.8 | 0e+00 | 28/32 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.27×** | +15.3 | 0e+00 | 30/32 (KATO III, COLO 205, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **6.20×** | +15.1 | 0e+00 | 30/33 (NCI-H460, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +12.9 | 2e-36 | 30/32 (KATO III, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +12.0 | 2e-31 | 27/32 (C32, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +9.7 | 1e-20 | 25/32 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.15×** | +9.5 | 7e-20 | 26/32 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.08×** | +8.7 | 1e-16 | 27/32 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +7.7 | 3e-13 | 26/32 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.370×** | -22.6 | 0e+00 | 32/32 (A549, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.318×** | -22.2 | 0e+00 | 33/34 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.310×** | -20.1 | 0e+00 | 33/33 (A549, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.330×** | -19.7 | 0e+00 | 32/32 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.361×** | -18.1 | 0e+00 | 29/31 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.416×** | -16.5 | 0e+00 | 32/33 (C32, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.453×** | -13.5 | 7e-40 | 31/32 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.552×** | -13.4 | 6e-39 | 28/32 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.620×** | -11.9 | 5e-31 | 28/32 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -11.9 | 9e-31 | 20/28 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.582×** | -9.3 | 1e-18 | 25/33 (SHP-77, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **0.338×** | -9.0 | 1e-17 | 30/32 (SW 900, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.595×** | -8.9 | 2e-17 | 27/31 (COLO 205, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -8.9 | 3e-17 | 26/31 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -8.6 | 4e-16 | 19/33 (CHP-212, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.393×** | -7.7 | 4e-13 | 26/32 (LOX-IMVI, C32, …) | top dose only | noisy plate (z scaled) |
| [[BI-3406 (drug)]] 5 µM |  | **0.477×** | -6.1 | 3e-08 | 24/32 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.758×** | -5.9 | 1e-07 | 19/33 (PANC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 688 | 13 (1 ⚠) | 14 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +27.8) | [[Trametinib (drug)]] 5 µM 0.243× (z -19.1) |
| [[LOX-IMVI (line)]] | wt | 708 | 12 (1 ⚠) | 14 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +45.8) | [[Trametinib (drug)]] 5 µM 0.138× (z -23.5) |
| [[NCI-H460 (line)]] | wt | 230 | 19 (3 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 28.3× (z +62.5) | [[Trametinib (drug)]] 0.5 µM 0.429× (z -14.0) |
| [[PANC-1 (line)]] | alt | 183 | 14 (1 ⚠) | 11 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +35.1) | [[Trametinib (drug)]] 0.5 µM 0.332× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 539 | 8 (1 ⚠) | 16 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +34.6) | [[Trametinib (drug)]] 0.5 µM 0.374× (z -14.7) |
| [[SW480 (line)]] | alt | 178 | 11 (1 ⚠) | 12 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +25.0) | [[Trametinib (drug)]] 0.5 µM 0.291× (z -19.5) |
| [[NCI-H2347 (line)]] | alt | 145 | 14 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 22.7× (z +42.6) | [[Binimetinib (drug)]] 0.5 µM 0.362× (z -11.7) |
| [[A549 (line)]] | wt | 199 | 11 (1 ⚠) | 10 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +44.9) | [[Trametinib (drug)]] 0.5 µM 0.256× (z -20.0) |
| [[AsPC-1 (line)]] | alt | 90.3 | 11 (1 ⚠) | 10 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +45.2) | [[Trametinib (drug)]] 0.5 µM 0.268× (z -15.8) |
| [[COLO 205 (line)]] | alt | 178 | 10 (1 ⚠) | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 28.5× (z +44.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.198× (z -14.5) |
| [[A498 (line)]] | wt | 502 | 12 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +38.4) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 619 | 8 (2 ⚠) | 12 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +15.0) | [[Trametinib (drug)]] 0.5 µM 0.365× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 190 | 11 (1 ⚠) | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +34.9) | [[Trametinib (drug)]] 5 µM 0.247× (z -15.1) |
| [[HOP62 (line)]] | alt | 196 | 13 (2 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 46.6× (z +47.6) | [[Trametinib (drug)]] 5 µM 0.231× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 579 | 10 (2 ⚠) | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +42.4) | [[Trametinib (drug)]] 5 µM 0.268× (z -15.2) |
| [[HepG2_C3A (line)]] | wt | 274 | 7 (1 ⚠) | 11 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.8× (z +27.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.174× (z -17.8) |
| [[SHP-77 (line)]] | alt | 581 | 10 (2 ⚠) | 8 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.12× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.423× (z -12.0) |
| [[SW 900 (line)]] | alt | 530 | 8 (1 ⚠) | 10 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +35.5) | [[Trametinib (drug)]] 5 µM 0.246× (z -17.1) |
| [[A-172 (line)]] | wt | 163 | 12 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 46.1× (z +44.9) | [[Cobimetinib (drug)]] 5 µM 0.270× (z -10.4) |
| [[H4 (line)]] | wt | 339 | 9 (1 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +36.2) | [[Cobimetinib (drug)]] 5 µM 0.192× (z -15.7) |
| [[KATO III (line)]] | alt | 160 | 12 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +33.6) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 0.05 µM 0.451× (z -8.6) |
| [[HS-578T (line)]] | alt | 627 | 11 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +41.1) | [[Trametinib (drug)]] 5 µM 0.395× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 67.3 | 10 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +30.0) | [[Trametinib (drug)]] 0.5 µM 0.314× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 750 | 8 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +29.2) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.386× (z -9.4) |
| [[RKO (line)]] | wt | 587 | 9 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +28.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -11.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.1) |
| [[CHP-212 (line)]] | wt | 756 | 1 | 9 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 205 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +29.6) | — |
| [[SNU-423 (line)]] | alt | 382 | 8 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +40.1) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.449× (z -8.9) |
| [[Hs 766T (line)]] | wt | 81.7 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.1× (z +37.5) | — |
| [[hTERT-HPNE (line)]] | wt | 296 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +32.8) | [[Trametinib (drug)]] 5 µM 0.383× (z -8.7) |
| [[SW 1271 (line)]] | alt | 197 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0695× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.236× (z -8.5) |
| [[SW 1088 (line)]] | alt | 233 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +14.6) | — |
| [[A-427 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 41.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 53.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 41.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 23.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRL4]] | +0.67 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[BACH1]] | +0.64 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[IL31RA]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SPRY2]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[BCAN-AS1]] | +0.61 | +0.51 / +0.68 | both halves | 1e-05 | same gene group |
| [[LINC02930]] | +0.60 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[MCTP1]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[RASGRF1]] | +0.59 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[LINC00973]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.58 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[FOSL1]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLT8D1]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[ABHD12]] | -0.53 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[PTPRA]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ILKAP]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[CCZ1]] | -0.49 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[RNF38]] | -0.48 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[GID8]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ZFPM2-AS1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |
| [[CD163L1]] | B | CD163L1 activity raises ZFPM2-AS1's level | lines that do not express CD163L1 (24) vs lines expressing it (26) | 2.31× lower at baseline in the lines without CD163L1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, ENSG00000230647, CNRIP1; maybe low, not absent |
| [[CD44]] | B | CD44 activity raises ZFPM2-AS1's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.10× lower at baseline in the lines without CD44 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[TMEM156]] | B | TMEM156 activity raises ZFPM2-AS1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without TMEM156 | 0.063 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[XKR6]] | B | XKR6 activity raises ZFPM2-AS1's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 2.09× lower at baseline in the lines without XKR6 | 0.074 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |
| [[ETV1]] | B | ETV1 activity raises ZFPM2-AS1's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 3.40× lower at baseline in the lines without ETV1 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[PCED1B]] | B | PCED1B activity raises ZFPM2-AS1's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.46× lower at baseline in the lines without PCED1B | 0.077 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[LCP1]] | B | LCP1 activity raises ZFPM2-AS1's level | lines that do not express LCP1 (33) vs lines expressing it (17) | 2.82× lower at baseline in the lines without LCP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000237268, GRIN2A, ENSG00000234352 |
| [[LIF]] | B | LIF activity raises ZFPM2-AS1's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.98× lower at baseline in the lines without LIF | 0.092 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | C | TM4SF19, TM4SF19-DYNLT2B activity raises ZFPM2-AS1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 3.83× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent with the target; co-absent genes |
| [[EVA1A]] | C | EVA1A activity raises ZFPM2-AS1's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 3.76× lower at baseline in the lines without EVA1A | 0.052 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |
| [[LINC00973]] | C | LINC00973 activity raises ZFPM2-AS1's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 3.75× lower at baseline in the lines without LINC00973 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 12, C 5. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00460]] | B | ZFPM2-AS1 activity raises LINC00460's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without ZFPM2-AS1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[PALM2AKAP2]] | B | ZFPM2-AS1 activity raises PALM2AKAP2's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 3.35× lower at baseline in the lines without ZFPM2-AS1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[MIR4280HG]] | B | ZFPM2-AS1 activity raises MIR4280HG's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without ZFPM2-AS1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[LCP1]] | B | ZFPM2-AS1 activity raises LCP1's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without ZFPM2-AS1 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[KBTBD8]] | B | ZFPM2-AS1 activity raises KBTBD8's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without ZFPM2-AS1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[CD44]] | B | ZFPM2-AS1 activity raises CD44's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 3.47× lower at baseline in the lines without ZFPM2-AS1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[TUSC3]] | B | ZFPM2-AS1 activity strengthens TUSC3's drug response | lines that do not express ZFPM2-AS1 (8) vs lines expressing it (24) | the lines without ZFPM2-AS1 respond 0.31× as strongly (z diff +3.56); strongest at Auranofin 5 µM: 0.88x vs 1.70x (z diff +6.1) | 0.060 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6; target measured in part of the lines; artifact flags |
| [[ZNF697]] | B | ZFPM2-AS1 activity raises ZNF697's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without ZFPM2-AS1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[SLC43A3]] | B | ZFPM2-AS1 activity raises SLC43A3's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 3.74× lower at baseline in the lines without ZFPM2-AS1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[PTPRA]] | B | ZFPM2-AS1 activity raises PTPRA's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.18× lower at baseline in the lines without ZFPM2-AS1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[LINC02934]] | B | ZFPM2-AS1 activity raises LINC02934's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without ZFPM2-AS1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| cells under [[Tofacitinib (drug)]] 0.05 µM | B | ZFPM2-AS1 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (32) | the lines without ZFPM2-AS1: 0.83× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.6, 10.1); signed map (11.2, 42.7). **Vector** length 124, 40.4% of its response variance represented; |z| ≥ 3 in 1,851 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.52 to 8); *MAPK family signaling cascades* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +12.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.3 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +17.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +15.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +6.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -9.0 | -22.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.7 | -22.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.9 | -16.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.9 | -20.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.4 | -19.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.7 | -18.1 |

## What is on record

|  |  |
|---|---|
| Name | ZFPM2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q23.1 — chr8:105,546,089-106,060,524 (-) |
| Ensembl biotype | lncRNA |
| Also known as | SCAT3 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50698) · Entrez [102723356](https://www.ncbi.nlm.nih.gov/gene/102723356) · Ensembl [ENSG00000251003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251003)

## Data

Gene col 14728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14728); `tables/drug_effects.parquet` (86 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14728]; `tensor/DDL_lfc|DDL_z.npy` [14728]; `embed/gene_vectors.npy` [14728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14728 or target_col == 14728). Every well: [[ZFPM2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFPM2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
