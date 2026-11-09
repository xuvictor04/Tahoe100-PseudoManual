---
symbol: "SSBP2"
type: "gene"
col: 7012
ensembl_id: "ENSG00000145687"
name: "single stranded DNA binding protein 2"
location: "5q14.1"
module: 106
arm: "+"
pooled_cpm: 163.26
n_lines_expressing: 46
n_dd_up: 25
n_dd_down: 31
n_dd_up_clean: 24
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# SSBP2

*single stranded DNA binding protein 2* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.87× (z +10.4, q 2e-22, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.292× (z -19.6, q 0e+00, down in 38 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.457× (z -12.9, q 3e-36, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC22D3]] (+0.67, fdr 7e-06), [[UGP2]] (+0.63, fdr 7e-06), [[HERC3]] (+0.63, fdr 7e-06); moves opposite to [[ITGB1-DT]] (-0.57, fdr 1e-05), [[GPR39]] (-0.56, fdr 1e-05), [[TBILA]] (-0.54, fdr 2e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LOX]] → it (grade B ⚠); 8 go from it, the strongest it → [[CST3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 2 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +10.4 | 2e-22 | 40/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +8.7 | 6e-16 | 38/44 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +6.3 | 5e-08 | 31/44 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.46×** | +6.2 | 6e-08 | 27/44 (hTERT-HPNE, H4, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.43×** | +6.0 | 3e-07 | 29/44 (hTERT-HPNE, H4, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.42×** | +5.6 | 2e-06 | 27/45 (hTERT-HPNE, H4, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +5.0 | 4e-05 | 30/45 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.33×** | +4.7 | 2e-04 | 29/46 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **1.33×** | +4.7 | 2e-04 | 24/44 (hTERT-HPNE, H4, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.32×** | +4.6 | 3e-04 | 25/44 (hTERT-HPNE, H4, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 1e-03 | 30/46 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 1e-03 | 24/44 (hTERT-HPNE, H4, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 1e-03 | 24/43 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 27/44 (hTERT-HPNE, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.002 | 22/44 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.292×** | -19.6 | 0e+00 | 38/41 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.319×** | -18.9 | 0e+00 | 43/45 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.393×** | -14.3 | 5e-44 | 38/42 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.436×** | -13.2 | 1e-37 | 40/43 (NCI-H460, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.457×** | -12.9 | 3e-36 | 40/44 (NCI-H460, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.599×** | -8.5 | 2e-15 | 41/44 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.624×** | -7.8 | 5e-13 | 34/44 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.736×** | -7.0 | 2e-10 | 29/44 (C32, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.653×** | -6.7 | 2e-09 | 33/44 (NCI-H460, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -6.0 | 1e-07 | 29/44 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.726×** | -5.3 | 6e-06 | 27/44 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.747×** | -4.6 | 2e-04 | 32/44 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.595×** | -4.5 | 3e-04 | 30/44 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.770×** | -4.3 | 6e-04 | 25/43 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.775×** | -4.0 | 0.002 | 29/43 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.785×** | -4.0 | 0.002 | 25/44 (A-172, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.641×** | -3.8 | 0.004 | 27/44 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.790×** | -3.6 | 0.009 | 23/44 (NCI-H460, C32, …) | all doses, flat |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.854× | -3.6 | 0.010 | 13/45 (A-427, HEC-1-A, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.739×** | -3.5 | 0.011 | 20/44 (SW 900, C-33 A, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.813×** | -3.4 | 0.014 | 23/44 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 172 | 14 | 4 (3 ⚠) | [[Budesonide (drug)]] 5 µM 3.86× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.393× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 184 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -14.1) |
| [[C32 (line)]] | wt | 335 | 1 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.16× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0673× (z -29.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.424× (z -13.6) |
| [[HT-29 (line)]] | alt | 124 | 4 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.51× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.252× (z -14.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -10.5) |
| [[LS 180 (line)]] | wt | 84.6 | 6 (1 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.55× (z +14.0) | [[Ixazomib citrate (drug)]] 5 µM 0.361× (z -9.4) |
| [[SNU-423 (line)]] | alt | 241 | 1 | 9 (5 ⚠) | [[Budesonide (drug)]] 5 µM 2.14× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -13.6) |
| [[LoVo (line)]] | wt | 66.5 | 9 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +27.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.44× (z +21.0) | — |
| [[A-172 (line)]] | wt | 233 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -10.8) |
| [[H4 (line)]] | wt | 213 | 5 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +18.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 5 µM 2.72× (z +9.2) | [[Auranofin (drug)]] 5 µM 0.256× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 323 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -14.4) |
| [[RKO (line)]] | wt | 104 | 4 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.59× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 68.3 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +13.8) | [[Auranofin (drug)]] 5 µM 0.447× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 261 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 291 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.378× (z -9.4) |
| [[SW 900 (line)]] | alt | 291 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.247× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.356× (z -10.8) |
| [[SW480 (line)]] | alt | 132 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.24× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -16.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 48.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.36× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -13.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 266 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0603× (z -30.9) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.385× (z -11.0) |
| [[HOP62 (line)]] | alt | 203 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -10.1) |
| [[Hs 766T (line)]] | wt | 190 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -11.5) |
| [[HS-578T (line)]] | alt | 176 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -9.3) |
| [[SNU-1 (line)]] | wt | 1,067 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.320× (z -11.4) |
| [[A549 (line)]] | wt | 146 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.558× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 183 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 102 | 2 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.83× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -13.7) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.468× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 99.6 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 77.2 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +15.4) | [[Auranofin (drug)]] 5 µM 0.468× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 223 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.296× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 164 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -9.6) |
| [[AN3 CA (line)]] | alt | 604 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0815× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.240× (z -10.8) |
| [[J82 (line)]] | alt | 144 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -9.9) |
| [[C-33 A (line)]] | alt | 224 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 299 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -18.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -16.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 52.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.02× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 60.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -9.9) |
| [[SHP-77 (line)]] | alt | 325 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.85× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~20% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -14.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 87.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.397× (z -9.2) |
| [[SW48 (line)]] | wt | 55.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.08× (z +9.3) | — |
| [[A498 (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 80.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 349 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -9.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 30.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[UGP2]] | +0.63 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[HERC3]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PACSIN2]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PXK]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[KLF9]] | +0.61 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ESYT2]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TBC1D12]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[EFNA3]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LIX1L]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PHF21A]] | +0.60 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[AGTPBP1]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1-DT]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[GPR39]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TBILA]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ZNF195]] | -0.52 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[BICD1]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[RABGEF1P3]] | -0.51 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[NAV3]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ANXA10]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[LINC01589]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[KIAA1549]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[REXO1]] | -0.50 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[CSTF3]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOX]] | B | LOX activity raises SSBP2's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.73× lower at baseline in the lines without LOX | 0.037 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[RIPOR2]] | B | RIPOR2 activity raises SSBP2's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 2.20× lower at baseline in the lines without RIPOR2 | 0.038 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[PRDX2]] | B | PRDX2 activity raises SSBP2's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.08× lower at baseline in the lines without PRDX2 | 0.058 | ⚠ within organs, on part of the lines; also absent: RAB20 |
| [[NR3C1]] | B | NR3C1 activity raises SSBP2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[DEPP1]] | B | DEPP1 activity raises SSBP2's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.55× lower at baseline in the lines without DEPP1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SSBP2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CST3]] | C | SSBP2 activity lowers CST3's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 2.85× higher at baseline in the lines without SSBP2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent; its own permutation p |
| [[BICD1]] | C | SSBP2 activity raises BICD1's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without SSBP2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent; its own permutation p |
| [[TFEB]] | C | SSBP2 activity lowers TFEB's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 2.32× higher at baseline in the lines without SSBP2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent; its own permutation p |
| [[ZNF83]] | C | SSBP2 activity raises ZNF83's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 4.85× lower at baseline in the lines without SSBP2 | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent |
| [[JAK1]] | C | SSBP2 activity lowers JAK1's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 1.36× higher at baseline in the lines without SSBP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent; its own permutation p |
| [[BCKDHB]] | C | SSBP2 activity raises BCKDHB's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without SSBP2 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | SSBP2's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | SSBP2's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.446 over the table, 0.049 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | SSBP2's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | SSBP2's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, 11.1); signed map (-28.6, 24.5). **Vector** length 140, 50.3% of its response variance represented; |z| ≥ 3 in 1,781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Betamethasone dipropionate (drug)]] 5 µM |  | +6.6 | +5.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +6.5 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +8.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +5.7 | +4.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +5.6 | +4.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +5.1 | +3.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.7 | -13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.3 | -12.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.9 | -7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.6 | -8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.1 | -6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.2 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | +0.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | single stranded DNA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:81,412,804-81,751,797 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC116 |
| Gene groups (HGNC) | Wnt enhanceosome complex |
| Matched by | ensembl_id |

UniProt [P81877](https://www.uniprot.org/uniprotkb/P81877) carries no function annotation.

**Summary**, from NCBI Gene [23635](https://www.ncbi.nlm.nih.gov/gene/23635):

> This gene encodes a subunit of a protein complex that interacts with single-stranded DNA and is involved in the DNA damage response and maintenance of genome stability. The encoded protein may also play a role in telomere repair. A variant of this gene may be associated with survival in human glioblastoma patients. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:15831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15831) · Entrez [23635](https://www.ncbi.nlm.nih.gov/gene/23635) · UniProt [P81877](https://www.uniprot.org/uniprotkb/P81877) · Ensembl [ENSG00000145687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145687)

## Data

Gene col 7012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7012); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7012]; `tensor/DDL_lfc|DDL_z.npy` [7012]; `embed/gene_vectors.npy` [7012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7012 or target_col == 7012). Every well: [[SSBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
