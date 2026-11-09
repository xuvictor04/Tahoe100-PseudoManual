---
symbol: "PPP2R2A"
type: "gene"
col: 13317
ensembl_id: "ENSG00000221914"
name: "protein phosphatase 2 regulatory subunit Balpha"
location: "8p21.2"
module: 23
arm: "-"
pooled_cpm: 298.77
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 14
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PPP2R2A

*protein phosphatase 2 regulatory subunit Balpha* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.59× (z +17.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.383× (z -17.3, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.565× (z -15.1, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTDC1]] (+0.62, fdr 1e-05), [[UGCG]] (+0.61, fdr 1e-05), [[RYBP]] (+0.60, fdr 1e-05); moves opposite to [[PPIP5K2]] (-0.59, fdr 1e-05), [[ACAD9]] (-0.56, fdr 1e-04), [[ATXN1L]] (-0.56, fdr 3e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.59×** | +17.8 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +15.6 | 0e+00 | 47/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.70×** | +12.8 | 5e-35 | 47/49 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.91×** | +12.1 | 1e-31 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.57×** | +11.9 | 2e-30 | 38/48 (COLO 205, A498, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.12×** | +11.1 | 1e-26 | 47/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +11.0 | 3e-26 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +11.0 | 3e-26 | 44/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.7 | 2e-16 | 44/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +8.4 | 2e-15 | 42/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +7.2 | 4e-11 | 34/48 (KATO III, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.49×** | +5.9 | 2e-07 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.9 | 2e-07 | 35/48 (KATO III, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +5.7 | 5e-07 | 28/48 (COLO 205, NCI-H460, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 9e-06 | 36/49 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.39×** | +4.9 | 3e-05 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 2e-04 | 31/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.5 | 2e-04 | 19/49 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 0.001 | 25/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.383×** | -17.3 | 0e+00 | 44/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -15.1 | 0e+00 | 45/49 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.504×** | -12.8 | 3e-35 | 45/49 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.576×** | -9.5 | 2e-19 | 36/45 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -6.7 | 2e-09 | 34/48 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.720×** | -5.9 | 3e-07 | 32/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -5.9 | 3e-07 | 34/50 (LS 180, SW48, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -5.3 | 7e-06 | 32/48 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.767×** | -5.0 | 4e-05 | 36/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.797×** | -4.2 | 0.001 | 27/48 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.814×** | -3.8 | 0.006 | 25/48 (COLO 205, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.820×** | -3.7 | 0.010 | 25/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.828×** | -3.5 | 0.018 | 20/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.834× | -3.4 | 0.028 | 20/48 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.836× | -3.4 | 0.029 | 20/48 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.837× | -3.3 | 0.030 | 17/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.051 | 20/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.845× | -3.1 | 0.052 | 20/47 (LOX-IMVI, AsPC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.813×** | -3.1 | 0.056 | 23/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 227 | 14 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.19× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -10.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 321 | 11 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -13.5) |
| [[KATO III (line)]] | alt | 383 | 8 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +20.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -16.3) |
| [[LoVo (line)]] | wt | 429 | 9 (3 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -21.9) |
| [[LS 180 (line)]] | wt | 620 | 5 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -18.6) |
| [[NCI-H2347 (line)]] | alt | 443 | 3 | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 598 | 7 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -15.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 225 | 8 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +20.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 376 | 5 (2 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.66× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 256 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -30.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 137 | 8 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.07× (z +21.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -12.3) |
| [[A-172 (line)]] | wt | 245 | 3 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +17.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.8) |
| [[BT-474 (line)]] | alt | 360 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -13.9) |
| [[HCT15 (line)]] | alt | 447 | 5 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.8) |
| [[HT-29 (line)]] | alt | 187 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 444 | 4 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.95× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.300× (z -14.2) ⚠ toxic; cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 242 | 6 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.81× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -13.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 295 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 246 | 3 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.8) |
| [[SW48 (line)]] | wt | 744 | 4 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.73× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -12.8) |
| [[A-427 (line)]] | wt | 299 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.36× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -11.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 323 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 269 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 215 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -9.7) |
| [[RKO (line)]] | wt | 529 | 3 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.44× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 284 | 1 | 5 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.64× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.6) |
| [[SHP-77 (line)]] | alt | 289 | 4 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -13.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 295 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 301 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.1) |
| [[H4 (line)]] | wt | 201 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.37× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 290 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.0) |
| [[Hs 766T (line)]] | wt | 206 | 4 (2 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.10× (z +9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.97× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 378 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 232 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.67× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -10.0) |
| [[A549 (line)]] | wt | 307 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.96× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -22.1) |
| [[HOP62 (line)]] | alt | 172 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 332 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 168 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.07× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +9.0) | — |
| [[J82 (line)]] | alt | 135 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 453 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 219 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +13.9) | — |
| [[C32 (line)]] | wt | 118 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 138 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 319 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.5) |
| [[AN3 CA (line)]] | alt | 269 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 9 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTDC1]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[UGCG]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RYBP]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[FAM133B]] | +0.59 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ZC3H15]] | +0.59 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[CFD]] | +0.57 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[TSC22D2]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[EIF4A2]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[TTC3P1]] | +0.53 | +0.19 / +0.54 | ⚠ one half (not replicated) | 9e-04 |  |
| [[LYPD5]] | +0.52 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[SNHG15]] | +0.52 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[RPL22L1]] ⚠ | +0.52 | +0.34 / +0.41 | both halves | 1e-04 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); ⚠ in the vector space only through flagged drug-doses |
| [[ARHGAP32]] | +0.51 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[DDIT4]] | +0.51 | +0.43 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIP5K2]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ACAD9]] | -0.56 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[ATXN1L]] | -0.56 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[DCTN5]] | -0.56 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[DVL3]] | -0.56 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[KIAA0753]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[LSM1]] | -0.54 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ACO2]] | -0.54 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[TRIM39]] | -0.54 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[LY6G5B]] | -0.53 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[GLYR1]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[MCM3AP]] | -0.52 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PPP2R2A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.243). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-9.9, 17.0); signed map (-9.1, 17.8). **Vector** length 92.5, 40.6% of its response variance represented; |z| ≥ 3 in 1,677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +16.7 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +12.6 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | -17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | -12.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.9 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.6 | +12.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.4 | +17.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -15.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | +0.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit Balpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:26,291,508-26,372,680 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PR52A, PR55A, B55A, PR55alpha, B55alpha |
| Gene groups (HGNC) | WD repeat domain containing; Protein phosphatase 2 regulatory subunits |
| Reactome | 20 pathways, smallest: Initiation of Nuclear Envelope (NE) Reformation; Turbulent (oscillatory, disturbed) flow shear stress activates signaling by PIEZO1 and integrins in endothelial cells; Cyclin A/B1/B2 associated events during G2/M transition |
| Matched by | ensembl_id |

