---
symbol: "RGS12"
type: "gene"
col: 8276
ensembl_id: "ENSG00000159788"
name: "regulator of G protein signaling 12"
location: "4p16.3"
module: 2
arm: "+"
pooled_cpm: 55.45
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RGS12

*regulator of G protein signaling 12* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.28× (z +6.6, q 3e-08, up in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 2.49×, LoVo 1.84×, A498 1.75×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (C32 2.75×; ⚠ cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (C32 2.03×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (C32 2.95×).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.451× (z -29.3, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIP2A]] (+0.65, fdr 7e-06), [[RNF38]] (+0.55, fdr 1e-05), [[GIT1]] (+0.55, fdr 3e-05); moves opposite to [[ANAPC13]] (-0.48, fdr 9e-05), [[MCTS1]] (-0.48, fdr 8e-05), [[NCOA7]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8276.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 2.49×, LoVo 1.84×, A498 1.75×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (C32 2.75×; ⚠ cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (C32 2.03×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (C32 2.95×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +6.6 | 3e-08 | 24/47 (HOP62, SW48, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +6.5 | 3e-08 | 27/47 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +4.7 | 4e-04 | 10/48 (NCI-H1792, J82, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.018 | 6/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.16× | +3.7 | 0.020 | 14/48 (J82, HS-578T, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.09× | +3.2 | 0.11 | 5/48 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.17× | +3.0 | 0.17 | 4/48 (AsPC-1, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[MK-3903 (drug)]] 5 µM |  | 1.24× | +3.0 | 0.17 | 5/48 (LoVo, H4, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.451×** | -29.3 | 0e+00 | 41/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.405×** | -22.6 | 0e+00 | 47/48 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.462×** | -20.1 | 0e+00 | 46/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.511×** | -17.5 | 0e+00 | 42/48 (SW480, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.326×** | -15.3 | 0e+00 | 42/49 (HOP62, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.603×** | -13.1 | 2e-37 | 35/48 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.605×** | -13.0 | 6e-37 | 36/49 (NCI-H23, AsPC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.618×** | -11.6 | 4e-29 | 30/45 (A549, RPMI-7951, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.673×** | -9.9 | 3e-21 | 24/42 (A-172, C-33 A, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -9.4 | 3e-19 | 31/48 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.712×** | -8.8 | 6e-17 | 29/48 (C32, LS 180, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.736×** | -7.6 | 1e-12 | 25/47 (HOP62, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.763×** | -7.0 | 1e-10 | 24/48 (C32, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.765×** | -6.9 | 2e-10 | 27/47 (LS 180, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.766×** | -6.9 | 2e-10 | 25/48 (J82, HepG2/C3A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -6.1 | 3e-08 | 22/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -5.9 | 1e-07 | 20/48 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.663×** | -5.6 | 7e-07 | 20/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -5.0 | 2e-05 | 21/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -4.8 | 4e-05 | 22/48 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.726×** | -4.3 | 3e-04 | 16/48 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.806×** | -4.0 | 0.001 | 12/48 (LOX-IMVI, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.904× | -3.6 | 0.005 | 7/48 (CFPAC-1, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 102 | 0 | 14 (8 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.327× (z -15.9) |
| [[LS 180 (line)]] | wt | 104 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -23.8) |
| [[A-172 (line)]] | wt | 73.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -29.0) |
| [[C32 (line)]] | wt | 125 | 4 (2 ⚠) | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.03× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -14.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 48.6 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.0) |
| [[SW480 (line)]] | alt | 60.2 | 0 | 8 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.280× (z -18.7) |
| [[HEC-1-A (line)]] | alt | 66.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -21.7) |
| [[MIA PaCa-2 (line)]] | alt | 64.4 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.247× (z -15.2) |
| [[SNU-423 (line)]] | alt | 71.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -19.2) |
| [[A-427 (line)]] | wt | 45.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -27.7) |
| [[A549 (line)]] | wt | 46.7 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0491× (z -28.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.253× (z -20.1) |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 56.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -20.6) |
| [[NCI-H23 (line)]] | alt | 52.0 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.316× (z -11.6) |
| [[A498 (line)]] | wt | 37.3 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -16.9) |
| [[J82 (line)]] | alt | 51.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -18.1) |
| [[LoVo (line)]] | wt | 39.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Harringtonine (drug)]] 5 µM 0.290× (z -13.7) |
| [[AN3 CA (line)]] | alt | 122 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.8) |
| [[HS-578T (line)]] | alt | 37.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.240× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 47.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.2) |
| [[KATO III (line)]] | alt | 56.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 49.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 89.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.191× (z -9.7) |
| [[SW48 (line)]] | wt | 62.7 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.259× (z -10.5) |
| [[BT-474 (line)]] | alt | 64.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -15.9) |
| [[C-33 A (line)]] | alt | 87.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[COLO 205 (line)]] | alt | 41.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.1) |
| [[HT-29 (line)]] | alt | 27.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 38.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.364× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 46.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0690× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.261× (z -10.4) |
| [[SNU-1 (line)]] | wt | 55.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.5) |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.9) |
| [[H4 (line)]] | wt | 92.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.344× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 70.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[Hs 766T (line)]] | wt | 77.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 45.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.623× (z -8.6) |
| [[RKO (line)]] | wt | 46.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.340× (z -9.4) |
| [[SW 1271 (line)]] | alt | 76.8 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.120× (z -8.7) |
| [[SW1417 (line)]] | alt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.4) |
| [[CHP-212 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[RNF38]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[GIT1]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ZFYVE21]] | +0.54 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[SMG6]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PBX4]] | +0.53 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[MOB2]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[AXIN1]] | +0.52 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[FBXL2]] | +0.52 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[KLC1]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MAP3K3]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[MEX3D]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC13]] | -0.48 | -0.55 / -0.37 | both halves | 9e-05 |  |
| [[MCTS1]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[NCOA7]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PUS7L]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[HMG20A]] | -0.47 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[CLCN3]] | -0.46 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[ZSCAN30]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[RANBP6]] | -0.45 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ZKSCAN4]] | -0.44 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[PPP1R3B-DT]] | -0.44 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[SLC25A46]] | -0.44 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[FNDC3A]] | -0.43 | -0.32 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.6, -1.1); signed map (-41.9, -1.8). **Vector** length 90.1, 21.9% of its response variance represented; |z| ≥ 3 in 1,301 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.9 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +3.5 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | -0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +4.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.9 | -15.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -17.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -22.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -20.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -6.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:3,293,021-3,439,913 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Regulators of G-protein signaling; PDZ domain containing |
| Reactome | 3 pathways, smallest: G alpha (i) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [O14924](https://www.uniprot.org/uniprotkb/O14924) (Regulator of G protein signaling 12):

> Regulates G protein-coupled receptor signaling cascades. Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits, thereby driving them into their inactive GDP-bound form.; [Isoform 5]: Behaves as a cell cycle-dependent transcriptional repressor, promoting inhibition of S-phase DNA synthesis.

**Summary**, from NCBI Gene [6002](https://www.ncbi.nlm.nih.gov/gene/6002):

> This gene encodes a member of the 'regulator of G protein signaling' (RGS) gene family. The encoded protein may function as a guanosine triphosphatase (GTPase)-activating protein as well as a transcriptional repressor. This protein may play a role in tumorigenesis. Multiple transcript variants encoding distinct isoforms have been identified for this gene. Other alternative splice variants have been described but their biological nature has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9994) · Entrez [6002](https://www.ncbi.nlm.nih.gov/gene/6002) · UniProt [O14924](https://www.uniprot.org/uniprotkb/O14924) · Ensembl [ENSG00000159788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159788)

## Data

Gene col 8276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8276); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8276]; `tensor/DDL_lfc|DDL_z.npy` [8276]; `embed/gene_vectors.npy` [8276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8276 or target_col == 8276). Every well: [[RGS12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
