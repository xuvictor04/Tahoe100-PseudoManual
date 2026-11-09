---
symbol: "CHMP3"
type: "gene"
col: 3696
ensembl_id: "ENSG00000115561"
name: "charged multivesicular body protein 3"
location: "2p11.2"
module: 83
arm: "+"
pooled_cpm: 89.05
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# CHMP3

*charged multivesicular body protein 3* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +30.7, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.20× (z +5.2, q 2e-05, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A498 3.55×, HEC-1-A 3.37×, SW480 2.79×, HOP62 4.37×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 3.21×, A-427 4.17×, AsPC-1 4.03×, HOP62 4.01×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 3.06×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 1.64×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.517× (z -19.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERMAP]] (+0.71, fdr 1e-05), [[ZNF655]] (+0.69, fdr 2e-05), [[LINC00571]] (+0.67, fdr 1e-05); moves opposite to [[MALSU1]] (-0.70, fdr 1e-05), [[MMS19]] (-0.66, fdr 1e-05), [[ATG4C]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RAB20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3696.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A498 3.55×, HEC-1-A 3.37×, SW480 2.79×, HOP62 4.37×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 3.21×, A-427 4.17×, AsPC-1 4.03×, HOP62 4.01×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 3.06×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 1.64×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +30.7 | 0e+00 | 49/49 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +28.8 | 0e+00 | 42/43 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +23.5 | 0e+00 | 44/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +6.0 | 2e-07 | 25/47 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +5.2 | 2e-05 | 21/48 (A498, KATO III, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.0 | 5e-05 | 19/50 (A-172, NCI-H2347, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.9 | 6e-05 | 16/38 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.38×** | +4.9 | 6e-05 | 21/47 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.8 | 1e-04 | 22/48 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.004 | 16/48 (Panc 03.27, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.8 | 0.007 | 6/48 (LoVo, A-427, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.13× | +3.5 | 0.023 | 3/49 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.025 | 12/48 (A498, RKO, …) | all doses, flat |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.09× | +3.4 | 0.025 | 1/48 (CFPAC-1) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.11× | +3.1 | 0.074 | 7/48 (LoVo, H4, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.11× | +3.0 | 0.095 | 8/48 (A549, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.517×** | -19.3 | 0e+00 | 47/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.552×** | -17.4 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.607×** | -14.5 | 1e-45 | 41/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.618×** | -14.0 | 1e-42 | 43/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.629×** | -13.5 | 1e-39 | 46/48 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -7.7 | 2e-12 | 25/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -7.1 | 1e-10 | 30/49 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.648×** | -6.6 | 3e-09 | 37/49 (NCI-H1792, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.719×** | -5.0 | 3e-05 | 25/45 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.900× | -4.4 | 7e-04 | 2/48 (AsPC-1, SW 900) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | 0.865× | -4.2 | 0.001 | 22/48 (BT-474, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.869× | -4.1 | 0.002 | 10/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.8 | 0.005 | 14/48 (HT-29, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.900× | -3.1 | 0.081 | 5/48 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Sildenafil (drug)]] 0.5 µM |  | 0.900× | -3.1 | 0.081 | 6/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 112 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +12.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.356× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 112 | 4 (4 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +15.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.416× (z -11.4) |
| [[PANC-1 (line)]] | alt | 115 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +19.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.440× (z -14.4) |
| [[SW480 (line)]] | alt | 94.6 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +18.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.467× (z -13.8) |
| [[A-172 (line)]] | wt | 76.8 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.64× (z +8.9) | — |
| [[A498 (line)]] | wt | 97.5 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +19.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 84.5 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +17.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.486× (z -9.1) |
| [[HT-29 (line)]] | alt | 112 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +12.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.415× (z -12.9) |
| [[KATO III (line)]] | alt | 142 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +14.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.455× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 74.1 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +15.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.429× (z -12.2) |
| [[SW1417 (line)]] | alt | 109 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.519× (z -9.4) |
| [[A-427 (line)]] | wt | 118 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.17× (z +19.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.508× (z -9.5) |
| [[COLO 205 (line)]] | alt | 123 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.286× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 106 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +18.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.610× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 64.5 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +12.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.402× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 85.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +11.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.354× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 78.9 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.431× (z -10.1) |
| [[A549 (line)]] | wt | 141 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +15.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.466× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 74.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +15.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 77.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +12.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.373× (z -8.9) |
| [[J82 (line)]] | alt | 51.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +12.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.400× (z -10.1) |
| [[LS 180 (line)]] | wt | 120 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +13.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.472× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 63.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +11.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.400× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 106 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 134 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +13.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.524× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 69.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +14.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 86.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.63× (z +9.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.344× (z -11.7) |
| [[HOP62 (line)]] | alt | 66.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +18.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 54.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 68.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 78.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 60.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +14.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 61.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +12.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 61.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 53.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +14.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 70.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +12.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 75.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +8.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 76.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0800× (z -15.8) |
| [[H4 (line)]] | wt | 87.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 64.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 96.0 | 0 | 1 | — | [[Finasteride (drug)]] 5 µM 0.105× (z -8.7) |
| [[BT-474 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 95.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERMAP]] | +0.71 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.69 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[LINC00571]] | +0.67 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.67 | +0.64 / +0.39 | both halves | 6e-05 |  |
| [[SECISBP2]] | +0.65 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[TSGA10]] | +0.65 | +0.63 / +0.27 | both halves | 3e-04 |  |
| [[OSTM1]] | +0.65 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | +0.64 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TRIP12]] | +0.64 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[WSB2]] | +0.64 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[SMIM15-AS1]] | +0.63 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[LINC01004]] | +0.63 | +0.60 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALSU1]] | -0.70 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[MMS19]] | -0.66 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.66 | -0.44 / -0.59 | both halves | 3e-05 | pathway: Autophagy |
| [[MRPS34]] | -0.63 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[XYLT2]] | -0.62 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[CDC14B]] | -0.62 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.62 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.62 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[C15orf61]] ⚠ | -0.62 | -0.37 / -0.60 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[STK32C]] | -0.61 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[POP7]] | -0.61 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[NFRKB]] | -0.61 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PHAF1]] | -0.61 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity lowers CHMP3's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.38× higher at baseline in the lines without RAB20 | 0.004 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CHMP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CHMP3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (1.3, -12.0); signed map (18.7, -27.1). **Vector** length 127, 37.8% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.8 | +23.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +28.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +30.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.4 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -9.6 | -14.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.0 | -13.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.6 | -19.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -17.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -14.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.5 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -7.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:86,503,430-86,563,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NEDF, CGI-149; previously VPS24 |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III |
| Reactome | 29 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3E7](https://www.uniprot.org/uniprotkb/Q9Y3E7) (Charged multivesicular body protein 3):

> Probable core component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal enzymes and lipids. The …

**Summary**, from NCBI Gene [51652](https://www.ncbi.nlm.nih.gov/gene/51652):

> This gene encodes a protein that sorts transmembrane proteins into lysosomes/vacuoles via the multivesicular body (MVB) pathway. This protein, along with other soluble coiled-coil containing proteins, forms part of the ESCRT-III protein complex that binds to the endosomal membrane and recruits additional cofactors for protein sorting into the MVB. This protein may also co-immunoprecipitate with a member of the IFG-binding protein superfamily. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:29865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29865) · Entrez [51652](https://www.ncbi.nlm.nih.gov/gene/51652) · UniProt [Q9Y3E7](https://www.uniprot.org/uniprotkb/Q9Y3E7) · Ensembl [ENSG00000115561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115561)

## Data

Gene col 3696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3696); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3696]; `tensor/DDL_lfc|DDL_z.npy` [3696]; `embed/gene_vectors.npy` [3696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3696 or target_col == 3696). Every well: [[CHMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
