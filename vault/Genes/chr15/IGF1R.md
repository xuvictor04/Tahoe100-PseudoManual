---
symbol: "IGF1R"
type: "gene"
col: 6408
ensembl_id: "ENSG00000140443"
name: "insulin like growth factor 1 receptor"
location: "15q26.3"
module: 225
arm: "+"
pooled_cpm: 329.06
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 33
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# IGF1R

*insulin like growth factor 1 receptor* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Bimiralisib (drug)]] 5 µM: 1.74× (z +4.7, q 0.002, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.400× (z -20.9, q 0e+00, down in 43 of 44 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.454× (z -12.8, q 6e-35, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGI1]] (+0.57, fdr 2e-05), [[CASTOR2]] (+0.53, fdr 3e-05), [[PTTG1IP]] (+0.52, fdr 2e-05); moves opposite to [[SEC23B]] (-0.55, fdr 2e-05), [[BMS1P4-1]] (-0.52, fdr 3e-05), [[GOSR1]] (-0.48, fdr 3e-05).
> It is in [[Module 225]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | **1.74×** | +4.7 | 0.002 | 35/46 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.044 | 33/44 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.073 | 28/45 (AsPC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | 1.48× | +3.3 | 0.14 | 27/45 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.21× | +3.1 | 0.22 | 22/44 (Hs 766T, PANC-1, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.0 | 0.23 | 13/44 (Hs 766T, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 18 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.400×** | -20.9 | 0e+00 | 43/44 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.428×** | -13.2 | 3e-37 | 43/44 (C32, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.454×** | -12.8 | 6e-35 | 42/44 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.471×** | -11.7 | 2e-29 | 36/43 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.563×** | -9.3 | 2e-18 | 40/44 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.563×** | -8.9 | 4e-17 | 34/40 (C32, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.564×** | -8.5 | 1e-15 | 33/41 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.617×** | -7.8 | 4e-13 | 35/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.573×** | -7.6 | 2e-12 | 36/45 (COLO 205, C32, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.645×** | -6.0 | 1e-07 | 33/44 (SW48, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -5.7 | 7e-07 | 34/44 (SW48, CHP-212, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.533×** | -5.3 | 5e-06 | 40/44 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.554×** | -5.0 | 3e-05 | 38/44 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **0.728×** | -4.9 | 4e-05 | 31/43 (SW48, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.745×** | -4.7 | 8e-05 | 29/44 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.583×** | -4.6 | 2e-04 | 38/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.585×** | -4.5 | 2e-04 | 33/44 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -4.5 | 2e-04 | 27/44 (HepG2/C3A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -4.2 | 7e-04 | 23/44 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.754×** | -4.1 | 0.001 | 26/44 (HOP62, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.635×** | -3.8 | 0.003 | 28/43 (SW48, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.709×** | -3.7 | 0.004 | 29/44 (MIA PaCa-2, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.656×** | -3.6 | 0.008 | 26/44 (SW48, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.725×** | -3.5 | 0.009 | 32/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.728×** | -3.5 | 0.011 | 32/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.2 | 0.022 | 24/44 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 683 | 0 | 15 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -30.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 529 | 0 | 14 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -27.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 779 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -32.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 662 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -17.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -10.1) |
| [[HOP62 (line)]] | alt | 582 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -22.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -16.5) |
| [[SW480 (line)]] | alt | 381 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -17.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 238 | 6 | 3 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.14× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -16.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 311 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -20.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 314 | 0 | 9 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.216× (z -17.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.403× (z -10.5) |
| [[LoVo (line)]] | wt | 393 | 1 (1 ⚠) | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +12.2) ⚠ cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -16.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -12.3) |
| [[C-33 A (line)]] | alt | 122 | 1 | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.29× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -19.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 367 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.200× (z -18.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 451 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -22.9) |
| [[RKO (line)]] | wt | 139 | 1 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +11.7) ⚠ cell-cycle shift, explains ~42% of this change | [[Harringtonine (drug)]] 5 µM 0.213× (z -14.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.239× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 236 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -20.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -12.5) |
| [[COLO 205 (line)]] | alt | 582 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -18.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.393× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 569 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -14.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -22.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -11.7) |
| [[SHP-77 (line)]] | alt | 408 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -13.3) |
| [[SNU-1 (line)]] | wt | 353 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.242× (z -15.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 270 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -20.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -14.2) |
| [[SW48 (line)]] | wt | 222 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.220× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.196× (z -12.6) |
| [[BT-474 (line)]] | alt | 236 | 1 | 3 (2 ⚠) | [[Neratinib (maleate) (drug)]] 5 µM 1.76× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 597 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.348× (z -11.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.444× (z -8.8) |
| [[LS 180 (line)]] | wt | 215 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.5) ⚠ cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -14.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -11.6) |
| [[PANC-1 (line)]] | alt | 462 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.390× (z -13.3) |
| [[HT-29 (line)]] | alt | 358 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -9.3) |
| [[J82 (line)]] | alt | 296 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.232× (z -14.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -11.1) |
| [[SW1417 (line)]] | alt | 133 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.473× (z -9.2) |
| [[A-172 (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.373× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 781 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -13.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CHP-212 (line)]] | wt | 450 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 199 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -11.3) ⚠ toxic |
| [[A-427 (line)]] | wt | 166 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.484× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 249 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.436× (z -9.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 327 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H661 (line)]] | alt | 458 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -8.5) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SW 1271 (line)]] | alt | 283 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 58.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 52.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 229 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 65.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 147 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 63.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 612 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGI1]] | +0.57 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[CASTOR2]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[PTTG1IP]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ZNF37BP]] | +0.52 | +0.37 / +0.47 | both halves | 7e-05 |  |
| [[RERE]] | +0.51 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[AGTPBP1]] | +0.50 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[FAM117B]] | +0.50 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FOXN3]] | +0.48 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[CDHR3]] | +0.48 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[HECA]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[RAP2A]] | +0.48 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[DOCK9]] | +0.47 | +0.44 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC23B]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[BMS1P4-1]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[GOSR1]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[AGAP9]] | -0.46 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[ZNF721]] | -0.45 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[FKBP15]] | -0.45 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[SCFD1]] | -0.45 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[AGAP5]] | -0.44 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[ZNF264]] | -0.43 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[GORAB]] | -0.43 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TRIM5]] | -0.43 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[UFL1]] | -0.43 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.488). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.8, -43.9); signed map (-28.1, 25.8). **Vector** length 101, 33.8% of its response variance represented; |z| ≥ 3 in 1,592 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | +2.7 | -4.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.1 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.5 | -20.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.1 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -11.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -5.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.7 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor 1 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:98,648,539-98,964,530 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JTK13, CD221, IGFIR, MGC18216, IGFR |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; MicroRNA protein coding host genes; Insulin receptor family |
| Hallmark sets | UV_RESPONSE_DN, IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_EARLY |
| Reactome | 11 pathways, smallest: SHC-related events triggered by IGF1R; Respiratory syncytial virus (RSV) attachment and entry; IRS-related events triggered by IGF1R |
| Matched by | ensembl_id |

