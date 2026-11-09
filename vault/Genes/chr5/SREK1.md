---
symbol: "SREK1"
type: "gene"
col: 7749
ensembl_id: "ENSG00000153914"
name: "splicing regulatory glutamic acid and lysine rich protein 1"
location: "5q12.3"
module: 51
arm: "+"
pooled_cpm: 236.64
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SREK1

*splicing regulatory glutamic acid and lysine rich protein 1* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +33.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.330× (z -26.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF4B]] (+0.74, fdr 7e-06), [[SCAF8]] (+0.69, fdr 9e-06), [[NFYC]] (+0.67, fdr 7e-06); moves opposite to [[TOR1B]] (-0.66, fdr 1e-05), [[MYO9B]] (-0.63, fdr 1e-05), [[CAP1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +33.2 | 0e+00 | 48/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +20.0 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.30×** | +19.1 | 0e+00 | 47/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +18.6 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +18.6 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +13.5 | 8e-40 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +13.0 | 7e-37 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +11.2 | 2e-27 | 47/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +11.2 | 3e-27 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +10.0 | 9e-22 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +9.2 | 2e-18 | 42/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +7.2 | 4e-11 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +6.4 | 8e-09 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.9 | 4e-05 | 26/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +4.6 | 1e-04 | 25/45 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Flutamide (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.044 | 11/48 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.074 | 20/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.077 | 22/48 (LoVo, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.330×** | -26.4 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.337×** | -25.9 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.380×** | -23.1 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -20.4 | 0e+00 | 47/49 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.569×** | -13.4 | 4e-39 | 48/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -10.8 | 2e-25 | 42/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.639×** | -10.7 | 1e-24 | 47/48 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -9.8 | 6e-21 | 43/50 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.775×** | -8.6 | 5e-16 | 33/48 (NCI-H2347, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -8.3 | 9e-15 | 41/48 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.546×** | -7.6 | 2e-12 | 47/49 (SW480, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.804×** | -5.2 | 9e-06 | 27/48 (SW480, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.865× | -3.5 | 0.023 | 8/47 (SNU-423, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.908× | -3.2 | 0.049 | 10/48 (SW480, HT-29, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.056 | 9/48 (LS 180, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 295 | 13 (2 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +26.7) | [[Panobinostat (drug)]] 5 µM 0.271× (z -29.9) |
| [[LoVo (line)]] | wt | 270 | 13 (3 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +24.6) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 237 | 14 (2 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +29.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -20.0) |
| [[A549 (line)]] | wt | 195 | 11 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +29.2) | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -19.4) |
| [[HEC-1-A (line)]] | alt | 228 | 10 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +25.3) | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -19.6) |
| [[A-427 (line)]] | wt | 260 | 9 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.312× (z -19.1) |
| [[KATO III (line)]] | alt | 200 | 7 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +21.2) | [[Panobinostat (drug)]] 5 µM 0.296× (z -21.0) |
| [[LS 180 (line)]] | wt | 267 | 7 (1 ⚠) | 8 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -18.9) |
| [[NCI-H2347 (line)]] | alt | 419 | 6 (1 ⚠) | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +27.1) | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -22.5) |
| [[PANC-1 (line)]] | alt | 250 | 8 (1 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +27.3) | [[Panobinostat (drug)]] 5 µM 0.336× (z -19.5) |
| [[COLO 205 (line)]] | alt | 261 | 8 (2 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +21.0) | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -20.0) |
| [[MIA PaCa-2 (line)]] | alt | 305 | 9 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +19.5) | [[Panobinostat (drug)]] 5 µM 0.246× (z -22.1) |
| [[NCI-H1792 (line)]] | alt | 190 | 10 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 4.12× (z +19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -15.6) |
| [[SW 900 (line)]] | alt | 286 | 8 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +20.3) | [[Panobinostat (drug)]] 5 µM 0.316× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 274 | 8 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +18.3) | [[Panobinostat (drug)]] 5 µM 0.319× (z -15.9) |
| [[RKO (line)]] | wt | 284 | 7 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +24.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -20.7) |
| [[C-33 A (line)]] | alt | 263 | 5 (1 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.6) | [[Belinostat (drug)]] 5 µM 0.305× (z -16.9) |
| [[HT-29 (line)]] | alt | 247 | 5 (1 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +23.9) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -18.7) |
| [[NCI-H1573 (line)]] | alt | 135 | 8 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +19.3) | [[Panobinostat (drug)]] 5 µM 0.296× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 186 | 7 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +25.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 249 | 6 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +18.5) | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -19.7) |
| [[SNU-1 (line)]] | wt | 292 | 6 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.338× (z -13.7) |
| [[SNU-423 (line)]] | alt | 188 | 6 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +26.2) | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 234 | 6 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +22.6) | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -18.2) |
| [[A498 (line)]] | wt | 199 | 4 | 5 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +27.9) | [[Panobinostat (drug)]] 5 µM 0.387× (z -15.8) |
| [[BT-474 (line)]] | alt | 165 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -15.0) |
| [[C32 (line)]] | wt | 283 | 2 | 7 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -17.4) |
| [[H4 (line)]] | wt | 185 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.290× (z -12.9) |
| [[HCT15 (line)]] | alt | 279 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +21.9) | [[Belinostat (drug)]] 5 µM 0.331× (z -15.9) |
| [[HOP62 (line)]] | alt | 86.8 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -11.2) |
| [[J82 (line)]] | alt | 250 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +22.6) | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 288 | 4 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.279× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 221 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +21.2) | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -14.3) |
| [[SW1417 (line)]] | alt | 215 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.9) | [[Panobinostat (drug)]] 5 µM 0.360× (z -15.0) |
| [[SW48 (line)]] | wt | 305 | 4 | 5 | [[TAK-901 (drug)]] 0.05 µM 3.37× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.182× (z -20.5) |
| [[AsPC-1 (line)]] | alt | 225 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +26.1) | [[Panobinostat (drug)]] 5 µM 0.264× (z -17.7) |
| [[Hs 766T (line)]] | wt | 165 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +20.2) | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -13.0) |
| [[HS-578T (line)]] | alt | 215 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +23.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 147 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -11.4) |
| [[SHP-77 (line)]] | alt | 237 | 3 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.258× (z -20.6) |
| [[SK-MEL-2 (line)]] | alt | 200 | 3 | 5 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +22.0) | [[Panobinostat (drug)]] 5 µM 0.428× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 187 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -19.3) |
| [[CHP-212 (line)]] | wt | 244 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.273× (z -11.7) |
| [[A-172 (line)]] | wt | 160 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +25.7) | — |
| [[SW 1271 (line)]] | alt | 480 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.325× (z -9.2) |
| [[AN3 CA (line)]] | alt | 382 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.9) |
| [[NCI-H2122 (line)]] | alt | 239 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0657× (z -9.1) ⚠ transcription drop |
| [[NCI-H596 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 223 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF4B]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 | STRING 593 |
| [[SCAF8]] | +0.69 | +0.57 / +0.64 | both halves | 9e-06 | same gene group |
| [[NFYC]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SLTM]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 | same gene group; STRING 413 |
| [[SRSF11]] ⚠ | +0.66 | +0.71 / +0.56 | both halves | 1e-05 | same gene group; STRING 933; ⚠ in the vector space only through flagged drug-doses |
| [[ZNF280D]] | +0.66 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SRSF4]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 | same gene group; STRING 648 |
| [[ZNF428]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[EPC1]] | +0.65 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[LUC7L2]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 | STRING 547 |
| [[DHFR2]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[TXNRD2]] | +0.64 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SENP6]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR1B]] | -0.66 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.63 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[CAP1]] | -0.61 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[MFN1]] | -0.60 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[LRRC8A]] | -0.58 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[PRDX1]] | -0.58 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[PRELID1]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ARPC2]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TPST2]] | -0.56 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RHOC]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[MLF2]] | -0.55 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TRAPPC1]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SREK1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.8, 6.1); signed map (11.8, -35.2). **Vector** length 118, 49.9% of its response variance represented; |z| ≥ 3 in 1,539 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.8 | +20.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.5 | +33.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.8 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.6 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.5 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.9 | +10.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.6 | -0.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +5.0 | -0.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +5.0 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.5 | -8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.5 | -10.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.0 | -0.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -4.7 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -9.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.0 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.7 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +2.4 |

