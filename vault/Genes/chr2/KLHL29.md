---
symbol: "KLHL29"
type: "gene"
col: 4116
ensembl_id: "ENSG00000119771"
name: "kelch like family member 29"
location: "2p24.1"
module: 17
arm: "-"
pooled_cpm: 88.75
n_lines_expressing: 43
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# KLHL29

*kelch like family member 29* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.41× (z +31.6, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.233× (z -13.9, q 4e-41, down in 39 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKCE]] (+0.65, fdr 7e-06), [[FAM89A]] (+0.62, fdr 1e-05), [[LMBR1]] (+0.60, fdr 1e-05); moves opposite to [[NPHP1]] (-0.63, fdr 1e-05), [[PDIK1L]] (-0.61, fdr 3e-05), [[DLD]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[ZSCAN26]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.41×** | +31.6 | 0e+00 | 41/42 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +18.7 | 0e+00 | 39/40 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +17.7 | 0e+00 | 40/41 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +15.9 | 0e+00 | 35/41 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +13.8 | 4e-41 | 35/41 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +13.5 | 1e-39 | 31/43 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +13.5 | 1e-39 | 33/41 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.10×** | +13.5 | 1e-39 | 36/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +12.2 | 1e-32 | 37/42 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +11.4 | 4e-28 | 33/41 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +10.4 | 1e-23 | 26/41 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +8.2 | 8e-15 | 29/41 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +7.9 | 1e-13 | 28/41 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +6.3 | 1e-08 | 27/42 (A-427, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +6.2 | 2e-08 | 30/41 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 8e-08 | 20/41 (CFPAC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.233×** | -13.9 | 4e-41 | 39/42 (SNU-423, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.452×** | -13.4 | 3e-38 | 29/37 (KATO III, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.495×** | -12.3 | 3e-32 | 33/41 (LoVo, AN3 CA, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -11.0 | 8e-26 | 27/36 (HCT15, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.617×** | -8.8 | 2e-16 | 30/42 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.439×** | -7.8 | 4e-13 | 30/41 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -5.8 | 4e-07 | 23/41 (LOX-IMVI, A-427, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **0.754×** | -5.1 | 2e-05 | 24/40 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.598×** | -4.9 | 6e-05 | 25/40 (RKO, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.770×** | -4.8 | 1e-04 | 19/40 (LoVo, KATO III, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.839× | -4.5 | 3e-04 | 19/41 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.839× | -3.8 | 0.008 | 15/41 (HEC-1-A, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.824×** | -3.5 | 0.018 | 18/42 (HS-578T, HCT15, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.847× | -3.5 | 0.020 | 16/43 (NCI-H23, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.835× | -3.3 | 0.039 | 17/41 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | **0.833×** | -3.2 | 0.047 | 14/41 (LoVo, HT-29, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.841× | -3.0 | 0.079 | 14/40 (C32, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 82.7 | 7 | 9 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +29.6) | [[Harringtonine (drug)]] 5 µM 0.234× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.199× (z -10.5) |
| [[PANC-1 (line)]] | alt | 80.9 | 7 (1 ⚠) | 8 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.134× (z -13.7) |
| [[HOP62 (line)]] | alt | 73.3 | 13 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +18.5) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 87.8 | 12 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +18.8) | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -10.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 97.1 | 9 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +23.5) | [[TAK-901 (drug)]] 5 µM 0.191× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 78.0 | 10 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.98× (z +28.5) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.5 | 9 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +16.5) | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -15.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 485 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0816× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0891× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 233 | 4 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.352× (z -11.7) |
| [[LS 180 (line)]] | wt | 113 | 3 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.137× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 9 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.25× (z +19.2) | [[Adagrasib (drug)]] 0.05 µM 0.649× (z -9.3) ⚠ position not correctable |
| [[HEC-1-A (line)]] | alt | 167 | 1 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +15.7) | [[Harringtonine (drug)]] 5 µM 0.236× (z -16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.154× (z -11.9) |
| [[SW1417 (line)]] | alt | 50.6 | 9 | 0 | [[Tucidinostat (drug)]] 5 µM 5.29× (z +20.7) | — |
| [[J82 (line)]] | alt | 63.6 | 5 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -15.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 59.7 | 5 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.36× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -16.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 116 | 6 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +20.6) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -13.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 195 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.108× (z -13.0) |
| [[A498 (line)]] | wt | 34.0 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +22.1) | — |
| [[HT-29 (line)]] | alt | 80.0 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.29× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.8 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.39× (z +15.6) | — |
| [[RKO (line)]] | wt | 99.0 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +18.8) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.132× (z -9.2) |
| [[SNU-423 (line)]] | alt | 133 | 0 | 6 (5 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0558× (z -13.7) |
| [[A549 (line)]] | wt | 73.7 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +20.4) | [[Harringtonine (drug)]] 5 µM 0.335× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 62.7 | 1 | 4 (3 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.21× (z +8.7) | [[Lonafarnib (drug)]] 5 µM 0.0752× (z -10.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -8.5) |
| [[SHP-77 (line)]] | alt | 338 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.417× (z -10.4) |
| [[AN3 CA (line)]] | alt | 110 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.0675× (z -16.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 73.8 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -14.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 56.3 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 87.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -19.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 101 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 165 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.0502× (z -26.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 61.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 69.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 86.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 24.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +12.9) | — |
| [[SW48 (line)]] | wt | 59.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 69.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 80.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.28 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKCE]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FAM89A]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LMBR1]] | +0.60 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[GAN]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 | same gene group |
| [[DOCK9]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[ESRRA]] | +0.53 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PTPRG]] | +0.52 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ATP1B3]] | +0.52 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[TMEM181]] | +0.52 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[LONRF3]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SIPA1L1]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[DOCK5]] | +0.52 | +0.46 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP1]] | -0.63 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[PDIK1L]] | -0.61 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[DLD]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[TMEM254]] | -0.57 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[NDUFA5]] | -0.57 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[EHMT2]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SCRN3]] | -0.55 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[DNAL1]] | -0.55 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[GALT]] | -0.54 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[IFT22]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[IFT81]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[IQCK]] | -0.54 | -0.38 / -0.56 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KLHL29's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKH]] | B | ANKH activity raises KLHL29's level | lines that do not express ANKH (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without ANKH | 0.046 | ⚠ within organs, on part of the lines; also absent: GCNT1, LCA5, CA13; maybe low, not absent |
| [[STC2]] | B | STC2 activity raises KLHL29's level | lines that do not express STC2 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without STC2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CHST10, PEG10, ZNF606 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN26]] | B | KLHL29 activity raises ZSCAN26's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without KLHL29 | 0.013 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[NPHP1]] | B | KLHL29 activity raises NPHP1's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without KLHL29 | 0.032 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[DNAJC6]] | B | KLHL29 activity raises DNAJC6's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 2.33× lower at baseline in the lines without KLHL29 | 0.033 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[LINC-PINT]] | B | KLHL29 activity raises LINC-PINT's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without KLHL29 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[NBPF9]] | B | KLHL29 activity raises NBPF9's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without KLHL29 | 0.056 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[SMG7]] | B | KLHL29 activity lowers SMG7's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.17× higher at baseline in the lines without KLHL29 | 0.067 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[PRKCE]] | B | KLHL29 activity raises PRKCE's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without KLHL29 | 0.085 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[CASC2]] | B | KLHL29 activity raises CASC2's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 2.04× lower at baseline in the lines without KLHL29 | 0.087 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[MKS1]] | B | KLHL29 activity raises MKS1's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without KLHL29 | 0.091 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.4, 1.9); signed map (-18.8, 44.4). **Vector** length 123, 38.7% of its response variance represented; |z| ≥ 3 in 1,512 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +17.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +10.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +31.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.9 | +6.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.7 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +11.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.1 | -13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -13.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -5.2 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.0 | -12.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.0 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.9 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:23,385,179-23,708,611 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1921; previously KBTBD9 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q96CT2](https://www.uniprot.org/uniprotkb/Q96CT2) carries no function annotation.

**Summary**, from NCBI Gene [114818](https://www.ncbi.nlm.nih.gov/gene/114818):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29404) · Entrez [114818](https://www.ncbi.nlm.nih.gov/gene/114818) · UniProt [Q96CT2](https://www.uniprot.org/uniprotkb/Q96CT2) · Ensembl [ENSG00000119771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119771)

## Data

Gene col 4116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4116); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4116]; `tensor/DDL_lfc|DDL_z.npy` [4116]; `embed/gene_vectors.npy` [4116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4116 or target_col == 4116). Every well: [[KLHL29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
