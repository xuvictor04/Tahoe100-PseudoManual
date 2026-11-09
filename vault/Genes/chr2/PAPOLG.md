---
symbol: "PAPOLG"
type: "gene"
col: 3673
ensembl_id: "ENSG00000115421"
name: "poly(A) polymerase gamma"
location: "2p16.1"
module: 187
arm: "+"
pooled_cpm: 50.99
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 21
n_dd_up_clean: 17
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# PAPOLG

*poly(A) polymerase gamma* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +13.5, q 1e-38, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.347× (z -16.5, q 0e+00, down in 39 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.767× (z -4.3, q 0.002, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf87]] (+0.66, fdr 7e-06), [[CLPX]] (+0.65, fdr 1e-05), [[CDC37L1]] (+0.64, fdr 5e-05); moves opposite to [[LINC00641]] (-0.57, fdr 1e-05), [[ETF1]] (-0.56, fdr 6e-05), [[SFPQ]] (-0.53, fdr 2e-05).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02666]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +13.5 | 1e-38 | 45/48 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +11.4 | 1e-27 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +10.6 | 7e-24 | 33/48 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +10.5 | 9e-24 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.08×** | +9.6 | 1e-19 | 42/49 (SW480, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +8.3 | 1e-14 | 41/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +8.2 | 2e-14 | 44/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.58×** | +8.1 | 5e-14 | 36/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.1 | 8e-11 | 31/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 5e-09 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +6.0 | 1e-07 | 32/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.2 | 1e-05 | 29/47 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +4.7 | 1e-04 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +4.6 | 2e-04 | 26/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 2e-04 | 24/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 9e-04 | 26/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -16.5 | 0e+00 | 39/42 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.385×** | -15.5 | 0e+00 | 45/49 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.512×** | -10.1 | 2e-21 | 36/45 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.741×** | -4.9 | 2e-04 | 28/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.767×** | -4.3 | 0.002 | 23/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.016 | 27/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.798×** | -3.7 | 0.020 | 19/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.023 | 18/48 (Panc 03.27, A-172, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.804×** | -3.5 | 0.024 | 18/47 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.805×** | -3.5 | 0.024 | 21/48 (NCI-H2030, RKO, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.043 | 16/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.680×** | -3.3 | 0.050 | 15/48 (NCI-H2347, AN3 CA, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.869× | -3.2 | 0.056 | 14/48 (SK-MEL-2, AN3 CA, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.821×** | -3.2 | 0.056 | 16/49 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.830×** | -3.0 | 0.081 | 12/48 (NCI-H2030, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.830×** | -3.0 | 0.081 | 13/48 (hTERT-HPNE, A-427, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.831×** | -3.0 | 0.081 | 16/49 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.831×** | -3.0 | 0.081 | 18/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.703×** | -3.0 | 0.081 | 17/48 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 56.7 | 9 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.4 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 131 | 3 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.86× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 77.2 | 4 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.20× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 46.6 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -10.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 34.2 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 57.7 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -14.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 55.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -15.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 46.5 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.66× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -16.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 36.8 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -12.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 37.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 53.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -18.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 57.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -10.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 39.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 89.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 54.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 49.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 48.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -15.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 31.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 53.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.25× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 80.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -19.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 44.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -15.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 42.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 73.6 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.34× (z +8.6) | — |
| [[C32 (line)]] | wt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 55.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0883× (z -11.0) |
| [[H4 (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -14.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 33.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 74.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -13.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 51.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -11.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 55.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0701× (z -18.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf87]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CLPX]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CDC37L1]] | +0.64 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[DYNC1LI1]] | +0.63 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[FHIP2A]] | +0.63 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[TAPT1]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[UBA3]] | +0.62 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[EAPP]] | +0.62 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[PIK3CA]] | +0.61 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[MBIP]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[FBXL15]] | +0.61 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[RWDD3]] | +0.61 | +0.68 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00641]] | -0.57 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ETF1]] | -0.56 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[SFPQ]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02666]] | B | LINC02666 activity lowers PAPOLG's level | lines that do not express LINC02666 (14) vs lines expressing it (36) | 1.20× higher at baseline in the lines without LINC02666 | 0.063 | ⚠ within organs, on part of the lines; also absent: MGMT |
| [[TOP2A]] | B | TOP2A activity lowers PAPOLG's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC16A14]] | B | SLC16A14 activity lowers PAPOLG's level | lines that do not express SLC16A14 (16) vs lines expressing it (34) | 1.06× higher at baseline in the lines without SLC16A14 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, ARHGEF16, NEBL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.8, -7.7); signed map (-22.7, -8.1). **Vector** length 81.5, 22.1% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.5 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) polymerase gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:60,756,253-60,802,086 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12972 |
| Reactome | 5 pathways, smallest: Nuclear RNA decay; mRNA Polyadenylation; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWT3](https://www.uniprot.org/uniprotkb/Q9BWT3) (Poly(A) polymerase gamma):

> Responsible for the post-transcriptional adenylation of the 3'-terminal of mRNA precursors and several small RNAs including signal recognition particle (SRP) RNA, nuclear 7SK RNA, U2 small nuclear RNA, and ribosomal 5S RNA.

**Summary**, from NCBI Gene [64895](https://www.ncbi.nlm.nih.gov/gene/64895):

> This gene encodes a member of the poly(A) polymerase family which catalyzes template-independent extension of the 3' end of a DNA/RNA strand. This enzyme shares 60% identity to the well characterized poly(A) polymerase II (PAPII) at the amino acid level. These two enzymes have similar organization of structural and functional domains. This enzyme is exclusively localized in the nucleus and exhibits both nonspecific and CPSF (cleavage and polyadenylation specificity factor)/AAUAAA-dependent …

**Accessions** — [HGNC:14982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14982) · Entrez [64895](https://www.ncbi.nlm.nih.gov/gene/64895) · UniProt [Q9BWT3](https://www.uniprot.org/uniprotkb/Q9BWT3) · Ensembl [ENSG00000115421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115421)

## Data

Gene col 3673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3673); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3673]; `tensor/DDL_lfc|DDL_z.npy` [3673]; `embed/gene_vectors.npy` [3673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3673 or target_col == 3673). Every well: [[PAPOLG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAPOLG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
