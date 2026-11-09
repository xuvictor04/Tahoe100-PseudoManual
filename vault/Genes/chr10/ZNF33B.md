---
symbol: "ZNF33B"
type: "gene"
col: 12267
ensembl_id: "ENSG00000196693"
name: "zinc finger protein 33B"
location: "10q11.21"
module: 64
arm: "+"
pooled_cpm: 52.84
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 31
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# ZNF33B

*zinc finger protein 33B* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.39× (z +6.9, q 3e-09, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.364× (z -21.2, q 0e+00, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.530× (z -18.1, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00665]] (+0.58, fdr 2e-05), [[PGGT1B]] (+0.55, fdr 1e-04), [[GTPBP8]] (+0.53, fdr 5e-05); moves opposite to [[HOMER1]] (-0.50, fdr 2e-05), [[TIMP1]] (-0.50, fdr 4e-05), [[KCTD5]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +6.9 | 3e-09 | 36/48 (H4, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 1e-04 | 23/48 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.5 | 0.001 | 20/45 (SW1417, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.27×** | +4.4 | 0.001 | 20/48 (HOP62, LoVo, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.006 | 20/49 (RKO, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +3.6 | 0.032 | 17/48 (HOP62, A498, …) | two highest doses | low cells (technical?) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.033 | 12/48 (BT-474, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.5 | 0.033 | 16/43 (HT-29, LoVo, …) | inconsistent across doses | composition shift |
| [[Alpelisib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.033 | 13/47 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.057 | 8/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.057 | 13/47 (LoVo, RKO, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.23×** | +3.2 | 0.057 | 12/49 (BT-474, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.17× | +3.2 | 0.058 | 17/47 (MIA PaCa-2, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.364×** | -21.2 | 0e+00 | 36/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.389×** | -19.9 | 0e+00 | 36/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.519×** | -18.7 | 0e+00 | 39/47 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.530×** | -18.1 | 0e+00 | 43/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.441×** | -17.2 | 0e+00 | 36/48 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.526×** | -13.5 | 2e-39 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.535×** | -13.1 | 2e-37 | 38/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.579×** | -11.5 | 1e-28 | 42/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.603×** | -10.6 | 1e-24 | 34/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.615×** | -10.2 | 1e-22 | 33/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.631×** | -9.7 | 2e-20 | 38/47 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.662×** | -8.6 | 3e-16 | 34/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.654×** | -8.6 | 5e-16 | 31/48 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.662×** | -8.3 | 3e-15 | 30/49 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.619×** | -8.0 | 4e-14 | 36/48 (CFPAC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.677×** | -7.2 | 2e-11 | 30/47 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.777×** | -5.3 | 3e-06 | 23/47 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.660×** | -4.2 | 8e-04 | 14/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.767×** | -4.0 | 0.002 | 15/48 (MIA PaCa-2, NCI-H661, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.796×** | -3.4 | 0.013 | 16/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.713×** | -3.4 | 0.013 | 16/48 (HEC-1-A, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.889× | -3.3 | 0.016 | 5/49 (Hs 766T, KATO III, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.720×** | -3.3 | 0.017 | 13/47 (SNU-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.855× | -3.3 | 0.017 | 12/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.824×** | -2.9 | 0.063 | 9/48 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 68.8 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -22.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 83.0 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -19.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -14.5) |
| [[SNU-423 (line)]] | alt | 68.5 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -17.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -17.3) |
| [[LOX-IMVI (line)]] | wt | 36.4 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -16.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 53.3 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.2) |
| [[SW480 (line)]] | alt | 86.6 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -18.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 39.3 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -23.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -10.8) |
| [[A-427 (line)]] | wt | 57.2 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -12.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 64.1 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -16.2) |
| [[HT-29 (line)]] | alt | 67.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 40.5 | 0 | 6 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0599× (z -21.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW1417 (line)]] | alt | 65.1 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -12.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 37.3 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -12.0) |
| [[C-33 A (line)]] | alt | 113 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +8.8) | [[Belinostat (drug)]] 0.5 µM 0.419× (z -8.9) |
| [[LoVo (line)]] | wt | 74.1 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.12× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.319× (z -14.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 76.9 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.5) |
| [[A549 (line)]] | wt | 46.4 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -13.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 23.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -12.3) |
| [[LS 180 (line)]] | wt | 66.7 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -15.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 47.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 59.6 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.274× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 26.1 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.299× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 46.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -13.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 36.4 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.271× (z -12.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 83.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -11.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 49.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -13.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 45.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -8.5) |
| [[RKO (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.166× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 63.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[H4 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -18.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A498 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00665]] | +0.58 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PGGT1B]] | +0.55 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[GTPBP8]] | +0.53 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[PM20D2]] | +0.53 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[PAIP1]] | +0.53 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[TRUB1]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ZNF33A]] | +0.52 | +0.52 / +0.45 | both halves | 3e-05 | same gene group |
| [[TM7SF3]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[AIMP2]] | +0.52 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[MTPAP]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ZNF428]] | +0.51 | +0.38 / +0.41 | both halves | 6e-05 | same gene group |
| [[FLOT2]] | +0.51 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOMER1]] | -0.50 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[TIMP1]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[KCTD5]] | -0.49 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[TUBA4A]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TUBB4B]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SPSB1]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PRDX1]] | -0.47 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[PDLIM7]] | -0.46 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[GLIS3]] | -0.46 | -0.49 / -0.39 | both halves | 5e-05 | same gene group |
| [[RELL2]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ZSWIM6]] | -0.46 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[LRWD1]] | -0.46 | -0.38 / -0.43 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.212). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-21.5, 3.5); signed map (8.6, -37.7). **Vector** length 90.5, 22.8% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.7 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.8 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +0.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +4.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.1 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -18.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -11.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 33B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:42,574,185-42,638,570 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX31, KOX2; previously ZNF11B |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06732](https://www.uniprot.org/uniprotkb/Q06732) (Zinc finger protein 33B):

> May be involved in transcriptional regulation.; (Microbial infection) Facilitates Japanese encephalitis virus replication by stabilizing viral RNA and inhibiting 'Lys-63'-linked polyubiquitination of viral polymerase NS5. Instead, promotes NS5 SUMOylation that competes with its ubiquitination and degradation.

**Summary**, from NCBI Gene [7582](https://www.ncbi.nlm.nih.gov/gene/7582):

> This gene encodes a member of the zinc finger family of proteins. This gene shows decreased expression in cumulus cells derived from patients undergoing controlled ovarian stimulation. This gene is present in a gene cluster with several related zinc finger genes in the pericentromeric region of chromosome 10. Pseudogenes have been identified on chromosomes 7 and 10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:13097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13097) · Entrez [7582](https://www.ncbi.nlm.nih.gov/gene/7582) · UniProt [Q06732](https://www.uniprot.org/uniprotkb/Q06732) · Ensembl [ENSG00000196693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196693)

## Data

Gene col 12267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12267); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12267]; `tensor/DDL_lfc|DDL_z.npy` [12267]; `embed/gene_vectors.npy` [12267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12267 or target_col == 12267). Every well: [[ZNF33B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF33B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