**Function**, from UniProt [P08069](https://www.uniprot.org/uniprotkb/P08069) (Insulin-like growth factor 1 receptor):

> Receptor tyrosine kinase which mediates actions of insulin-like growth factor 1 (IGF1). Binds IGF1 with high affinity and IGF2 and insulin (INS) with a lower affinity. The activated IGF1R is involved in cell growth and survival control. IGF1R is crucial for tumor transformation and survival of malignant cell. Ligand binding activates the receptor kinase, leading to receptor autophosphorylation, and tyrosines phosphorylation of multiple substrates, that function as signaling adapter proteins …

**Summary**, from NCBI Gene [3480](https://www.ncbi.nlm.nih.gov/gene/3480):

> This receptor binds insulin-like growth factor with a high affinity. It has tyrosine kinase activity. The insulin-like growth factor I receptor plays a critical role in transformation events. Cleavage of the precursor generates alpha and beta subunits. It is highly overexpressed in most malignant tissues where it functions as an anti-apoptotic agent by enhancing cell survival. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:5465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5465) · Entrez [3480](https://www.ncbi.nlm.nih.gov/gene/3480) · UniProt [P08069](https://www.uniprot.org/uniprotkb/P08069) · Ensembl [ENSG00000140443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140443)

## Data

Gene col 6408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6408); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6408]; `tensor/DDL_lfc|DDL_z.npy` [6408]; `embed/gene_vectors.npy` [6408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6408 or target_col == 6408). Every well: [[IGF1R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGF1R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
