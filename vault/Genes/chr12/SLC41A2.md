---
symbol: "SLC41A2"
type: "gene"
col: 5807
ensembl_id: "ENSG00000136052"
name: "solute carrier family 41 member 2"
location: "12q23.3"
module: 14
arm: "+"
pooled_cpm: 129.42
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 25
n_dd_up_clean: 14
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLC41A2

*solute carrier family 41 member 2* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.98× (z +29.6, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.490× (z -13.7, q 8e-40, down in 34 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.709× (z -6.6, q 6e-09, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEURL3]] (+0.70, fdr 7e-06), [[MARCKS]] (+0.66, fdr 7e-06), [[TUBB2B]] (+0.66, fdr 9e-06); moves opposite to [[TMEM164]] (-0.61, fdr 7e-06), [[LTBR]] (-0.59, fdr 7e-06), [[NUP50]] (-0.58, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[IL32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.98×** | +29.6 | 0e+00 | 45/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +13.1 | 2e-36 | 35/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +10.0 | 4e-21 | 36/46 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +8.6 | 1e-15 | 32/46 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +8.5 | 2e-15 | 39/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +7.4 | 1e-11 | 32/45 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +6.1 | 9e-08 | 37/48 (A549, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +5.1 | 2e-05 | 23/47 (A549, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 2e-05 | 21/46 (A549, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +4.8 | 8e-05 | 21/46 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 9e-05 | 25/45 (LS 180, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +4.7 | 1e-04 | 27/46 (A549, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 4e-04 | 23/47 (A549, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 8e-04 | 22/46 (LS 180, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.015 | 19/46 (LS 180, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.017 | 22/46 (A549, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5807.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.490×** | -13.7 | 8e-40 | 34/47 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.481×** | -13.5 | 4e-39 | 34/42 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.617×** | -8.6 | 2e-15 | 31/43 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -8.1 | 9e-14 | 34/45 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.709×** | -6.6 | 6e-09 | 27/46 (HS-578T, SNU-423, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.798×** | -6.1 | 9e-08 | 29/46 (PANC-1, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -6.1 | 9e-08 | 28/46 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.740×** | -5.8 | 6e-07 | 28/46 (NCI-H1573, SNU-423, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.767×** | -5.1 | 3e-05 | 29/46 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.774×** | -4.9 | 5e-05 | 23/46 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.782×** | -4.7 | 1e-04 | 22/46 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.783×** | -4.7 | 1e-04 | 24/46 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.630×** | -4.6 | 2e-04 | 25/43 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.855× | -4.2 | 9e-04 | 19/46 (NCI-H1792, A549, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.671×** | -4.0 | 0.002 | 18/45 (NCI-H1792, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -3.9 | 0.003 | 19/46 (A549, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.814×** | -3.8 | 0.005 | 22/46 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.824×** | -3.7 | 0.007 | 22/46 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.828×** | -3.6 | 0.009 | 23/46 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.831×** | -3.5 | 0.011 | 21/46 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.832×** | -3.5 | 0.011 | 19/46 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -3.5 | 0.011 | 21/46 (PANC-1, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 220 | 1 | 9 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 309 | 1 | 7 (7 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.22× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 181 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.530× (z -8.8) |
| [[PANC-1 (line)]] | alt | 115 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +28.4) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.506× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 354 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 0.596× (z -8.8) |
| [[SNU-423 (line)]] | alt | 319 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -11.2) |
| [[HS-578T (line)]] | alt | 185 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.307× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 186 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.311× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 96.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +25.0) | — |
| [[NCI-H2347 (line)]] | alt | 160 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 227 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.360× (z -10.9) |
| [[A498 (line)]] | wt | 226 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 345 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +24.6) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 54.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 68.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.428× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 50.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +22.0) | — |
| [[CFPAC-1 (line)]] | alt | 99.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 50.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.9) | — |
| [[LoVo (line)]] | wt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +24.8) | — |
| [[LOX-IMVI (line)]] | wt | 65.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.9) | [[Homoharringtonine (drug)]] 0.05 µM 0.346× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 112 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 82.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 71.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +18.2) | — |
| [[H4 (line)]] | wt | 166 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.2) | [[Docetaxel (drug)]] 0.05 µM 0.348× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 137 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 80.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 171 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 137 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 47.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.75× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 98.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +20.6) | — |
| [[SW 900 (line)]] | alt | 131 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 59.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +16.3) | — |
| [[AsPC-1 (line)]] | alt | 245 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +20.1) | — |
| [[C-33 A (line)]] | alt | 55.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 60.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 125 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +21.7) | — |
| [[NCI-H2030 (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +17.8) | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.180× (z -8.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[Panc 03.27 (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +21.1) | — |
| [[SNU-1 (line)]] | wt | 68.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +13.8) | — |
| [[SW 1271 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 227 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEURL3]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[MARCKS]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TUBB2B]] | +0.66 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[OPTN]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SLC30A4]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[LACTB]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[HMGN2P46]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[NBPF19]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[C15orf48]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[DUSP8]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[RIPK2]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LRRC49]] | +0.60 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM164]] | -0.61 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[LTBR]] | -0.59 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[NUP50]] | -0.58 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[BCR]] | -0.57 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[DHX33]] | -0.54 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[DDX54]] | -0.54 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ZFYVE9]] | -0.54 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[TRRAP]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.54 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[NUP155]] | -0.54 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL32]] | B | IL32 activity raises SLC41A2's level | lines that do not express IL32 (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without IL32 | 0.005 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SLC41A2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RRAD]] | B | RRAD activity raises SLC41A2's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without RRAD | 0.037 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[KMO]] | B | KMO activity raises SLC41A2's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without KMO | 0.041 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[SYNPO]] | B | SYNPO activity raises SLC41A2's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.96× lower at baseline in the lines without SYNPO | 0.045 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[HLA-F]] | B | HLA-F activity raises SLC41A2's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without HLA-F | 0.052 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[RRAD]] | B | RRAD activity weakens SLC41A2's drug response | lines that do not express RRAD (29) vs lines expressing it (18) | the lines without RRAD respond 0.94× as strongly (z diff +0.03); strongest at Homoharringtonine 0.5 µM: 2.42x vs 1.29x (z diff -4.4) | 0.062 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; target measured in part of the lines; both ways; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers SLC41A2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[ABI3BP]] | B | ABI3BP activity raises SLC41A2's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 1.81× lower at baseline in the lines without ABI3BP | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[BDKRB2]] | B | BDKRB2 activity raises SLC41A2's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.71× lower at baseline in the lines without BDKRB2 | 0.078 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[ABI3BP]] | B | ABI3BP activity weakens SLC41A2's drug response | lines that do not express ABI3BP (30) vs lines expressing it (17) | the lines without ABI3BP respond 1.07× as strongly (z diff -0.06); strongest at Homoharringtonine 0.5 µM: 2.33x vs 1.32x (z diff -4.9) | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, 0.1); signed map (44.0, 11.1). **Vector** length 134, 46.1% of its response variance represented; |z| ≥ 3 in 1,652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +29.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +8.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +7.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.5 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.4 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.3 | +5.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.7 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.0 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.7 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.2 | -3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 41 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:104,801,801-104,958,744 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434K0427 |
| Gene groups (HGNC) | Solute carrier family 41 |
| Reactome | 3 pathways, smallest: Metal ion SLC transporters; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JW4](https://www.uniprot.org/uniprotkb/Q96JW4) (Solute carrier family 41 member 2):

> Acts as a plasma-membrane magnesium transporter. Can also mediate the transport of other divalent metal cations in an order of Ba(2+) > Ni(2+) > Co(2+) > Fe(2+) > Mn(2+) (By similarity).

**Summary**, from NCBI Gene [84102](https://www.ncbi.nlm.nih.gov/gene/84102):

> Predicted to enable magnesium ion transmembrane transporter activity. Involved in magnesium ion transport. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31045) · Entrez [84102](https://www.ncbi.nlm.nih.gov/gene/84102) · UniProt [Q96JW4](https://www.uniprot.org/uniprotkb/Q96JW4) · Ensembl [ENSG00000136052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136052)

## Data

Gene col 5807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5807); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5807]; `tensor/DDL_lfc|DDL_z.npy` [5807]; `embed/gene_vectors.npy` [5807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5807 or target_col == 5807). Every well: [[SLC41A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC41A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
