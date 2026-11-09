---
symbol: "SPAG5"
type: "gene"
col: 1152
ensembl_id: "ENSG00000076382"
name: "sperm associated antigen 5"
location: "17q11.2"
module: 67
arm: "+"
pooled_cpm: 58.99
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# SPAG5

*sperm associated antigen 5* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.66× (z +13.5, q 1e-38, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 7 lines (PANC-1 5.71×, KATO III 8.00×, SW480 4.10×, LoVo 5.27×, …; ⚠ cell-cycle shift, explains ~38% of this change); [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 3.95×, KATO III 5.12×, NCI-H23 3.95×, LoVo 4.20×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 5.63×, PANC-1 2.14×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.604× (z -9.9, q 2e-20, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.734× (z -6.1, q 2e-07, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RACGAP1]] (+0.91, fdr 7e-06), [[KIFC1]] (+0.91, fdr 7e-06), [[KIF22]] (+0.90, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 11 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1152.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 7 lines (PANC-1 5.71×, KATO III 8.00×, SW480 4.10×, LoVo 5.27×, …; ⚠ cell-cycle shift, explains ~38% of this change); [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 3.95×, KATO III 5.12×, NCI-H23 3.95×, LoVo 4.20×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 5.63×, PANC-1 2.14×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.66×** | +13.5 | 1e-38 | 47/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.12×** | +10.4 | 1e-22 | 42/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.75×** | +7.7 | 2e-12 | 42/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.75×** | +7.7 | 2e-12 | 40/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.58×** | +6.3 | 4e-08 | 29/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.57×** | +6.2 | 5e-08 | 32/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +6.0 | 2e-07 | 4/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~99% of this change | **1.41×** | +4.7 | 2e-04 | 26/48 (HT-29, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.23×** | +4.0 | 0.003 | 23/48 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.74×** | +4.0 | 0.004 | 24/47 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.26×** | +3.2 | 0.081 | 13/48 (HT-29, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1152.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.604×** | -9.9 | 2e-20 | 38/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.532×** | -8.8 | 6e-16 | 37/48 (H4, SW 1271, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.734×** | -6.1 | 2e-07 | 36/48 (SK-MEL-2, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -5.7 | 1e-06 | 28/48 (A498, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.647×** | -5.7 | 1e-06 | 28/48 (KATO III, A-172, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.759×** | -5.4 | 5e-06 | 36/48 (HCT15, A-172, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.705×** | -4.7 | 2e-04 | 33/48 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -4.6 | 3e-04 | 31/48 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.721×** | -4.6 | 3e-04 | 30/48 (NCI-H460, H4, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.723×** | -4.3 | 9e-04 | 33/48 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -4.2 | 0.001 | 28/48 (SK-MEL-2, NCI-H2347, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.742×** | -4.2 | 0.001 | 27/48 (Hs 766T, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.811×** | -4.1 | 0.002 | 23/48 (A498, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.753×** | -4.0 | 0.003 | 23/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.826×** | -3.8 | 0.006 | 21/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.765×** | -3.7 | 0.007 | 24/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.839× | -3.5 | 0.017 | 24/48 (HT-29, CHP-212, …) | rises with dose | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.787×** | -3.4 | 0.025 | 21/48 (SW 1088, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.028 | 20/48 (RKO, A498, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.793×** | -3.2 | 0.033 | 17/47 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.794×** | -3.2 | 0.033 | 16/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.796×** | -3.2 | 0.037 | 19/48 (HOP62, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 41.8 | 2 (2 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.72× (z +11.7) ⚠ cell-cycle shift, explains ~38% of this change | [[Selinexor (drug)]] 5 µM 0.201× (z -15.4) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.388× (z -9.1) |
| [[PANC-1 (line)]] | alt | 66.3 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.71× (z +18.2) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 65.4 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -14.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.421× (z -11.7) |
| [[H4 (line)]] | wt | 67.8 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0960× (z -12.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[KATO III (line)]] | alt | 48.2 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.00× (z +16.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 78.8 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +12.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 95.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +10.6) ⚠ cell-cycle shift, explains ~38% of this change | [[Selinexor (drug)]] 5 µM 0.464× (z -8.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H1792 (line)]] | alt | 44.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.45× (z +10.6) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 66.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.382× (z -11.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-427 (line)]] | wt | 75.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.203× (z -19.3) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LoVo (line)]] | wt | 26.9 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.27× (z +12.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LOX-IMVI (line)]] | wt | 77.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.278× (z -12.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.264× (z -11.7) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -9.0) |
| [[SW480 (line)]] | alt | 52.3 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +12.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 61.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.360× (z -9.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[CFPAC-1 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.352× (z -10.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.112× (z -9.1) |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.389× (z -9.3) ⚠ cell-cycle shift, explains ~66% of this change |
| [[hTERT-HPNE (line)]] | wt | 46.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -8.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[J82 (line)]] | alt | 58.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +10.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.128× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 86.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 60.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +8.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -16.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 75.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0639× (z -9.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW 900 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +11.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 57.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -8.5) |
| [[A549 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RACGAP1]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 771 |
| [[KIFC1]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | STRING 866 |
| [[KIF22]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 629 |
| [[TACC3]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 633 |
| [[CDCA3]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 877 |
| [[KIF2C]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 926 |
| [[CIT]] | +0.88 | +0.89 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDCA8]] | +0.88 | +0.88 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 929 |
| [[INCENP]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 525 |
| [[BUB1]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | STRING 934 |
| [[TROAP]] | +0.87 | +0.83 / +0.86 | both halves | 7e-06 | STRING 813 |
| [[BUB1B]] | +0.86 | +0.87 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 951 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises SPAG5's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without PIMREG | 0.035 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises SPAG5's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without NDC80 | 0.009 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises SPAG5's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.80× lower at baseline in the lines without PBK | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises SPAG5's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without AURKB | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MELK]] | C | MELK activity raises SPAG5's level | lines that do not express MELK (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises SPAG5's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises SPAG5's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.07× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.895). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.6, -54.4); signed map (-47.8, -41.7). **Vector** length 142, 49.1% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.79 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.75 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.70 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~99% of this change | +6.7 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +4.5 | +4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.3 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.1 | +13.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.5 | +1.9 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.0 | +0.4 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.9 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.9 | +1.8 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -7.7 | -8.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -7.5 | -9.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | -6.7 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -5.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.7 | -5.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | sperm associated antigen 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,577,565-28,599,025 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DEEPEST, MAP126, hMAP126 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96R06](https://www.uniprot.org/uniprotkb/Q96R06) (Sperm-associated antigen 5):

> Essential component of the mitotic spindle required for normal chromosome segregation and progression into anaphase. Required for chromosome alignment, normal timing of sister chromatid segregation, and maintenance of spindle pole architecture. In complex with SKAP, promotes stable microtubule-kinetochore attachments. May contribute to the regulation of separase activity. May regulate AURKA localization to mitotic spindle, but not to centrosomes and CCNB1 localization to both mitotic spindle …

**Summary**, from NCBI Gene [10615](https://www.ncbi.nlm.nih.gov/gene/10615):

> This gene encodes a protein associated with the mitotic spindle apparatus. The encoded protein may be involved in the functional and dynamic regulation of mitotic spindles. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13452) · Entrez [10615](https://www.ncbi.nlm.nih.gov/gene/10615) · UniProt [Q96R06](https://www.uniprot.org/uniprotkb/Q96R06) · Ensembl [ENSG00000076382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076382)

## Data

Gene col 1152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1152); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1152]; `tensor/DDL_lfc|DDL_z.npy` [1152]; `embed/gene_vectors.npy` [1152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1152 or target_col == 1152). Every well: [[SPAG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
