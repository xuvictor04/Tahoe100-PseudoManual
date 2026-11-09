---
symbol: "FNTA"
type: "gene"
col: 9664
ensembl_id: "ENSG00000168522"
name: "farnesyltransferase, CAAX box, subunit alpha"
location: "8p11.21"
module: 11
arm: "+"
pooled_cpm: 72.5
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# FNTA

*farnesyltransferase, CAAX box, subunit alpha* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +18.7, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.656× (z -10.9, q 1e-24, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.698× (z -4.8, q 7e-05, down in 18 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RKO 0.426×, HEC-1-A 0.524×, SW480 0.607×, A-172 0.552×, …; ⚠ cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 0.361×, HOP62 0.393×, A-172 0.399×, hTERT-HPNE 0.346×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.307×, SNU-423 0.326×, HOP62 0.450×; ⚠ cell-cycle shift, explains ~57% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.408×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.613×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NECAP2]] (+0.73, fdr 7e-06), [[ZNF197]] (+0.71, fdr 7e-06), [[ARL14EP]] (+0.68, fdr 7e-06); moves opposite to [[STRAP]] (-0.63, fdr 7e-06), [[GRB2]] (-0.61, fdr 1e-05), [[MFSD14B]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +18.7 | 0e+00 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +14.4 | 3e-44 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +13.7 | 3e-40 | 43/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +7.9 | 4e-13 | 32/48 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +7.1 | 1e-10 | 29/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 8e-07 | 27/48 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.7 | 1e-06 | 26/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +5.5 | 3e-06 | 24/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 8e-05 | 23/48 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.018 | 15/47 (LoVo, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.14× | +3.2 | 0.069 | 10/47 (HCT15, LoVo, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.087 | 3/48 (Hs 766T, SW 1088, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9664.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RKO 0.426×, HEC-1-A 0.524×, SW480 0.607×, A-172 0.552×, …; ⚠ cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 0.361×, HOP62 0.393×, A-172 0.399×, hTERT-HPNE 0.346×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.307×, SNU-423 0.326×, HOP62 0.450×; ⚠ cell-cycle shift, explains ~57% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.408×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.613×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.656×** | -10.9 | 1e-24 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.753×** | -10.3 | 2e-22 | 31/49 (RKO, HEC-1-A, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.673×** | -10.2 | 4e-22 | 39/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.668×** | -10.0 | 3e-21 | 28/43 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.685×** | -9.7 | 3e-20 | 31/48 (A549, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.686×** | -9.7 | 3e-20 | 35/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.781×** | -6.1 | 9e-08 | 26/50 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.786×** | -5.9 | 2e-07 | 24/48 (RKO, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.801×** | -5.3 | 9e-06 | 24/45 (C-33 A, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.828×** | -4.8 | 7e-05 | 24/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.698×** | -4.8 | 7e-05 | 18/49 (SK-MEL-2, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.835× | -4.6 | 2e-04 | 22/48 (RKO, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | 0.835× | -4.5 | 4e-04 | 20/47 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.842× | -4.4 | 4e-04 | 21/48 (HOP62, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.897× | -3.9 | 0.003 | 8/48 (SW1417, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.858× | -3.9 | 0.003 | 18/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.876× | -3.4 | 0.023 | 18/48 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.890× | -3.0 | 0.080 | 7/48 (SW48, HCT15, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 94.8 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HOP62 (line)]] | alt | 108 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.613× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 94.4 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 51.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +23.3) | — |
| [[A498 (line)]] | wt | 70.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.539× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A549 (line)]] | wt | 96.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 110 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.499× (z -9.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[LoVo (line)]] | wt | 59.0 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 3.07× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 79.3 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.16× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 84.6 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 84.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 111 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -10.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[PANC-1 (line)]] | alt | 31.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +20.9) | — |
| [[RKO (line)]] | wt | 96.1 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 75.1 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 2.44× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.408× (z -10.0) |
| [[HCT15 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HS-578T (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -10.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 82.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +17.5) | — |
| [[LOX-IMVI (line)]] | wt | 82.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H1573 (line)]] | alt | 66.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.428× (z -8.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 63.4 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.78× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 44.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +19.4) | — |
| [[SNU-423 (line)]] | alt | 58.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -12.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 63.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[CHP-212 (line)]] | wt | 67.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[COLO 205 (line)]] | alt | 50.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 69.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 77.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H23 (line)]] | alt | 68.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.8) | — |
| [[SW48 (line)]] | wt | 78.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NECAP2]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[ZNF197]] | +0.71 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[LIPT1]] | +0.67 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 | pathway: Programmed Cell Death |
| [[ZNF264]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[MAPK1IP1L]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[THAP1]] | +0.65 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[LRCH3]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZNF554]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[THAP5]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.63 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[GRB2]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[MFSD14B]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RPN2]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SMG1P2]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[PDIA6]] | -0.56 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[PPP2R5E]] | -0.56 | -0.61 / -0.49 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[CBX1]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[PARP1]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[DNAJB11]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SRPK2]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CCNY]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FNTA's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-31.2, 6.8); signed map (6.0, -19.5). **Vector** length 109, 28.9% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.9 | +14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +18.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +13.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.6 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +5.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +0.2 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.4 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.7 | -10.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.4 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.2 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | farnesyltransferase, CAAX box, subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:43,034,194-43,085,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FPTA, PGGT1A, PTAR2 |
| Gene groups (HGNC) | Prenyltransferase alpha subunit repeat containing; Farnesyltransferase, CAAX box, subunits; Protein geranylgeranyltransferase type I subunits |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 20 pathways, smallest: OAS antiviral response; GBP-mediated host defense; Inactivation, recovery and regulation of the phototransduction cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P49354](https://www.uniprot.org/uniprotkb/P49354) (Protein farnesyltransferase/geranylgeranyltransferase type-1 subunit alpha):

> Essential subunit of both the farnesyltransferase and the geranylgeranyltransferase complex. Contributes to the transfer of a farnesyl or geranylgeranyl moiety from farnesyl or geranylgeranyl diphosphate to a cysteine at the fourth position from the C-terminus of several proteins having the C-terminal sequence Cys-aliphatic-aliphatic-X. May positively regulate neuromuscular junction development downstream of MUSK via its function in RAC1 prenylation and activation.

**Summary**, from NCBI Gene [2339](https://www.ncbi.nlm.nih.gov/gene/2339):

> Prenyltransferases can attach either a farnesyl group or a geranylgeranyl group in thioether linkage to the cysteine residue of proteins with a C-terminal CAAX box. CAAX geranylgeranyltransferase and CAAX farnesyltransferase are heterodimers that share the same alpha subunit but have different beta subunits. This gene encodes the alpha subunit of these transferases. Alternative splicing results in multiple transcript variants. Related pseudogenes have been identified on chromosomes 11 and 13. …

**Accessions** — [HGNC:3782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3782) · Entrez [2339](https://www.ncbi.nlm.nih.gov/gene/2339) · UniProt [P49354](https://www.uniprot.org/uniprotkb/P49354) · Ensembl [ENSG00000168522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168522)

## Data

Gene col 9664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9664); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9664]; `tensor/DDL_lfc|DDL_z.npy` [9664]; `embed/gene_vectors.npy` [9664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9664 or target_col == 9664). Every well: [[FNTA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNTA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