## What is on record

|  |  |
|---|---|
| Name | splicing regulatory glutamic acid and lysine rich protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:66,139,971-66,183,615 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564B176, SRrp86, SRrp508; previously SFRS12 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXA9](https://www.uniprot.org/uniprotkb/Q8WXA9) (Splicing regulatory glutamine/lysine-rich protein 1):

> Participates in the regulation of alternative splicing by modulating the activity of other splice facors. Inhibits the splicing activity of SFRS1, SFRS2 and SFRS6. Augments the splicing activity of SFRS3 (By similarity).

**Summary**, from NCBI Gene [140890](https://www.ncbi.nlm.nih.gov/gene/140890):

> This gene encodes a member of a family of serine/arginine-rich (SR) splicing proteins containing RNA recognition motif (RRM) domains. The encoded protein interacts with other SR proteins to modulate splice site selection. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:17882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17882) · Entrez [140890](https://www.ncbi.nlm.nih.gov/gene/140890) · UniProt [Q8WXA9](https://www.uniprot.org/uniprotkb/Q8WXA9) · Ensembl [ENSG00000153914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153914)

## Data

Gene col 7749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7749); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7749]; `tensor/DDL_lfc|DDL_z.npy` [7749]; `embed/gene_vectors.npy` [7749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7749 or target_col == 7749). Every well: [[SREK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SREK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
