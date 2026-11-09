---
symbol: "CERS6"
type: "gene"
col: 10235
ensembl_id: "ENSG00000172292"
name: "ceramide synthase 6"
location: "2q24.3"
module: 23
arm: "-"
pooled_cpm: 194.54
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CERS6

*ceramide synthase 6* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.80× (z +17.1, q 0e+00, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.753× (z -11.7, q 1e-28, down in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (SW1417 0.407×, NCI-H2030 0.424×, NCI-H23 0.356×, PANC-1 0.498×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HCT15 0.374×, LOX-IMVI 0.509×, PANC-1 0.540×; ⚠ cell-cycle shift, explains ~52% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (LoVo 0.459×, COLO 205 0.255×, LS 180 0.437×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.472×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPR1]] (+0.57, fdr 1e-05), [[CARMIL1]] (+0.57, fdr 1e-05), [[CYRIB]] (+0.57, fdr 1e-05); moves opposite to [[SMIM12]] (-0.58, fdr 2e-05), [[ZNF425]] (-0.57, fdr 3e-05), [[HAVCR2]] (-0.56, fdr 3e-05).
> It sits in the **-** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +17.1 | 0e+00 | 39/46 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +14.2 | 4e-43 | 39/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +13.9 | 2e-41 | 42/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +12.4 | 3e-33 | 37/46 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +10.4 | 2e-23 | 30/46 (NCI-H460, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +10.1 | 4e-22 | 32/46 (A498, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +9.8 | 9e-21 | 34/46 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +9.1 | 6e-18 | 27/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +8.6 | 4e-16 | 33/43 (A498, RKO, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +8.6 | 4e-16 | 32/46 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +7.4 | 7e-12 | 25/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +6.9 | 3e-10 | 26/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.38×** | +6.7 | 9e-10 | 34/47 (RKO, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +6.3 | 1e-08 | 23/46 (AsPC-1, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +6.1 | 5e-08 | 25/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +5.6 | 8e-07 | 26/47 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +4.6 | 1e-04 | 21/46 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 25/45 (C32, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +4.2 | 7e-04 | 18/47 (RKO, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.001 | 21/46 (C32, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10235.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (SW1417 0.407×, NCI-H2030 0.424×, NCI-H23 0.356×, PANC-1 0.498×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HCT15 0.374×, LOX-IMVI 0.509×, PANC-1 0.540×; ⚠ cell-cycle shift, explains ~52% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (LoVo 0.459×, COLO 205 0.255×, LS 180 0.437×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.472×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -11.7 | 1e-28 | 29/47 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.735×** | -8.9 | 1e-16 | 28/46 (KATO III, SW1417, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.744×** | -8.2 | 3e-14 | 29/45 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.837× | -7.3 | 4e-11 | 22/46 (HCT15, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -7.2 | 8e-11 | 27/46 (MIA PaCa-2, SW1417, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -5.6 | 2e-06 | 1/48 (HOP62) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.828×** | -5.5 | 3e-06 | 24/46 (SNU-423, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -4.7 | 2e-04 | 19/46 (SW1417, BT-474, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.855× | -4.5 | 4e-04 | 15/46 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.858× | -4.4 | 5e-04 | 15/46 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.904× | -4.1 | 0.002 | 0/47 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.869× | -4.1 | 0.002 | 17/46 (SW1417, KATO III, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.877× | -3.8 | 0.006 | 11/45 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.916× | -3.6 | 0.014 | 11/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.897× | -3.1 | 0.062 | 8/46 (LoVo, SW480, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.898× | -3.1 | 0.063 | 5/46 (NCI-H1792, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 166 | 31 (19 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.42× (z +24.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +24.3) | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 16 | 0 | [[Budesonide (drug)]] 5 µM 3.50× (z +13.0) | — |
| [[A498 (line)]] | wt | 216 | 13 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +22.7) | — |
| [[A549 (line)]] | wt | 128 | 11 (5 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.26× (z +10.6) | — |
| [[RKO (line)]] | wt | 322 | 11 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.36× (z +17.2) | — |
| [[SW480 (line)]] | alt | 312 | 9 (5 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.49× (z +16.2) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -14.3) |
| [[LoVo (line)]] | wt | 270 | 6 (3 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.75× (z +15.2) ⚠ toxic; cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.459× (z -12.3) |
| [[SW 900 (line)]] | alt | 145 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 503 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -20.0) |
| [[HEC-1-A (line)]] | alt | 316 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -13.7) |
| [[J82 (line)]] | alt | 186 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 76.8 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.98× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 104 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +16.1) | — |
| [[C32 (line)]] | wt | 127 | 4 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.88× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 2.47× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HOP62 (line)]] | alt | 118 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 116 | 3 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.77× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -11.1) |
| [[HT-29 (line)]] | alt | 308 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.31× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 180 | 2 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.90× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.7) |
| [[COLO 205 (line)]] | alt | 409 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 124 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 250 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -15.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 186 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.09× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -17.0) |
| [[HCT15 (line)]] | alt | 246 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -18.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[KATO III (line)]] | alt | 183 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -15.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 112 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.09× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 164 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.71× (z +9.4) ⚠ toxic; cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +9.2) | — |
| [[SW48 (line)]] | wt | 383 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.15× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -10.3) |
| [[A-172 (line)]] | wt | 116 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.90× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 379 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.437× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 194 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.03× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -15.5) |
| [[SNU-1 (line)]] | wt | 332 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 241 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.8) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[A-427 (line)]] | wt | 180 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.91× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 271 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[BT-474 (line)]] | alt | 250 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.494× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 252 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[CFPAC-1 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.7) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[H4 (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.29× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[RPMI-7951 (line)]] | alt | 117 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPR1]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CARMIL1]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CYRIB]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 | same gene group |
| [[SPIDR]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LDHB]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SOAT1]] | +0.56 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[LAPTM4B]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MERTK]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[HPSE]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[CHRNA5]] | +0.55 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[BLMH]] | +0.53 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[EXT2]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM12]] | -0.58 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ZNF425]] | -0.57 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[HAVCR2]] | -0.56 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[LINC01772]] | -0.56 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[CFAP53]] | -0.55 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[CKMT2-AS1]] | -0.55 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[MTG2]] | -0.54 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[KRBOX5]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[LINC02362]] | -0.53 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[ST20-MTHFS]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[TJAP1]] | -0.52 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[NMNAT1]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-4.0, 36.0); signed map (-18.2, 37.5). **Vector** length 134, 41.6% of its response variance represented; |z| ≥ 3 in 1,607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +13.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +10.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +6.1 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +10.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -8.9 | -8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -7.8 | -7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.7 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.1 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ceramide synthase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:168,456,249-168,775,134 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LASS6 |
| Gene groups (HGNC) | CERS class homeoboxes; MicroRNA protein coding host genes; Ceramide synthases |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMG9](https://www.uniprot.org/uniprotkb/Q6ZMG9) (Ceramide synthase 6):

> Ceramide synthase that catalyzes the transfer of the fatty acyl chain from acyl-CoA to a sphingoid base, with high selectivity toward palmitoyl-CoA (hexadecanoyl-CoA; C16:0-CoA). Can use different sphingoid bases as substrates for ceramide synthesis, such as sphinganine in de novo synthesis, and sphing-4E-enine (sphingosine), (4R)-hydroxysphinganine (phytosphingosine) or sphinga-4E,14Z-dienine in salvage pathways. Other fatty acyl-CoAs such as long-chain saturated stearoyl-CoA …

**Summary**, from NCBI Gene [253782](https://www.ncbi.nlm.nih.gov/gene/253782):

> Enables sphingosine N-acyltransferase activity. Involved in ceramide biosynthetic process. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23826) · Entrez [253782](https://www.ncbi.nlm.nih.gov/gene/253782) · UniProt [Q6ZMG9](https://www.uniprot.org/uniprotkb/Q6ZMG9) · Ensembl [ENSG00000172292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172292)

## Data

Gene col 10235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10235); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10235]; `tensor/DDL_lfc|DDL_z.npy` [10235]; `embed/gene_vectors.npy` [10235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10235 or target_col == 10235). Every well: [[CERS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CERS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
