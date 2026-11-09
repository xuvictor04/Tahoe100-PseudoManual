---
symbol: "AAMDC"
type: "gene"
col: 1514
ensembl_id: "ENSG00000087884"
name: "adipogenesis associated Mth938 domain containing"
location: "11q14.1"
module: 4
arm: "-"
pooled_cpm: 58.75
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 26
n_dd_up_clean: 15
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# AAMDC

*adipogenesis associated Mth938 domain containing* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +24.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.441× (z -16.0, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.428× (z -8.7, q 1e-15, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSRP1]] (+0.78, fdr 7e-06), [[ARID4A]] (+0.73, fdr 7e-06), [[LMBR1L]] (+0.72, fdr 1e-05); moves opposite to [[NAA15]] (-0.78, fdr 7e-06), [[TMEM33]] (-0.74, fdr 7e-06), [[ATIC]] (-0.72, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLAG1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[AGPS]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +24.6 | 0e+00 | 48/48 (HT-29, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +18.7 | 0e+00 | 46/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +18.0 | 0e+00 | 42/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.17×** | +15.2 | 0e+00 | 44/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +12.1 | 1e-31 | 37/48 (LoVo, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +11.2 | 3e-27 | 42/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +10.2 | 2e-22 | 39/49 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +8.1 | 3e-14 | 39/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +7.2 | 5e-11 | 35/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +6.8 | 8e-10 | 25/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.23×** | +5.7 | 6e-07 | 25/48 (SW480, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.6 | 1e-06 | 26/49 (HT-29, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.69×** | +5.4 | 4e-06 | 32/48 (PANC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.61×** | +4.9 | 4e-05 | 26/48 (Hs 766T, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +4.7 | 8e-05 | 25/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 7e-04 | 23/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.024 | 11/48 (LoVo, A-427, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.441×** | -16.0 | 0e+00 | 47/48 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.428×** | -8.7 | 1e-15 | 41/48 (A549, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.466×** | -7.8 | 1e-12 | 38/48 (A-172, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.472×** | -7.7 | 2e-12 | 39/48 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.669×** | -7.6 | 4e-12 | 23/41 (A549, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -7.1 | 9e-11 | 31/49 (A-172, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.501×** | -7.1 | 1e-10 | 37/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.504×** | -7.0 | 2e-10 | 35/48 (CFPAC-1, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.700×** | -6.4 | 7e-09 | 30/44 (CFPAC-1, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -6.0 | 1e-07 | 30/48 (A-172, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -6.0 | 1e-07 | 28/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.740×** | -5.9 | 2e-07 | 27/48 (SHP-77, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.733×** | -5.9 | 2e-07 | 27/48 (SNU-423, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.742×** | -5.8 | 2e-07 | 26/48 (CFPAC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.746×** | -5.7 | 4e-07 | 32/48 (LOX-IMVI, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.718×** | -5.6 | 8e-07 | 25/48 (A549, A-172, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.761×** | -5.0 | 2e-05 | 29/48 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.713×** | -4.7 | 7e-05 | 23/48 (Hs 766T, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.776×** | -4.6 | 1e-04 | 24/47 (SW48, LOX-IMVI, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 75.4 | 8 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +17.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.397× (z -10.6) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 60.8 | 7 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +18.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.445× (z -10.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.506× (z -8.6) |
| [[PANC-1 (line)]] | alt | 73.9 | 7 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +19.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.467× (z -10.6) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 94.6 | 3 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +13.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.364× (z -11.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.365× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 112 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.268× (z -16.0) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.479× (z -9.0) |
| [[HT-29 (line)]] | alt | 65.0 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +19.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.393× (z -9.5) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 73.0 | 3 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.319× (z -12.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -8.8) |
| [[RKO (line)]] | wt | 33.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +14.1) | — |
| [[J82 (line)]] | alt | 65.6 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[MIA PaCa-2 (line)]] | alt | 62.0 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +17.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -11.4) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 28.0 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +15.3) | — |
| [[A498 (line)]] | wt | 32.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.8) | — |
| [[A549 (line)]] | wt | 62.6 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.67× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.391× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 52.0 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +16.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -12.4) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 30.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +18.6) | — |
| [[Panc 03.27 (line)]] | alt | 76.5 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 101 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.304× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.418× (z -8.7) |
| [[SW 900 (line)]] | alt | 67.9 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[H4 (line)]] | wt | 76.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.326× (z -8.6) |
| [[KATO III (line)]] | alt | 71.7 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 51.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 45.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.4) | — |
| [[A-427 (line)]] | wt | 52.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 60.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +15.6) | — |
| [[HS-578T (line)]] | alt | 71.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.336× (z -10.5) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 55.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.47× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 36.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 59.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HCT15 (line)]] | alt | 87.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.334× (z -8.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HOP62 (line)]] | alt | 56.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 66.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.268× (z -11.6) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 70.6 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 37.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 75.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.435× (z -8.9) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 39.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.216× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SW48 (line)]] | wt | 30.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +10.0) | [[Harringtonine (drug)]] 0.05 µM 0.154× (z -8.5) |
| [[BT-474 (line)]] | alt | 29.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 50.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +9.9) | — |
| [[C32 (line)]] | wt | 39.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 38.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | +0.78 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[LMBR1L]] | +0.72 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[TESK2]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[OGA]] | +0.71 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZFYVE1]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[CERT1]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[NARF]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[HINFP]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MINDY2]] | +0.68 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[PLAG1]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA15]] | -0.78 | -0.75 / -0.76 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.74 | -0.71 / -0.71 | both halves | 7e-06 |  |
| [[ATIC]] | -0.72 | -0.64 / -0.70 | both halves | 7e-06 |  |
| [[RUVBL1]] | -0.70 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[CCT5]] | -0.70 | -0.70 / -0.66 | both halves | 7e-06 |  |
| [[PPIL1]] | -0.69 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[LTV1]] | -0.67 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[FARSB]] | -0.67 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[CLPB]] | -0.67 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[RAD51D]] | -0.66 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.66 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAG1]] | B | PLAG1 activity raises AAMDC's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without PLAG1 | 0.058 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGPS]] | C | AAMDC's natural level weakens AGPS's drug response | AAMDC's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.21; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.801). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.7, -42.5); signed map (-12.5, 8.8). **Vector** length 131, 43.3% of its response variance represented; |z| ≥ 3 in 1,446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +24.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +10.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +11.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +4.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.1 | -16.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.2 | -7.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.8 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -6.0 |
|  | [[EX229 (drug)]] 5 µM |  | -6.8 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.4 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | adipogenesis associated Mth938 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:77,821,109-77,918,432 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTD015, FLJ21035, CK067; previously C11orf67 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7C9](https://www.uniprot.org/uniprotkb/Q9H7C9) (Mth938 domain-containing protein):

> May play a role in preadipocyte differentiation and adipogenesis.

**Summary**, from NCBI Gene [28971](https://www.ncbi.nlm.nih.gov/gene/28971):

> Predicted to be involved in positive regulation of fat cell differentiation. Predicted to act upstream of or within negative regulation of apoptotic process and positive regulation of transcription by RNA polymerase II. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30205) · Entrez [28971](https://www.ncbi.nlm.nih.gov/gene/28971) · UniProt [Q9H7C9](https://www.uniprot.org/uniprotkb/Q9H7C9) · Ensembl [ENSG00000087884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087884)

## Data

Gene col 1514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1514); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1514]; `tensor/DDL_lfc|DDL_z.npy` [1514]; `embed/gene_vectors.npy` [1514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1514 or target_col == 1514). Every well: [[AAMDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AAMDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
