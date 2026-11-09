---
symbol: "SOX2-OT"
type: "gene"
col: 14331
ensembl_id: "ENSG00000242808"
name: "SOX2 overlapping transcript"
location: "3q26.33"
module: 26
arm: "+"
pooled_cpm: 23.33
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 21
n_dd_up_clean: 24
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SOX2-OT

*SOX2 overlapping transcript* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.57× (z +29.3, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.543× (z -8.3, q 5e-14, down in 28 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.553× (z -8.1, q 2e-13, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.79, fdr 7e-06), [[CFAP418-AS1]] (+0.77, fdr 7e-06), [[CCDC90B-AS1]] (+0.74, fdr 7e-06); moves opposite to [[WRAP73]] (-0.65, fdr 8e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.57×** | +29.3 | 0e+00 | 44/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **9.37×** | +28.2 | 0e+00 | 33/35 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **7.07×** | +26.6 | 0e+00 | 43/46 (BT-474, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.50×** | +16.4 | 0e+00 | 40/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +13.7 | 9e-41 | 32/46 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +13.2 | 5e-38 | 34/45 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.86×** | +12.0 | 4e-31 | 30/47 (A-172, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +10.0 | 1e-21 | 28/39 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +9.3 | 1e-18 | 19/29 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.43×** | +6.3 | 1e-08 | 19/25 (A-172, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.0 | 1e-07 | 23/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +6.0 | 1e-07 | 24/46 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 2e-05 | 13/47 (KATO III, SW480, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +5.0 | 2e-05 | 20/47 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +4.7 | 1e-04 | 19/47 (NCI-H2347, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.6 | 1e-04 | 17/45 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.2 | 7e-04 | 16/47 (KATO III, SW480, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.002 | 12/47 (SW480, SW48, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.002 | 9/47 (LoVo, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -8.3 | 5e-14 | 28/45 (C-33 A, C32, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.553×** | -8.1 | 2e-13 | 33/46 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -7.9 | 6e-13 | 30/46 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.566×** | -7.7 | 1e-12 | 30/45 (SW480, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -7.7 | 2e-12 | 29/46 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -7.5 | 9e-12 | 27/47 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -6.1 | 1e-07 | 27/47 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.645×** | -6.0 | 2e-07 | 23/45 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.660×** | -5.7 | 1e-06 | 23/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -4.9 | 4e-05 | 20/42 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -4.9 | 6e-05 | 16/46 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.722×** | -4.4 | 4e-04 | 17/46 (C-33 A, SW480, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.663×** | -4.0 | 0.003 | 9/47 (SW480, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.760×** | -3.7 | 0.008 | 15/47 (HEC-1-A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 0.05 µM |  | **0.782×** | -3.3 | 0.031 | 12/46 (C32, SNU-423, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.789×** | -3.2 | 0.044 | 7/47 (A549, H4, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.638×** | -3.2 | 0.045 | 11/47 (C-33 A, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.791×** | -3.2 | 0.046 | 11/47 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.795×** | -3.1 | 0.052 | 9/47 (SW1417, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 526 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0968× (z -18.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.101× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 46.1 | 5 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 8.26× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 6.27× (z +14.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 10.3 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 31.8× (z +20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +14.7) | — |
| [[SW480 (line)]] | alt | 33.5 | 2 (1 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.04× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.44× (z +8.5) | [[Ixazomib citrate (drug)]] 5 µM 0.189× (z -11.4) |
| [[C32 (line)]] | wt | 21.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 18.2× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 11.8× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.107× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 14.1 | 6 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 26.9× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 10.7× (z +13.3) | — |
| [[LoVo (line)]] | wt | 12.2 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 72.3× (z +21.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 9.09× (z +17.1) | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +14.1) | — |
| [[NCI-H23 (line)]] | alt | 35.8 | 4 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 9.46× (z +13.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0731× (z -14.9) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[A-172 (line)]] | wt | 7.98 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +16.9) | — |
| [[A-427 (line)]] | wt | 32.8 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 7.55× (z +10.9) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.0526× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~60% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.1000× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 8.78 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.85× (z +14.6) | — |
| [[RKO (line)]] | wt | 22.0 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.166× (z -9.2) |
| [[A498 (line)]] | wt | 7.44 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 60.3× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +18.0) | — |
| [[NCI-H2347 (line)]] | alt | 6.78 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +15.4) | — |
| [[PANC-1 (line)]] | alt | 15.2 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 17.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 11.7× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -9.3) ⚠ toxic |
| [[BT-474 (line)]] | alt | 18.5 | 2 | 1 | [[Auranofin (drug)]] 5 µM 66.5× (z +20.6) | [[Pimozide (drug)]] 0.05 µM 0.169× (z -8.6) |
| [[HS-578T (line)]] | alt | 19.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.43× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 24.7× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 10.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 13.6 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 41.7× (z +15.2) | — |
| [[A549 (line)]] | wt | 7.27 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 41.1× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 14.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 15.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.03× (z +10.9) | — |
| [[J82 (line)]] | alt | 10.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +11.1) | — |
| [[SNU-1 (line)]] | wt | 17.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.81× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 13.7× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.66× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.284× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.79 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[CFAP418-AS1]] | +0.77 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.74 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.74 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[MGAM]] | +0.74 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[LIX1-AS1]] | +0.73 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[NEB]] | +0.73 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[DNAH12]] | +0.72 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[ZRANB2-DT]] | +0.71 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[HCG17]] | +0.71 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.70 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.70 | +0.77 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.65 | -0.54 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SOX2-OT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF717]] | B | ZNF717 activity raises SOX2-OT's level | lines that do not express ZNF717 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without ZNF717 | 0.090 | ⚠ within organs, on part of the lines; also absent: PTGR1, CCDC110, MYBL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.796). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.2, 16.4); signed map (29.0, -8.5). **Vector** length 109, 27.9% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +26.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +29.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +16.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.9 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | +0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.7 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SOX2 overlapping transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q26.33 — chr3:180,989,762-181,836,880 (+) |
| Ensembl biotype | lncRNA |
| Also known as | DKFZp761J1324, NCRNA00043; previously SOX2OT |
| Gene groups (HGNC) | Overlapping transcripts |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [347689](https://www.ncbi.nlm.nih.gov/gene/347689):

> This gene produces alternatively spliced long non-coding RNAs. These RNAs were observed to be upregulated in tumor cells and positively correlated to expression of the SRY-box 2 gene. Overexpression of these transcripts may promote cell proliferation. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:20209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20209) · Entrez [347689](https://www.ncbi.nlm.nih.gov/gene/347689) · Ensembl [ENSG00000242808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242808)

## Data

Gene col 14331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14331); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14331]; `tensor/DDL_lfc|DDL_z.npy` [14331]; `embed/gene_vectors.npy` [14331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14331 or target_col == 14331). Every well: [[SOX2-OT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX2-OT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
