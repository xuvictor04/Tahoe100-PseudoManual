---
symbol: "SARM1"
type: "gene"
col: 41
ensembl_id: "ENSG00000004139"
name: "sterile alpha and TIR motif containing 1"
location: "17q11.2"
module: 26
arm: "+"
pooled_cpm: 17.92
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SARM1

*sterile alpha and TIR motif containing 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.26× (z +29.7, q 0e+00, up in 29 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +19.0, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.611× (z -6.9, q 3e-09, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.719× (z -4.8, q 4e-04, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (COLO 205 0.0547×, NCI-H23 0.249×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (AN3 CA 0.0714×; ⚠ toxic); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.209×); [[Berbamine (dihydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0745×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SNU-423 0.126×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H3]] (+0.67, fdr 1e-05), [[MSTO1]] (+0.67, fdr 8e-06), [[EFCAB8]] (+0.63, fdr 1e-05); moves opposite to [[C17orf58]] (-0.63, fdr 3e-05), [[HPF1]] (-0.62, fdr 4e-04), [[TFB1M]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 41.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.26×** | +29.7 | 0e+00 | 29/29 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.34×** | +29.1 | 0e+00 | 40/42 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.17×** | +22.2 | 0e+00 | 33/37 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +19.0 | 0e+00 | 42/46 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +15.2 | 0e+00 | 46/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +7.8 | 7e-13 | 32/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +6.2 | 3e-08 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +6.0 | 1e-07 | 24/43 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +5.5 | 3e-06 | 24/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.8 | 9e-05 | 11/25 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 20/48 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.001 | 19/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.8 | 0.007 | 17/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.007 | 16/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.028 | 12/47 (CFPAC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.070 | 11/47 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.090 | 6/48 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.091 | 8/48 (HOP62, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 41.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (COLO 205 0.0547×, NCI-H23 0.249×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (AN3 CA 0.0714×; ⚠ toxic); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.209×); [[Berbamine (dihydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0745×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SNU-423 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.611×** | -6.9 | 3e-09 | 27/48 (SW480, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.8 | 4e-04 | 18/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.784×** | -3.5 | 0.076 | 17/48 (PANC-1, SW1417, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | 0.805× | -3.2 | 0.18 | 15/44 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.807× | -3.1 | 0.18 | 9/48 (SW480, COLO 205, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.665× | -3.1 | 0.18 | 6/44 (C32, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 41. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.2 | 13 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.8× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 6.04× (z +18.7) | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 78.4× (z +28.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 9.57× (z +15.2) | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 19.7× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 6.70× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 12.1× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 9.77 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 21.7× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +8.7) | [[Bosentan (hydrate) (drug)]] 5 µM 0.126× (z -8.6) |
| [[A498 (line)]] | wt | 13.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 21.5× (z +18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 28.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.51× (z +8.6) ⚠ toxic; transcription drop | [[Sunitinib (drug)]] 5 µM 0.0714× (z -10.6) ⚠ toxic · without an alert: [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0745× (z -9.6) |
| [[HOP62 (line)]] | alt | 21.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 33.5× (z +22.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.71× (z +10.4) | — |
| [[LoVo (line)]] | wt | 17.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 24.7× (z +23.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 5.29× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 22.2× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +9.9) | — |
| [[SW480 (line)]] | alt | 18.4 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.90× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 9.18 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 52.8× (z +15.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 12.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.94× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 8.07× (z +12.1) | — |
| [[KATO III (line)]] | alt | 10.9 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.8× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 22.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 31.7 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.73× (z +10.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 17.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 10.8× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 15.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.42× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 16.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.242× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A-427 (line)]] | wt | 19.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +11.4) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.209× (z -10.5) |
| [[A549 (line)]] | wt | 17.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.7× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +9.2) | — |
| [[C32 (line)]] | wt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.30× (z +12.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 9.17 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 51.1× (z +16.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 8.78 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.88× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 11.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.4× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 10.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 31.0× (z +13.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +11.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.6× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +11.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0547× (z -15.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 9.85 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.1× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.53× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.99× (z +13.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +12.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 9.14× (z +10.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 41), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H3]] | +0.67 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MSTO1]] | +0.67 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[EFCAB8]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[SUMO2P17]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LINC02646]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[TBCE-1]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ALOX12-AS1]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PTOV1-AS1]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PRC1-AS1]] | +0.57 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ACYP2]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[NUP210L]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C17orf58]] | -0.63 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[HPF1]] | -0.62 | -0.24 / -0.58 | both halves | 4e-04 |  |
| [[TFB1M]] | -0.56 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ZNF184]] | -0.56 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[MRPL17]] | -0.56 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PET117]] | -0.56 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[GEMIN2]] | -0.55 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[ISCA2]] | -0.55 | -0.16 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[ABHD10]] | -0.53 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[GPATCH11]] | -0.53 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[ARMC1]] | -0.52 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[MTFP1]] | -0.51 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[KCTD6]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SARM1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.5, 26.7); signed map (31.0, -15.9). **Vector** length 89.2, 19.4% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.4 | +22.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.3 | +29.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.0 | +29.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.7 | +15.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +19.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.8 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.6 | -6.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.6 | -3.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.2 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha and TIR motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,364,356-28,404,049 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SARM, SAMD2, KIAA0524 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; TIR domain containing; Armadillo like helical domain containing |
| Reactome | 9 pathways, smallest: TRAF6-mediated induction of TAK1 complex within TLR4 complex; Activation of IRF3, IRF7 mediated by TBK1, IKKε (IKBKE); IKK complex recruitment mediated by RIP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6SZW1](https://www.uniprot.org/uniprotkb/Q6SZW1) (NAD(+) hydrolase SARM1):

> NAD(+) hydrolase, which plays a key role in axonal degeneration following injury by regulating NAD(+) metabolism. Acts as a negative regulator of MYD88- and TRIF-dependent toll-like receptor signaling pathway by promoting Wallerian degeneration, an injury-induced form of programmed subcellular death which involves degeneration of an axon distal to the injury site. Wallerian degeneration is triggered by NAD(+) depletion: in response to injury, SARM1 is activated and catalyzes cleavage of NAD(+) …

**Summary**, from NCBI Gene [23098](https://www.ncbi.nlm.nih.gov/gene/23098):

> Enables double-stranded DNA binding activity; hydrolase activity, hydrolyzing N-glycosyl compounds; and identical protein binding activity. Involved in NAD+ catabolic process; positive regulation of programmed cell death; and response to axon injury. Located in cytoplasm. Is active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17074) · Entrez [23098](https://www.ncbi.nlm.nih.gov/gene/23098) · UniProt [Q6SZW1](https://www.uniprot.org/uniprotkb/Q6SZW1) · Ensembl [ENSG00000004139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004139)

## Data

Gene col 41: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 41); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 41, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 41]; `tensor/DDL_lfc|DDL_z.npy` [41]; `embed/gene_vectors.npy` [41]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 41 or target_col == 41). Every well: [[SARM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SARM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