**Function**, from UniProt [P63151](https://www.uniprot.org/uniprotkb/P63151) (Serine/threonine-protein phosphatase 2A 55 kDa regulatory subunit B alpha isoform):

> Substrate-recognition subunit of protein phosphatase 2A (PP2A) that plays a key role in cell cycle by controlling mitosis entry and exit. Involved in chromosome clustering during late mitosis by mediating dephosphorylation of MKI67 (By similarity). Essential for serine/threonine-protein phosphatase 2A-mediated dephosphorylation of WEE1, preventing its ubiquitin-mediated proteolysis, increasing WEE1 protein levels, and promoting the G2/M checkpoint.

**Summary**, from NCBI Gene [5520](https://www.ncbi.nlm.nih.gov/gene/5520):

> The product of this gene belongs to the phosphatase 2 regulatory subunit B family. Protein phosphatase 2 is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The B regulatory subunit might modulate substrate selectivity and catalytic activity. This …

**Accessions** — [HGNC:9304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9304) · Entrez [5520](https://www.ncbi.nlm.nih.gov/gene/5520) · UniProt [P63151](https://www.uniprot.org/uniprotkb/P63151) · Ensembl [ENSG00000221914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221914)

## Data

Gene col 13317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13317); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13317]; `tensor/DDL_lfc|DDL_z.npy` [13317]; `embed/gene_vectors.npy` [13317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13317 or target_col == 13317). Every well: [[PPP2R2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
