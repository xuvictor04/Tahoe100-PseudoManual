---
symbol: "HACL1"
type: "gene"
col: 5197
ensembl_id: "ENSG00000131373"
name: "2-hydroxyacyl-CoA lyase 1"
location: "3p25.1"
module: 76
arm: "+"
pooled_cpm: 46.46
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 19
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# HACL1

*2-hydroxyacyl-CoA lyase 1* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.93× (z +19.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.473× (z -13.6, q 3e-39, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.510× (z -6.4, q 3e-08, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFDP2]] (+0.75, fdr 7e-06), [[PLEKHM3]] (+0.71, fdr 1e-05), [[NIPAL3]] (+0.70, fdr 7e-06); moves opposite to [[TUG1]] (-0.58, fdr 2e-05), [[CYREN]] (-0.57, fdr 3e-05), [[ZC3H4]] (-0.57, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.93×** | +19.4 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.72×** | +18.1 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +17.4 | 0e+00 | 39/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +16.4 | 0e+00 | 47/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.12×** | +13.6 | 6e-40 | 46/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +11.7 | 9e-30 | 46/48 (SW480, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.93×** | +11.2 | 3e-27 | 44/48 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +10.7 | 7e-25 | 40/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.8 | 1e-20 | 39/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.65×** | +9.2 | 2e-18 | 36/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +9.1 | 4e-18 | 40/49 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +8.8 | 7e-17 | 41/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.82×** | +7.7 | 4e-13 | 41/48 (LOX-IMVI, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +7.0 | 8e-11 | 32/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +6.7 | 7e-10 | 34/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.7 | 7e-10 | 28/48 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.5 | 2e-09 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.473×** | -13.6 | 3e-39 | 46/48 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.585×** | -9.7 | 8e-20 | 34/47 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -8.7 | 9e-16 | 26/41 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.510×** | -6.4 | 3e-08 | 31/48 (SW480, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.565×** | -5.4 | 7e-06 | 32/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.572×** | -5.3 | 1e-05 | 25/48 (A498, SW 1271, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.588×** | -5.0 | 4e-05 | 24/48 (HEC-1-A, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.614×** | -4.6 | 3e-04 | 23/48 (NCI-H2347, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.777×** | -4.2 | 0.001 | 24/45 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.800×** | -4.1 | 0.003 | 20/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.806×** | -3.9 | 0.004 | 15/48 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.012 | 16/48 (SW480, SW1417, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.824×** | -3.5 | 0.019 | 14/48 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.832×** | -3.3 | 0.033 | 17/48 (SW1417, SW 900, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.878× | -3.3 | 0.033 | 11/48 (SNU-1, SW1417, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.834× | -3.3 | 0.033 | 15/48 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.826×** | -3.3 | 0.033 | 17/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.840× | -3.2 | 0.045 | 12/48 (A498, SW 1088, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.047 | 12/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.5 | 11 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +17.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -11.6) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 43.4 | 10 (3 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.54× (z +13.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 3.29× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.451× (z -8.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 36.6 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.56× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 65.3 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 27.8 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.99× (z +15.5) | — |
| [[LS 180 (line)]] | wt | 31.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 62.1 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 89.3 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -14.1) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 59.1 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 50.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 53.0 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.60× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 39.5 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +16.7) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.45× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 49.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.391× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 17.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.86× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 42.5 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 75.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -12.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 28.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.05× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 26.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.9) | — |
| [[KATO III (line)]] | alt | 31.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 49.5 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.0970× (z -19.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 73.2 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.31× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -9.5) ⚠ unreliable plate only · without an alert: [[Belzutifan (drug)]] 5 µM 0.131× (z -9.0) |
| [[SNU-423 (line)]] | alt | 41.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +12.5) | — |
| [[A-427 (line)]] | wt | 63.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -16.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 50.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.39× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -10.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 58.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 30.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.0) | — |
| [[J82 (line)]] | alt | 65.0 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.46× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.440× (z -8.7) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 40.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 58.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 40.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -8.5) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 19.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 44.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +10.7) | — |
| [[RKO (line)]] | wt | 45.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.349× (z -8.6) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 51.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -13.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 40.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.9) | — |
| [[SW48 (line)]] | wt | 49.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFDP2]] | +0.75 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[PLEKHM3]] | +0.71 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[NIPAL3]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[AUH]] | +0.70 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[COQ8A]] | +0.67 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[MED30]] | +0.66 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ELP2]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[COX14]] | +0.65 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SPSB3]] | +0.65 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[WDR48]] | +0.64 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[CCDC28A]] | +0.64 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[RHEBL1]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | -0.58 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CYREN]] | -0.57 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ZC3H4]] | -0.57 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[ZNF655]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[EIF4G1]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF460]] | -0.55 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[CHMP3]] | -0.54 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[OSTM1]] | -0.54 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[LIG4]] | -0.54 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[ZNF681]] | -0.54 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[TMEM147-AS1]] | -0.54 | -0.46 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.8, -46.6); signed map (-19.2, 8.6). **Vector** length 89.2, 25.2% of its response variance represented; |z| ≥ 3 in 1,360 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +13.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +11.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.9 | -13.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.0 | -6.4 |
|  | [[EX229 (drug)]] 5 µM |  | -6.9 | -5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.8 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.2 | -4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | 2-hydroxyacyl-CoA lyase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,560,699-15,601,852 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 2-HPCL, PHYH2; previously HPCL |
| Gene groups (HGNC) | 2-hydroxyacyl-CoA lyase family |
| Hallmark sets | BILE_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 6 pathways, smallest: Alpha-oxidation of phytanate; Peroxisomal lipid metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ83](https://www.uniprot.org/uniprotkb/Q9UJ83) (2-hydroxyacyl-CoA lyase 1):

> Peroxisomal 2-OH acyl-CoA lyase involved in the cleavage (C1 removal) reaction in the fatty acid alpha-oxydation in a thiamine pyrophosphate (TPP)-dependent manner. Involved in the degradation of 3-methyl-branched fatty acids like phytanic acid and the shortening of 2-hydroxy long-chain fatty acids. Plays a significant role in the biosynthesis of heptadecanal in the liver (By similarity).

**Summary**, from NCBI Gene [26061](https://www.ncbi.nlm.nih.gov/gene/26061):

> Enables several functions, including 2-hydroxyacyl-CoA lyase activity; ATP binding activity; and cation binding activity. Involved in fatty acid alpha-oxidation; phytanic acid metabolic process; and protein targeting to peroxisome. Located in peroxisome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17856) · Entrez [26061](https://www.ncbi.nlm.nih.gov/gene/26061) · UniProt [Q9UJ83](https://www.uniprot.org/uniprotkb/Q9UJ83) · Ensembl [ENSG00000131373](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131373)

## Data

Gene col 5197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5197); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5197]; `tensor/DDL_lfc|DDL_z.npy` [5197]; `embed/gene_vectors.npy` [5197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5197 or target_col == 5197). Every well: [[HACL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HACL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
