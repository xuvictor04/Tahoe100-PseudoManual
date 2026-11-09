---
symbol: "WIPI2"
type: "gene"
col: 8118
ensembl_id: "ENSG00000157954"
name: "WD repeat domain, phosphoinositide interacting 2"
location: "7p22.1"
module: 76
arm: "+"
pooled_cpm: 62.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 24
n_dd_up_clean: 13
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# WIPI2

*WD repeat domain, phosphoinositide interacting 2* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +17.1, q 0e+00, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.323× (z -24.8, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.550× (z -18.5, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC3]] (+0.80, fdr 7e-06), [[SPSB3]] (+0.77, fdr 7e-06), [[FBXL20]] (+0.74, fdr 1e-05); moves opposite to [[YTHDC2]] (-0.56, fdr 1e-05), [[RAD50]] (-0.54, fdr 2e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +17.1 | 0e+00 | 39/49 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +8.5 | 7e-15 | 37/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +8.2 | 4e-14 | 38/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +7.6 | 4e-12 | 35/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +7.6 | 4e-12 | 37/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +6.8 | 1e-09 | 35/48 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +6.7 | 2e-09 | 31/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 8e-07 | 31/48 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +5.2 | 1e-05 | 29/48 (HOP62, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.2 | 1e-05 | 25/48 (LOX-IMVI, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.005 | 9/49 (CFPAC-1, A549, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.018 | 16/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.030 | 12/49 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +3.3 | 0.034 | 10/47 (H4, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.036 | 20/49 (SHP-77, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.051 | 11/49 (HOP62, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.323×** | -24.8 | 0e+00 | 48/48 (SW48, KATO III, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.550×** | -18.5 | 0e+00 | 42/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.444×** | -17.1 | 0e+00 | 44/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -14.8 | 0e+00 | 45/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.318×** | -13.1 | 2e-37 | 47/48 (AsPC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.343×** | -12.3 | 1e-32 | 45/48 (AsPC-1, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.349×** | -12.1 | 1e-31 | 45/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.379×** | -11.1 | 7e-27 | 46/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.393×** | -10.7 | 6e-25 | 43/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.618×** | -10.6 | 3e-24 | 46/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.639×** | -9.4 | 2e-19 | 30/42 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.586×** | -8.4 | 3e-15 | 39/48 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.678×** | -8.0 | 4e-14 | 35/48 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.627×** | -7.3 | 1e-11 | 39/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.587×** | -6.1 | 4e-08 | 28/47 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.685×** | -5.9 | 1e-07 | 34/48 (KATO III, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -5.9 | 1e-07 | 24/48 (A-172, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 97.0 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.5) |
| [[SW480 (line)]] | alt | 59.4 | 4 | 8 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +13.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -19.9) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.260× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 95.3 | 1 | 8 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -19.0) |
| [[NCI-H2347 (line)]] | alt | 65.1 | 0 | 8 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.207× (z -20.3) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.198× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 50.6 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +13.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -15.3) |
| [[PANC-1 (line)]] | alt | 58.6 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -20.2) |
| [[A-172 (line)]] | wt | 69.3 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -27.6) |
| [[H4 (line)]] | wt | 96.3 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 82.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -22.1) |
| [[A498 (line)]] | wt | 105 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.322× (z -14.7) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.400× (z -11.4) |
| [[KATO III (line)]] | alt | 73.9 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.123× (z -21.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.160× (z -9.7) |
| [[LoVo (line)]] | wt | 63.6 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +14.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.206× (z -17.9) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.131× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 81.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.7) |
| [[A-427 (line)]] | wt | 61.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -18.6) |
| [[HEC-1-A (line)]] | alt | 39.9 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -16.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.219× (z -8.6) |
| [[SW 900 (line)]] | alt | 69.9 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.317× (z -10.6) |
| [[SW1417 (line)]] | alt | 69.0 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -15.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.117× (z -11.9) |
| [[HOP62 (line)]] | alt | 47.9 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -13.0) |
| [[HS-578T (line)]] | alt | 50.0 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.344× (z -9.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -9.2) |
| [[HT-29 (line)]] | alt | 64.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.245× (z -14.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 64.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.379× (z -9.0) |
| [[SW48 (line)]] | wt | 80.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0628× (z -22.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.330× (z -8.5) |
| [[A549 (line)]] | wt | 52.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -12.3) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 63.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.385× (z -9.0) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 43.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.5) | [[Lonafarnib (drug)]] 5 µM 0.143× (z -8.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 58.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.352× (z -8.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 51.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 47.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.324× (z -11.5) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 63.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.7) |
| [[RKO (line)]] | wt | 70.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -10.6) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 64.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 83.7 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -13.4) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 52.1 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.194× (z -11.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.2) |
| [[SNU-423 (line)]] | alt | 65.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -20.5) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -19.0) |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -9.3) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 1 | — | [[TAK-733 (drug)]] 5 µM 0.0264× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.3) |
| [[LS 180 (line)]] | wt | 45.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 96.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.331× (z -11.9) ⚠ unreliable plate only |
| [[NCI-H596 (line)]] | alt | 56.5 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.176× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC3]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.77 | +0.68 / +0.85 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.74 | +0.53 / +0.81 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.73 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[MXD4]] | +0.73 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[SAP30L]] | +0.72 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[CRIPT]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[HAGH]] | +0.70 | +0.41 / +0.75 | both halves | 4e-05 |  |
| [[ADIPOR1]] | +0.69 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[MOB2]] | +0.69 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[RETREG3]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDC2]] | -0.56 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[RAD50]] | -0.54 | -0.60 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.7, -44.3); signed map (-19.6, 10.7). **Vector** length 145, 46.4% of its response variance represented; |z| ≥ 3 in 1,337 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +17.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.5 | +7.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.9 | -24.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.7 | -17.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.4 | -12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -11.3 | -18.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.2 | -14.8 |
|  | [[EX229 (drug)]] 5 µM |  | -10.8 | -11.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -10.2 | -13.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.0 | -10.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -9.9 | -12.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain, phosphoinositide interacting 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,190,196-5,233,840 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATG21, CGI-50, FLJ12979, FLJ14217, FLJ42984, DKFZP434J154, DKFZp686P02188, ATG18B |
| Gene groups (HGNC) | WD repeat domain containing; Autophagy related; WIPI family |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4P8](https://www.uniprot.org/uniprotkb/Q9Y4P8) (WD repeat domain phosphoinositide-interacting protein 2):

> Component of the autophagy machinery that controls the major intracellular degradation process by which cytoplasmic materials are packaged into autophagosomes and delivered to lysosomes for degradation. Involved in an early step of the formation of preautophagosomal structures. Binds and is activated by phosphatidylinositol 3-phosphate (PtdIns3P) forming on membranes of the endoplasmic reticulum upon activation of the upstream ULK1 and PI3 kinases. Mediates ER-isolation membranes contacts by …

**Summary**, from NCBI Gene [26100](https://www.ncbi.nlm.nih.gov/gene/26100):

> WD40 repeat proteins are key components of many essential biologic functions. They regulate the assembly of multiprotein complexes by presenting a beta-propeller platform for simultaneous and reversible protein-protein interactions. Members of the WIPI subfamily of WD40 repeat proteins, such as WIPI2, have a 7-bladed propeller structure and contain a conserved motif for interaction with phospholipids (Proikas-Cezanne et al., 2004 [PubMed 15602573]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:32225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32225) · Entrez [26100](https://www.ncbi.nlm.nih.gov/gene/26100) · UniProt [Q9Y4P8](https://www.uniprot.org/uniprotkb/Q9Y4P8) · Ensembl [ENSG00000157954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157954)

## Data

Gene col 8118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8118); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8118]; `tensor/DDL_lfc|DDL_z.npy` [8118]; `embed/gene_vectors.npy` [8118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8118 or target_col == 8118). Every well: [[WIPI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WIPI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
