---
symbol: "KRR1"
type: "gene"
col: 3245
ensembl_id: "ENSG00000111615"
name: "KRR1 small subunit processome component"
location: "12q21.2"
module: 85
arm: "-"
pooled_cpm: 104.38
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# KRR1

*KRR1 small subunit processome component* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +19.0, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.18× (z +15.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.816× (z -3.8, q 0.095, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.692×, NCI-H23 0.809×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.493×, RKO 0.515×; ⚠ cell-cycle shift, explains ~40% of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.170×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.500×); [[Tucidinostat (drug)]] 5 µM in 1 line (RKO 0.534×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLHC1]] (+0.68, fdr 2e-04), [[PCBP1-AS1]] (+0.65, fdr 5e-05), [[EMG1]] (+0.64, fdr 1e-05); moves opposite to [[YIF1B]] (-0.69, fdr 1e-05), [[RRAS]] (-0.69, fdr 3e-05), [[TMEM256]] (-0.67, fdr 3e-05).
> It sits in the **-** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.69×** | +19.0 | 0e+00 | 48/49 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.30×** | +15.4 | 0e+00 | 43/44 (C32, Panc 03.27, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +15.0 | 0e+00 | 45/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +14.9 | 0e+00 | 42/45 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.66×** | +13.8 | 2e-41 | 42/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +12.9 | 5e-36 | 43/48 (SW480, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +10.7 | 9e-25 | 34/49 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.71×** | +9.9 | 2e-21 | 42/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +9.6 | 5e-20 | 41/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +9.0 | 1e-17 | 43/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.56×** | +8.6 | 4e-16 | 42/48 (SW480, NCI-H1792, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.7 | 7e-13 | 37/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.6 | 1e-12 | 35/50 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.47×** | +7.5 | 3e-12 | 37/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +7.3 | 2e-11 | 41/48 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +6.8 | 3e-10 | 37/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.8 | 4e-05 | 32/48 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +4.3 | 5e-04 | 28/48 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.001 | 25/47 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.007 | 21/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.010 | 24/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.010 | 23/48 (NCI-H1792, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.692×, NCI-H23 0.809×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.493×, RKO 0.515×; ⚠ cell-cycle shift, explains ~40% of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.170×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.500×); [[Tucidinostat (drug)]] 5 µM in 1 line (RKO 0.534×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.816×** | -3.8 | 0.095 | 22/47 (AN3 CA, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -3.4 | 0.20 | 12/48 (RKO, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.828× | -3.1 | 0.31 | 20/50 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 168 | 12 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +17.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.20× (z +16.1) | — |
| [[C32 (line)]] | wt | 104 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 67.7 | 10 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 87.4 | 10 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 87.0 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +18.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +17.0) | — |
| [[A549 (line)]] | wt | 64.0 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 83.1 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.47× (z +10.3) | — |
| [[SW480 (line)]] | alt | 126 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.74× (z +15.5) | — |
| [[SNU-423 (line)]] | alt | 71.5 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.86× (z +11.6) | — |
| [[A-172 (line)]] | wt | 62.7 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.71× (z +11.0) | — |
| [[A-427 (line)]] | wt | 485 | 2 (2 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -14.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 78.4 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +16.3) | — |
| [[PANC-1 (line)]] | alt | 136 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +9.8) | — |
| [[A498 (line)]] | wt | 80.6 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 68.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 47.4 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 152 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.32× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.6) |
| [[KATO III (line)]] | alt | 69.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.14× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 129 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.14× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 63.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 61.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 135 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 103 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.4) | — |
| [[RKO (line)]] | wt | 334 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.534× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 88.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.70× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 68.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.54× (z +9.0) | [[Lonafarnib (drug)]] 5 µM 0.180× (z -8.6) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 77.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 83.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 156 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 60.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 89.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.48× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 88.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[COLO 205 (line)]] | alt | 91.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 68.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.35× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 98.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 61.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 70.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.9) | — |
| [[NCI-H596 (line)]] | alt | 94.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.170× (z -18.2) |
| [[RPMI-7951 (line)]] | alt | 68.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 110 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.6) | — |
| [[SW48 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLHC1]] | +0.68 | +0.67 / +0.32 | both halves | 2e-04 |  |
| [[PCBP1-AS1]] | +0.65 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[EMG1]] | +0.64 | +0.64 / +0.50 | both halves | 1e-05 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[CSTF3]] | +0.64 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | +0.64 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ARRDC3-AS1]] | +0.63 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[UTP20]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[GPATCH4]] | +0.63 | +0.72 / +0.44 | both halves | 3e-05 | STRING 642 |
| [[ITPA]] | +0.62 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[DNAJC11]] | +0.62 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[GLIPR1-AS1]] | +0.62 | +0.54 / +0.42 | both halves | 4e-05 | ⚠ **readthrough risk**: GLIPR1-AS1 lies 1.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ZNF655]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[EIF5]] | +0.62 | +0.63 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | -0.69 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[RRAS]] | -0.69 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[TMEM256]] | -0.67 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[PEDS1]] | -0.65 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[ANAPC11]] | -0.65 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[ARL3]] | -0.65 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.64 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[METRN]] | -0.64 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.64 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[SNN]] | -0.63 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SLC17A5]] | -0.63 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[GNB2]] | -0.63 | -0.67 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KRR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **-** arm (projection on the module's main direction -0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.1, -1.4); signed map (21.2, -7.4). **Vector** length 82.6, 24.0% of its response variance represented; |z| ≥ 3 in 1,400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +15.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +12.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +9.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +6.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~77% of this change | -3.5 | +3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | KRR1 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:75,490,863-75,511,636 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIP-1; previously HRB2 |
| Gene groups (HGNC) | SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13601](https://www.uniprot.org/uniprotkb/Q13601) (KRR1 small subunit processome component homolog):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome.

**Summary**, from NCBI Gene [11103](https://www.ncbi.nlm.nih.gov/gene/11103):

> Enables RNA binding activity. Involved in ribosomal small subunit biogenesis. Located in nucleolus and nucleoplasm. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5176) · Entrez [11103](https://www.ncbi.nlm.nih.gov/gene/11103) · UniProt [Q13601](https://www.uniprot.org/uniprotkb/Q13601) · Ensembl [ENSG00000111615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111615)

## Data

Gene col 3245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3245); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3245]; `tensor/DDL_lfc|DDL_z.npy` [3245]; `embed/gene_vectors.npy` [3245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3245 or target_col == 3245). Every well: [[KRR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
