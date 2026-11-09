---
symbol: "TESK2"
type: "gene"
col: 963
ensembl_id: "ENSG00000070759"
name: "testis associated actin remodelling kinase 2"
location: "1p34.1"
module: 4
arm: "-"
pooled_cpm: 44.66
n_lines_expressing: 46
n_dd_up: 22
n_dd_down: 30
n_dd_up_clean: 19
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TESK2

*testis associated actin remodelling kinase 2* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.00× (z +24.5, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.366× (z -15.9, q 0e+00, down in 38 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.468× (z -6.3, q 3e-08, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AAMDC]] (+0.72, fdr 7e-06), [[NARF]] (+0.70, fdr 1e-05), [[RSRP1]] (+0.67, fdr 7e-06); moves opposite to [[FARSB]] (-0.72, fdr 7e-06), [[RRP15]] (-0.70, fdr 1e-05), [[TMEM33]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[SMIM14]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +24.5 | 0e+00 | 42/44 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.31×** | +23.1 | 0e+00 | 43/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.40×** | +19.3 | 0e+00 | 44/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.16×** | +18.2 | 0e+00 | 44/44 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +14.6 | 0e+00 | 37/43 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +10.0 | 1e-21 | 37/44 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.5 | 1e-15 | 32/43 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.4 | 8e-12 | 29/45 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 2e-07 | 26/43 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +5.5 | 2e-06 | 23/44 (BT-474, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +5.3 | 8e-06 | 29/44 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +5.1 | 2e-05 | 28/44 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.85×** | +5.1 | 2e-05 | 26/43 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.7 | 1e-04 | 21/43 (BT-474, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 8e-04 | 20/43 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +4.0 | 0.003 | 18/44 (A-172, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.366×** | -15.9 | 0e+00 | 38/44 (SW480, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -12.9 | 8e-36 | 31/37 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.386×** | -12.3 | 2e-32 | 33/42 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -10.0 | 3e-21 | 31/38 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -6.3 | 3e-08 | 27/45 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.663×** | -6.3 | 3e-08 | 28/44 (PANC-1, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.652×** | -6.2 | 3e-08 | 26/44 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -6.1 | 8e-08 | 26/44 (LS 180, SW480, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.483×** | -6.0 | 1e-07 | 28/44 (SW1417, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.518×** | -5.5 | 3e-06 | 28/44 (SW480, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.576×** | -4.6 | 3e-04 | 22/43 (KATO III, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.581×** | -4.5 | 3e-04 | 24/44 (NCI-H1792, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.585×** | -4.4 | 4e-04 | 22/44 (SW1417, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -4.4 | 4e-04 | 24/43 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.764×** | -4.3 | 7e-04 | 18/44 (NCI-H1573, hTERT-HPNE, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.771×** | -4.1 | 0.001 | 20/44 (hTERT-HPNE, NCI-H1573, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -3.7 | 0.007 | 17/44 (SNU-423, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.798×** | -3.6 | 0.010 | 16/44 (NCI-H1573, SW 1088, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.652×** | -3.5 | 0.012 | 18/42 (SNU-423, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 67.6 | 7 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.33× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.421× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 36.8 | 8 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.54× (z +23.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.371× (z -8.7) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 49.1 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.127× (z -9.8) |
| [[A-172 (line)]] | wt | 19.8 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +21.7) | — |
| [[A498 (line)]] | wt | 39.8 | 5 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +21.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -15.9) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 50.1 | 6 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 66.2 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.32× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0553× (z -17.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.3 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.57× (z +13.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.206× (z -14.5) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 13.6 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.82× (z +21.3) | — |
| [[Panc 03.27 (line)]] | alt | 80.1 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 34.7 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.99× (z +20.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.239× (z -15.0) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 47.2 | 4 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -12.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 73.1 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.34× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -15.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 37.6 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +13.8) | — |
| [[LoVo (line)]] | wt | 89.7 | 3 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -20.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 101 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 46.8 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -12.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 37.8 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 40.1 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.29× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.160× (z -11.5) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 19.7 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +14.3) | — |
| [[AsPC-1 (line)]] | alt | 30.3 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 67.3 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 37.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.77× (z +14.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.199× (z -12.1) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 53.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 59.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +16.7) | — |
| [[SW48 (line)]] | wt | 56.7 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 16.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.39× (z +16.1) | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +22.8) | — |
| [[A-427 (line)]] | wt | 53.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +11.4) | — |
| [[H4 (line)]] | wt | 32.5 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0792× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 59.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -12.1) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 49.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 77.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0646× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 48.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +10.3) | — |
| [[RKO (line)]] | wt | 27.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 57.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +9.6) | — |
| [[C32 (line)]] | wt | 74.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +18.1) | — |
| [[NCI-H1573 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAMDC]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[NARF]] | +0.70 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[RSRP1]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[IFT20]] | +0.66 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[KLHL24]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[PHF1]] | +0.64 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[NDUFA2]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[TULP3]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[RASA4B]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[STX5-DT]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[STX5]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | -0.72 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[RRP15]] | -0.70 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.69 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[FKTN]] | -0.68 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.68 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[MAK16]] | -0.68 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[WDR77]] | -0.68 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[GFM1]] | -0.67 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[PPIL1]] | -0.67 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.67 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[RPE]] | -0.67 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[POLR1A]] | -0.66 | -0.61 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM14]] | C | TESK2 activity raises SMIM14's level | lines that do not express TESK2 (3) vs lines expressing it (46) | 2.72× lower at baseline in the lines without TESK2 | 0.029 | ⚠ few lines (3 vs 46); across organs; also absent: SYNPO2, SLC9A3, SFXN3; maybe low, not absent |
| [[MINDY2]] | C | TESK2 activity lowers MINDY2's level | lines that do not express TESK2 (3) vs lines expressing it (46) | 2.19× higher at baseline in the lines without TESK2 | 0.081 | ⚠ few lines (3 vs 46); across organs; also absent: SYNPO2, SLC9A3, SFXN3; maybe low, not absent |
| [[A2MP1]] | C | TESK2 activity lowers A2MP1's level | lines that do not express TESK2 (3) vs lines expressing it (46) | 1.90× higher at baseline in the lines without TESK2 | 0.092 | ⚠ few lines (3 vs 46); across organs; also absent: SYNPO2, SLC9A3, SFXN3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.9, -36.3); signed map (-15.6, 14.2). **Vector** length 116, 35.8% of its response variance represented; |z| ≥ 3 in 1,313 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +24.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.5 | +0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.5 | -15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.4 | -12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -12.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.9 | -6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.6 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -5.5 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.4 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | testis associated actin remodelling kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,343,883-45,491,163 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LIMK/TESK kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S53](https://www.uniprot.org/uniprotkb/Q96S53) (Dual specificity testis-specific protein kinase 2):

> Dual specificity protein kinase activity catalyzing autophosphorylation and phosphorylation of exogenous substrates on both serine/threonine and tyrosine residues. Phosphorylates cofilin at 'Ser-3'. May play an important role in spermatogenesis.

**Summary**, from NCBI Gene [10420](https://www.ncbi.nlm.nih.gov/gene/10420):

> This gene product is a serine/threonine protein kinase that contains an N-terminal protein kinase domain that is structurally similar to the kinase domains of testis-specific protein kinase-1 and the LIM motif-containing protein kinases (LIMKs). Its overall structure is most related to the former, indicating that it belongs to the TESK subgroup of the LIMK/TESK family of protein kinases. This gene is predominantly expressed in testis and prostate. The developmental expression pattern of the rat …

**Accessions** — [HGNC:11732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11732) · Entrez [10420](https://www.ncbi.nlm.nih.gov/gene/10420) · UniProt [Q96S53](https://www.uniprot.org/uniprotkb/Q96S53) · Ensembl [ENSG00000070759](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070759)

## Data

Gene col 963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 963); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 963]; `tensor/DDL_lfc|DDL_z.npy` [963]; `embed/gene_vectors.npy` [963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 963 or target_col == 963). Every well: [[TESK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TESK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
