---
symbol: "ANKRD11"
type: "gene"
col: 9476
ensembl_id: "ENSG00000167522"
name: "ankyrin repeat domain 11"
location: "16q24.3"
module: 63
arm: "+"
pooled_cpm: 608.96
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ANKRD11

*ankyrin repeat domain 11* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.11× (z +10.4, q 2e-22, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.532× (z -16.1, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.574× (z -14.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIB3]] (+0.70, fdr 7e-06), [[GARS1]] (+0.69, fdr 7e-06), [[SESN2]] (+0.67, fdr 7e-06); moves opposite to [[ZBTB33]] (-0.45, fdr 4e-05), [[MEF2C]] (-0.42, fdr 3e-05), [[IFT57]] (-0.41, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +10.4 | 2e-22 | 47/49 (COLO 205, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +8.1 | 2e-13 | 40/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +7.7 | 3e-12 | 37/48 (LoVo, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +7.6 | 3e-12 | 32/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.21×** | +7.2 | 6e-11 | 26/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +6.1 | 9e-08 | 27/47 (COLO 205, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +6.1 | 9e-08 | 33/48 (SW480, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +5.4 | 4e-06 | 25/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +5.1 | 3e-05 | 12/49 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +4.9 | 5e-05 | 24/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.20×** | +4.8 | 7e-05 | 24/48 (NCI-H2030, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.8 | 7e-05 | 24/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.19× | +4.5 | 2e-04 | 21/47 (SNU-1, SK-MEL-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +4.4 | 5e-04 | 9/48 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.009 | 19/48 (SW480, BT-474, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.14× | +3.5 | 0.014 | 14/48 (SNU-1, NCI-H23, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.015 | 15/48 (SNU-1, SW48, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.026 | 8/48 (HCT15, A-172, …) | rises with dose | plate-row cell shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.031 | 5/48 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.034 | 4/48 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.035 | 14/48 (Hs 766T, SNU-1, …) | rises with dose |  |
| [[Tadalafil (drug)]] 5 µM |  | 1.13× | +3.1 | 0.045 | 6/48 (SW48, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -16.1 | 0e+00 | 42/44 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.538×** | -15.8 | 0e+00 | 45/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.574×** | -14.7 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.618×** | -12.8 | 3e-35 | 41/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -12.4 | 2e-33 | 42/49 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -11.1 | 1e-26 | 33/49 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.703×** | -9.3 | 7e-19 | 37/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.750×** | -7.7 | 1e-12 | 37/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -6.2 | 5e-08 | 18/48 (PANC-1, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.813×** | -5.5 | 2e-06 | 27/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.811×** | -5.4 | 4e-06 | 26/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.835× | -4.8 | 7e-05 | 20/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.842× | -4.4 | 5e-04 | 22/47 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.899× | -4.0 | 0.002 | 9/48 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.762×** | -3.8 | 0.006 | 26/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.892× | -3.4 | 0.020 | 9/48 (PANC-1, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.792×** | -3.2 | 0.034 | 24/47 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.888× | -3.2 | 0.043 | 13/47 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.896× | -2.9 | 0.079 | 4/48 (RPMI-7951, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 730 | 0 | 20 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -29.6) |
| [[A-172 (line)]] | wt | 792 | 2 (1 ⚠) | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +19.2) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.13× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.444× (z -15.7) |
| [[H4 (line)]] | wt | 1,116 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.400× (z -15.4) |
| [[HOP62 (line)]] | alt | 950 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -15.8) |
| [[LoVo (line)]] | wt | 641 | 2 | 8 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +17.4) | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -21.0) |
| [[MIA PaCa-2 (line)]] | alt | 796 | 3 (2 ⚠) | 7 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.80× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.39× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -16.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.524× (z -12.4) |
| [[A498 (line)]] | wt | 704 | 2 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.71× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 468 | 5 (3 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.550× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 480 | 2 (2 ⚠) | 6 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.71× (z +9.3) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.382× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.499× (z -12.6) |
| [[A549 (line)]] | wt | 734 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.347× (z -16.3) |
| [[HS-578T (line)]] | alt | 757 | 2 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +17.1) ⚠ cell-cycle shift, explains ~15% of this change | [[Panobinostat (drug)]] 0.5 µM 0.497× (z -10.7) |
| [[HT-29 (line)]] | alt | 772 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.443× (z -14.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 619 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.94× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.507× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 865 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.2) |
| [[HCT15 (line)]] | alt | 821 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.37× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.584× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 579 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +11.8) ⚠ cell-cycle shift, explains ~15% of this change | [[Dinaciclib (drug)]] 5 µM 0.466× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.556× (z -10.6) |
| [[KATO III (line)]] | alt | 795 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.422× (z -15.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.567× (z -10.4) |
| [[SW48 (line)]] | wt | 535 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.57× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -9.4) |
| [[SW480 (line)]] | alt | 405 | 5 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.93× (z +15.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.622× (z -10.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 557 | 3 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.80× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.566× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.581× (z -9.0) |
| [[J82 (line)]] | alt | 620 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +15.0) ⚠ cell-cycle shift, explains ~15% of this change | [[Dinaciclib (drug)]] 5 µM 0.511× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.603× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 826 | 2 (1 ⚠) | 3 (2 ⚠) | [[Neratinib (maleate) (drug)]] 5 µM 1.56× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 525 | 1 (1 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.74× (z +9.1) ⚠ toxic | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.557× (z -9.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.580× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 628 | 3 | 1 | [[Ponatinib (drug)]] 5 µM 1.82× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.540× (z -10.8) |
| [[Hs 766T (line)]] | wt | 544 | 2 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.98× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.523× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 588 | 2 (1 ⚠) | 2 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.79× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 547 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.508× (z -11.5) |
| [[C32 (line)]] | wt | 420 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.43× (z +13.6) | — |
| [[COLO 205 (line)]] | alt | 445 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.24× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 591 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.502× (z -11.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.545× (z -10.1) |
| [[LS 180 (line)]] | wt | 690 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.436× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 598 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.514× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.662× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 539 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.493× (z -11.1) |
| [[A-427 (line)]] | wt | 390 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.541× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.602× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 419 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.15× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.502× (z -12.0) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 566 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.578× (z -8.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.594× (z -8.5) |
| [[SNU-423 (line)]] | alt | 462 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +11.7) ⚠ cell-cycle shift, explains ~15% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.537× (z -10.3) ⚠ toxic |
| [[C-33 A (line)]] | alt | 400 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.609× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 500 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 1.56× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 356 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.498× (z -11.1) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 418 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.447× (z -10.3) |
| [[RKO (line)]] | wt | 439 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.546× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 735 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.9) |
| [[SW1417 (line)]] | alt | 633 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.524× (z -9.4) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 455 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 315 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 542 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 584 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 725 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIB3]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[GARS1]] | +0.69 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[SESN2]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[MARS1]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SARS1]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ARHGEF2]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CARS1]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ADM2]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CHAC1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[EIF2S2]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GOT1]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[XPOT]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB33]] | -0.45 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MEF2C]] | -0.42 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[IFT57]] | -0.41 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[TET2]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | ANKRD11's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | ANKRD11's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.478 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, 48.9); signed map (-12.5, 24.9). **Vector** length 115, 43.9% of its response variance represented; |z| ≥ 3 in 1,756 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.55 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.58 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.58 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +7.7 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +6.4 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.2 | +6.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.1 | +4.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +5.0 | +7.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.8 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.2 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.8 | -15.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.3 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,267,630-89,490,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LZ16, T13, ANCO1, ANCO-1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UB99](https://www.uniprot.org/uniprotkb/Q6UB99) (Ankyrin repeat domain-containing protein 11):

> Chromatin regulator which modulates histone acetylation and gene expression in neural precursor cells (By similarity). May recruit histone deacetylases (HDACs) to the p160 coactivators/nuclear receptor complex to inhibit ligand-dependent transactivation. Has a role in proliferation and development of cortical neural precursors. May also regulate bone homeostasis (By similarity).

**Summary**, from NCBI Gene [29123](https://www.ncbi.nlm.nih.gov/gene/29123):

> This locus encodes an ankryin repeat domain-containing protein. The encoded protein inhibits ligand-dependent activation of transcription. Mutations in this gene have been associated with KBG syndrome, which is characterized by macrodontia, distinctive craniofacial features, short stature, skeletal anomalies, global developmental delay, seizures and intellectual disability. Alternatively spliced transcript variants have been described. Related pseudogenes exist on chromosomes 2 and X. [provided …

**Accessions** — [HGNC:21316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21316) · Entrez [29123](https://www.ncbi.nlm.nih.gov/gene/29123) · UniProt [Q6UB99](https://www.uniprot.org/uniprotkb/Q6UB99) · Ensembl [ENSG00000167522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167522)

## Data

Gene col 9476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9476); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9476]; `tensor/DDL_lfc|DDL_z.npy` [9476]; `embed/gene_vectors.npy` [9476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9476 or target_col == 9476). Every well: [[ANKRD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
