---
symbol: "IDH1"
type: "gene"
col: 6172
ensembl_id: "ENSG00000138413"
name: "isocitrate dehydrogenase (NADP(+)) 1"
location: "2q34"
module: 63
arm: "+"
pooled_cpm: 32.7
n_lines_expressing: 50
n_dd_up: 71
n_dd_down: 22
n_dd_up_clean: 59
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# IDH1

*isocitrate dehydrogenase (NADP(+)) 1* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 71 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.94× (z +15.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.332× (z -15.5, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHGDH]] (+0.74, fdr 7e-06), [[TCEA1]] (+0.73, fdr 7e-06), [[PSAT1]] (+0.73, fdr 7e-06); moves opposite to [[ZNF347]] (-0.57, fdr 3e-05), [[PPP1R1C]] (-0.53, fdr 2e-05), [[EGFR]] (-0.52, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 77 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 71 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.94×** | +15.2 | 0e+00 | 48/48 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.92×** | +15.1 | 0e+00 | 47/48 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +14.9 | 0e+00 | 42/47 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +14.3 | 5e-44 | 36/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.70×** | +14.0 | 3e-42 | 44/48 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +12.5 | 4e-34 | 43/48 (A549, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +12.2 | 3e-32 | 28/36 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.08×** | +10.3 | 6e-23 | 33/47 (LoVo, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.13×** | +10.0 | 7e-22 | 37/48 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +9.0 | 2e-17 | 44/48 (SW1417, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +7.8 | 2e-13 | 24/39 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.47×** | +7.7 | 9e-13 | 35/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **1.46×** | +7.5 | 3e-12 | 33/48 (SNU-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +7.3 | 1e-11 | 30/48 (LoVo, COLO 205, …) | two highest doses |  |
| [[Berbamine (drug)]] 5 µM |  | **1.42×** | +7.0 | 9e-11 | 37/49 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +6.3 | 8e-09 | 33/47 (A549, SW480, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +6.0 | 5e-08 | 29/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.55×** | +6.0 | 7e-08 | 32/48 (SW480, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.332×** | -15.5 | 0e+00 | 40/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.494×** | -14.0 | 2e-42 | 38/47 (HT-29, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.409×** | -12.6 | 5e-34 | 43/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.415×** | -12.4 | 5e-33 | 44/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.431×** | -11.8 | 3e-30 | 43/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.469×** | -10.7 | 2e-24 | 39/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.466×** | -10.3 | 4e-23 | 37/48 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.483×** | -10.2 | 9e-23 | 37/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.495×** | -9.9 | 2e-21 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.604×** | -7.1 | 7e-11 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.597×** | -6.7 | 1e-09 | 29/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.765×** | -3.8 | 0.007 | 23/47 (MIA PaCa-2, HCT15, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.011 | 10/48 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.013 | 12/47 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.791×** | -3.3 | 0.035 | 17/48 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.621×** | -3.3 | 0.036 | 19/48 (LS 180, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.036 | 17/48 (A-172, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.855× | -3.1 | 0.052 | 15/48 (PANC-1, HCT15, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.802×** | -3.1 | 0.052 | 16/46 (HCT15, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.2 | 2 | 11 (4 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.04× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -20.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -20.0) |
| [[A-427 (line)]] | wt | 48.5 | 1 | 9 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.66× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -13.0) |
| [[KATO III (line)]] | alt | 104 | 1 | 9 (3 ⚠) | [[Artesunate (drug)]] 5 µM 2.02× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -21.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -17.4) |
| [[LoVo (line)]] | wt | 35.6 | 2 | 8 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.49× (z +11.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.259× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 52.3 | 6 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.92× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.14× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -17.0) |
| [[SW480 (line)]] | alt | 27.1 | 3 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +13.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -13.1) |
| [[HT-29 (line)]] | alt | 61.1 | 1 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -22.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -14.5) |
| [[J82 (line)]] | alt | 27.0 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 5.08× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 4 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.79× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -10.6) |
| [[A549 (line)]] | wt | 20.5 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.60× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.13× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 30.2 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.76× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 39.0 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 28.0 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.80× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -8.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -8.5) |
| [[SW1417 (line)]] | alt | 46.8 | 4 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +11.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -9.1) |
| [[A-172 (line)]] | wt | 23.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.71× (z +9.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.215× (z -10.0) |
| [[A498 (line)]] | wt | 40.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.13× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 93.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 36.2 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0675× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 15.8 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 5.00× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -9.8) |
| [[SNU-1 (line)]] | wt | 27.2 | 2 | 1 | [[Artesunate (drug)]] 5 µM 5.27× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -8.6) |
| [[H4 (line)]] | wt | 35.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0924× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 24.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.27× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -8.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 12.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.05× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -9.1) |
| [[RKO (line)]] | wt | 24.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -15.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.172× (z -9.7) |
| [[BT-474 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 42.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -9.1) |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H23 (line)]] | alt | 20.6 | 1 | 0 | [[Ponatinib (drug)]] 5 µM 5.63× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 25.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.66× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -8.6) |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -9.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 58.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -10.0) |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHGDH]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 555 |
| [[TCEA1]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PSAT1]] | +0.73 | +0.67 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 422 |
| [[XPOT]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[RTN3]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[EPRS1]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[CTH]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 405 |
| [[MTHFD2]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 543 |
| [[AARS1]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[GHITM]] | +0.67 | +0.73 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[CLGN]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[GARS1]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF347]] | -0.57 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PPP1R1C]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[EGFR]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 795 |
| [[ZNF75A]] | -0.51 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIR]] | B | PIR activity raises IDH1's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.50× lower at baseline in the lines without PIR | 0.054 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[DKK1]] | B | DKK1 activity raises IDH1's level | lines that do not express DKK1 (20) vs lines expressing it (30) | 1.18× lower at baseline in the lines without DKK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CACNG4, PALM, CRIP1 |
| [[LINC00662]] | C | LINC00662 activity lowers IDH1's level | lines that do not express LINC00662 (3) vs lines expressing it (47) | 2.18× higher at baseline in the lines without LINC00662 | 0.024 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |
| [[GPD1L]] | C | GPD1L activity raises IDH1's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without GPD1L | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[KIFC3]] | C | KIFC3 activity lowers IDH1's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 1.47× higher at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.2, 47.0); signed map (-14.7, 23.9). **Vector** length 135, 47.7% of its response variance represented; |z| ≥ 3 in 1,774 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.59 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.61 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.61 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.5 | +10.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +8.5 | +14.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +7.7 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +7.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.0 | +6.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.5 | +5.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +5.3 | +5.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +5.3 | +5.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.2 | -15.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -9.6 | -14.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.9 | -9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -10.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.5 | -10.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.6 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -0.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.1 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | isocitrate dehydrogenase (NADP(+)) 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:208,236,229-208,266,074 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Isocitrate dehydrogenases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, GLYCOLYSIS, ADIPOGENESIS, MTORC1_SIGNALING, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 13 pathways, smallest: NFE2L2 regulating TCA cycle genes; Metabolism of cofactors; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O75874](https://www.uniprot.org/uniprotkb/O75874) (Isocitrate dehydrogenase):

> Catalyzes the NADP(+)-dependent oxidative decarboxylation of isocitrate (D-threo-isocitrate) to 2-ketoglutarate (2-oxoglutarate), which is required by other enzymes such as the phytanoyl-CoA dioxygenase. Can also use 2-oxoglutarate as substrate and catalyze the reduction of 2-oxoglutarate to R-2-hydroxyglutarate. Plays a critical role in the generation of NADPH, an important cofactor in many biosynthesis pathways. May act as a corneal epithelial crystallin and may be involved in maintaining …

**Summary**, from NCBI Gene [3417](https://www.ncbi.nlm.nih.gov/gene/3417):

> Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isocitrate dehydrogenases, one of which is mitochondrial and the other predominantly cytosolic. Each …

**Accessions** — [HGNC:5382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5382) · Entrez [3417](https://www.ncbi.nlm.nih.gov/gene/3417) · UniProt [O75874](https://www.uniprot.org/uniprotkb/O75874) · Ensembl [ENSG00000138413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138413)

## Data

Gene col 6172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6172); `tables/drug_effects.parquet` (100 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6172]; `tensor/DDL_lfc|DDL_z.npy` [6172]; `embed/gene_vectors.npy` [6172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6172 or target_col == 6172). Every well: [[IDH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
