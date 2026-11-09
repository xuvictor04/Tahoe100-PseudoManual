---
symbol: "SDC4"
type: "gene"
col: 4485
ensembl_id: "ENSG00000124145"
name: "syndecan 4"
location: "20q13.12"
module: 141
arm: "+"
pooled_cpm: 192.0
n_lines_expressing: 45
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 16
direction_downstream: 9
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# SDC4

*syndecan 4* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.62× (z +19.8, q 0e+00, up in 39 of 43 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 3.78× (z +18.6, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.619× (z -6.6, q 3e-08, down in 32 of 43 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.666× (z -5.7, q 3e-06, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKB2]] (+0.62, fdr 1e-05), [[JUNB]] (+0.60, fdr 1e-05), [[PLEC]] (+0.59, fdr 1e-05); moves opposite to [[PSMA1]] (-0.59, fdr 1e-05), [[NAGPA]] (-0.56, fdr 1e-05), [[PSMB5]] (-0.51, fdr 2e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[CCL20]] → it (grade B ⚠); 9 go from it, the strongest it → [[SMAD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.62×** | +19.8 | 0e+00 | 39/43 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.78×** | +18.6 | 0e+00 | 42/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +15.3 | 0e+00 | 41/43 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.75×** | +14.7 | 0e+00 | 41/43 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.39×** | +12.6 | 2e-34 | 38/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.27×** | +11.7 | 2e-29 | 39/45 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +11.4 | 2e-28 | 37/43 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +11.2 | 2e-27 | 38/43 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +10.6 | 1e-24 | 36/43 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.07×** | +10.6 | 2e-24 | 35/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.04×** | +10.4 | 2e-23 | 41/43 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.89×** | +9.3 | 1e-18 | 37/43 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.83×** | +8.8 | 6e-17 | 39/43 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +7.8 | 3e-13 | 34/44 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.45×** | +5.4 | 3e-06 | 27/44 (PANC-1, LoVo, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.3 | 5e-06 | 26/44 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.44×** | +5.3 | 5e-06 | 30/44 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 5e-04 | 23/43 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.023 | 18/43 (SW1417, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.082 | 19/43 (NCI-H2030, HCT15, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4485.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.619×** | -6.6 | 3e-08 | 32/43 (H4, AsPC-1, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.666×** | -5.7 | 3e-06 | 38/44 (H4, HepG2/C3A, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.678×** | -5.6 | 3e-06 | 31/43 (HCT15, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -5.3 | 2e-05 | 31/43 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -4.9 | 1e-04 | 26/43 (HOP62, H4, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.497×** | -4.6 | 4e-04 | 32/42 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.733×** | -4.5 | 5e-04 | 24/43 (H4, AsPC-1, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.807×** | -4.3 | 0.001 | 21/43 (HCT15, SW48, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.775×** | -3.5 | 0.028 | 21/43 (NCI-H661, AsPC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.028 | 22/42 (HCT15, SW48, …) | two highest doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.845× | -3.4 | 0.030 | 19/43 (Panc 03.27, HEC-1-A, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.4 | 0.033 | 16/43 (SW48, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.607×** | -3.3 | 0.043 | 19/40 (HOP62, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.850× | -3.2 | 0.052 | 21/44 (HCT15, SW480, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.802×** | -3.2 | 0.052 | 21/43 (A-172, HCT15, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.798×** | -3.0 | 0.085 | 19/43 (HCT15, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 278 | 5 (4 ⚠) | 10 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.69× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.45× (z +10.2) | [[Trametinib (drug)]] 5 µM 0.237× (z -11.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.297× (z -10.1) |
| [[PANC-1 (line)]] | alt | 82.0 | 15 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +35.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 21.1× (z +28.7) | — |
| [[HOP62 (line)]] | alt | 168 | 12 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +28.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 13.9× (z +26.0) | [[Ixazomib citrate (drug)]] 5 µM 0.346× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 78.5 | 12 (5 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.65× (z +14.9) | — |
| [[hTERT-HPNE (line)]] | wt | 147 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +24.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 12.7× (z +19.4) | — |
| [[NCI-H1792 (line)]] | alt | 151 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +23.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.80× (z +16.9) | — |
| [[A-172 (line)]] | wt | 153 | 8 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +17.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.22× (z +13.2) | [[Ponatinib (drug)]] 5 µM 0.367× (z -8.5) |
| [[BT-474 (line)]] | alt | 244 | 9 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 8.89× (z +17.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 4.03× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 299 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +23.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.71× (z +18.9) | — |
| [[AsPC-1 (line)]] | alt | 601 | 5 (3 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.51× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.68× (z +10.7) | [[Trametinib (drug)]] 0.5 µM 0.484× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 191 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +17.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.49× (z +15.2) | — |
| [[NCI-H1573 (line)]] | alt | 254 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +15.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 85.0 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +18.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.06× (z +17.6) | — |
| [[NCI-H2347 (line)]] | alt | 468 | 8 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.07× (z +14.2) | — |
| [[Panc 03.27 (line)]] | alt | 287 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +29.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.43× (z +21.7) | — |
| [[SW48 (line)]] | wt | 217 | 5 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 6.45× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.16× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~4% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.361× (z -9.0) |
| [[A498 (line)]] | wt | 185 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +24.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.47× (z +17.7) | — |
| [[C32 (line)]] | wt | 62.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +14.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.48× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 173 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +18.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.55× (z +14.7) | — |
| [[SK-MEL-2 (line)]] | alt | 96.2 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +11.4) | — |
| [[SW1417 (line)]] | alt | 292 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +22.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.09× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 658 | 6 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.50× (z +18.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.78× (z +12.8) | — |
| [[J82 (line)]] | alt | 228 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +27.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.6× (z +20.5) | — |
| [[KATO III (line)]] | alt | 132 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +15.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.76× (z +9.9) | — |
| [[LoVo (line)]] | wt | 64.9 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.82× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 202 | 6 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.64× (z +14.7) | — |
| [[RPMI-7951 (line)]] | alt | 255 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.59× (z +20.0) | — |
| [[SW 900 (line)]] | alt | 202 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.74× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 248 | 4 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +14.0) ⚠ position not correctable · without an alert: [[Tucidinostat (drug)]] 5 µM 2.70× (z +10.4) | [[Ixazomib citrate (drug)]] 5 µM 0.309× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 306 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +25.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.64× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 140 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.76× (z +9.9) | [[Ixazomib citrate (drug)]] 5 µM 0.417× (z -9.1) |
| [[A549 (line)]] | wt | 127 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.75× (z +11.3) | — |
| [[H4 (line)]] | wt | 306 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.233× (z -12.9) |
| [[Hs 766T (line)]] | wt | 209 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +14.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.95× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 144 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.14× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 235 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 170 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.79× (z +11.7) | — |
| [[A-427 (line)]] | wt | 43.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 26.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 96.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 805 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 394 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKB2]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[JUNB]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PLEC]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[MAP2K3]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZMIZ2]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[EPHA2]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CCL20]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EBI3]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[EHD1]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IRAK2]] | +0.54 | +0.40 / +0.55 | both halves | 5e-05 | pathway: SARS-CoV-2 Infection |
| [[CD83]] | +0.53 | +0.43 / +0.57 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ADGRE5]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA1]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[NAGPA]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[PSMB5]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PSMB2]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[BABAM1]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ELMOD3]] | -0.50 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[SUPV3L1]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ZFYVE9]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[VPS50]] | -0.50 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[PSMC2]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[GTF3C3]] | -0.49 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ZW10]] | -0.49 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 13, C 3. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | B | CCL20 activity raises SDC4's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.79× lower at baseline in the lines without CCL20 | 0.003 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[SMAD3]] | B | SMAD3 activity raises SDC4's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 4.47× lower at baseline in the lines without SMAD3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[GOLT1A]] | B | GOLT1A activity raises SDC4's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.20× lower at baseline in the lines without GOLT1A | 0.013 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[AREG]] | B | AREG activity raises SDC4's level | lines that do not express AREG (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without AREG | 0.014 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[BIRC3]] | B | BIRC3 activity raises SDC4's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 4.85× lower at baseline in the lines without BIRC3 | 0.026 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[ABTB2]] | B | ABTB2 activity raises SDC4's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 3.77× lower at baseline in the lines without ABTB2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[LAMB3]] | B | LAMB3 activity raises SDC4's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without LAMB3 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[LONRF3]] | B | LONRF3 activity raises SDC4's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without LONRF3 | 0.042 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |
| [[KLF5]] | B | KLF5 activity raises SDC4's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without KLF5 | 0.065 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[TNFRSF1B]] | B | TNFRSF1B activity raises SDC4's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 2.11× lower at baseline in the lines without TNFRSF1B | 0.067 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| [[SERPINB1]] | B | SERPINB1 activity raises SDC4's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.59× lower at baseline in the lines without SERPINB1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[LAMC2]] | B | LAMC2 activity raises SDC4's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.91× lower at baseline in the lines without LAMC2 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD3]] | B | SDC4 activity raises SMAD3's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 4.49× lower at baseline in the lines without SDC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2; its own permutation p |
| [[S100A10]] | B | SDC4 activity raises S100A10's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 2.47× lower at baseline in the lines without SDC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2; its own permutation p |
| [[EHD1]] | B | SDC4 activity raises EHD1's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without SDC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2; its own permutation p |
| [[AGRN]] | B | SDC4 activity raises AGRN's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 2.06× lower at baseline in the lines without SDC4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |
| [[ABTB2]] | B | SDC4 activity raises ABTB2's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 3.41× lower at baseline in the lines without SDC4 | 0.082 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |
| [[LONRF3]] | B | SDC4 activity raises LONRF3's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 4.77× lower at baseline in the lines without SDC4 | 0.087 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |
| [[PLEC]] | B | SDC4 activity raises PLEC's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 3.11× lower at baseline in the lines without SDC4 | 0.090 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |
| [[ANXA5]] | B | SDC4 activity raises ANXA5's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without SDC4 | 0.099 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |
| [[SLC16A3]] | C | SDC4 activity raises SLC16A3's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 5.54× lower at baseline in the lines without SDC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.3, 1.0); signed map (7.5, 28.1). **Vector** length 128, 43.0% of its response variance represented; |z| ≥ 3 in 1,712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.0 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.1 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.9 | +11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +10.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.8 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | -10.5 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -9.4 | -5.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | -7.5 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.3 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.3 | -4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.5 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | syndecan 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,325,288-45,348,424 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SYND4, amphiglycan, ryudocan |
| Gene groups (HGNC) | Syndecans |
| Hallmark sets | HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 38 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; Defective B3GALT6 causes EDSP2 and SEMDJL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P31431](https://www.uniprot.org/uniprotkb/P31431) (Syndecan-4):

> Cell surface proteoglycan which regulates exosome biogenesis in concert with SDCBP and PDCD6IP.

**Summary**, from NCBI Gene [6385](https://www.ncbi.nlm.nih.gov/gene/6385):

> The protein encoded by this gene is a transmembrane (type I) heparan sulfate proteoglycan that functions as a receptor in intracellular signaling. The encoded protein is found as a homodimer and is a member of the syndecan proteoglycan family. This gene is found on chromosome 20, while a pseudogene has been found on chromosome 22. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10661) · Entrez [6385](https://www.ncbi.nlm.nih.gov/gene/6385) · UniProt [P31431](https://www.uniprot.org/uniprotkb/P31431) · Ensembl [ENSG00000124145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124145)

## Data

Gene col 4485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4485); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4485]; `tensor/DDL_lfc|DDL_z.npy` [4485]; `embed/gene_vectors.npy` [4485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4485 or target_col == 4485). Every well: [[SDC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
