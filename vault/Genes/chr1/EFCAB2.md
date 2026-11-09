---
symbol: "EFCAB2"
type: "gene"
col: 12774
ensembl_id: "ENSG00000203666"
name: "dynein regulatory complex subunit 8"
location: "1q44"
module: 137
arm: "+"
pooled_cpm: 40.02
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 21
n_dd_up_clean: 19
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# EFCAB2

*dynein regulatory complex subunit 8* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.13× (z +27.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.156× (z -31.0, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBLD]] (+0.80, fdr 1e-05), [[SPRY3]] (+0.80, fdr 1e-05), [[PKN2-AS1]] (+0.77, fdr 1e-04); moves opposite to [[FCHO1]] (-0.74, fdr 1e-05), [[YIF1B]] (-0.72, fdr 8e-05), [[ARRB2]] (-0.69, fdr 2e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TMEM92]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +27.0 | 0e+00 | 46/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +10.2 | 5e-22 | 36/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +9.5 | 3e-19 | 34/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +8.4 | 8e-15 | 27/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +8.3 | 8e-15 | 28/44 (LoVo, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +7.8 | 7e-13 | 26/42 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +7.7 | 2e-12 | 23/36 (H4, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 8e-09 | 30/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.2 | 4e-08 | 25/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +5.6 | 9e-07 | 26/47 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 18/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.006 | 19/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.012 | 13/48 (LoVo, NCI-H1792, …) | all doses, flat |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.5 | 0.017 | 12/48 (A-172, LoVo, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.019 | 8/48 (PANC-1, SW480, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.020 | 8/48 (SW480, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.020 | 12/48 (A498, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.022 | 9/48 (A549, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.156×** | -31.0 | 0e+00 | 47/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.176×** | -29.0 | 0e+00 | 47/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.192×** | -27.6 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.222×** | -25.1 | 0e+00 | 47/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.302×** | -20.0 | 0e+00 | 46/47 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.488×** | -16.9 | 0e+00 | 47/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.175×** | -15.2 | 0e+00 | 46/48 (NCI-H23, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.470×** | -12.6 | 1e-34 | 41/48 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.605×** | -8.4 | 3e-15 | 37/48 (C32, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -5.5 | 2e-06 | 28/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.816×** | -4.8 | 9e-05 | 28/48 (CFPAC-1, SW 1271, …) | rises with dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **0.711×** | -4.1 | 0.002 | 16/48 (SW 1271, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.790×** | -3.8 | 0.007 | 18/47 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.808×** | -3.6 | 0.015 | 17/47 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.031 | 20/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.5 | 2 | 8 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.0779× (z -28.5) |
| [[C32 (line)]] | wt | 32.4 | 2 | 7 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.0393× (z -20.6) |
| [[HOP62 (line)]] | alt | 63.7 | 1 | 8 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +14.3) | [[Belinostat (drug)]] 5 µM 0.0691× (z -26.7) |
| [[MIA PaCa-2 (line)]] | alt | 38.3 | 1 | 8 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +12.4) | [[Panobinostat (drug)]] 0.05 µM 0.0789× (z -19.3) |
| [[PANC-1 (line)]] | alt | 78.0 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0729× (z -31.3) |
| [[RPMI-7951 (line)]] | alt | 60.3 | 1 | 8 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.141× (z -14.6) |
| [[SW 900 (line)]] | alt | 73.9 | 1 | 8 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.2) | [[Belinostat (drug)]] 5 µM 0.0976× (z -20.5) |
| [[SW480 (line)]] | alt | 44.7 | 1 | 8 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.2) | [[Belinostat (drug)]] 5 µM 0.119× (z -24.1) |
| [[A498 (line)]] | wt | 38.8 | 1 | 7 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.190× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 92.7 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0507× (z -30.3) |
| [[SNU-423 (line)]] | alt | 33.7 | 1 | 7 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.0770× (z -18.0) |
| [[A-427 (line)]] | wt | 32.0 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -13.4) |
| [[HT-29 (line)]] | alt | 17.6 | 3 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +15.5) | [[Belinostat (drug)]] 5 µM 0.184× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.5) | [[Panobinostat (drug)]] 0.05 µM 0.0662× (z -18.2) |
| [[J82 (line)]] | alt | 51.3 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.0917× (z -22.6) |
| [[LoVo (line)]] | wt | 17.3 | 4 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +18.4) | [[Belinostat (drug)]] 5 µM 0.158× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 61.3 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.0764× (z -21.3) |
| [[RKO (line)]] | wt | 33.1 | 1 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 34.1 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -16.1) |
| [[H4 (line)]] | wt | 36.9 | 3 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.160× (z -9.8) |
| [[Hs 766T (line)]] | wt | 31.8 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -14.1) |
| [[HS-578T (line)]] | alt | 34.9 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0719× (z -19.8) |
| [[LS 180 (line)]] | wt | 20.8 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +14.5) | [[Belinostat (drug)]] 5 µM 0.0841× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 20.0 | 2 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +16.3) | [[Belinostat (drug)]] 5 µM 0.117× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 54.3 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -16.7) |
| [[A549 (line)]] | wt | 25.9 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.6) | [[Belinostat (drug)]] 5 µM 0.140× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 24.6 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +14.7) | [[Panobinostat (drug)]] 0.05 µM 0.215× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 53.4 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -13.7) |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -20.4) |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +11.2) | [[Panobinostat (drug)]] 0.05 µM 0.122× (z -11.4) |
| [[SW48 (line)]] | wt | 26.9 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.0526× (z -14.4) |
| [[HCT15 (line)]] | alt | 45.1 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.113× (z -14.4) |
| [[HepG2_C3A (line)]] | wt | 33.5 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +13.0) | [[Belinostat (drug)]] 5 µM 0.171× (z -10.6) |
| [[SW1417 (line)]] | alt | 24.0 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +11.1) | [[Panobinostat (drug)]] 0.05 µM 0.138× (z -13.7) |
| [[A-172 (line)]] | wt | 24.0 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -9.5) |
| [[C-33 A (line)]] | alt | 46.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -14.6) |
| [[COLO 205 (line)]] | alt | 18.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.111× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 18.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.170× (z -9.2) |
| [[SNU-1 (line)]] | wt | 42.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 25.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -11.3) |
| [[BT-474 (line)]] | alt | 43.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -9.3) |
| [[CHP-212 (line)]] | wt | 40.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0963× (z -10.6) |
| [[KATO III (line)]] | alt | 10.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +10.4) | [[Belinostat (drug)]] 0.5 µM 0.124× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.76× (z +14.2) | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -9.9) |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | +0.80 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SPRY3]] | +0.80 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.77 | +0.72 / +0.35 | both halves | 1e-04 |  |
| [[CRPPA]] | +0.77 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.76 | +0.72 / +0.29 | both halves | 2e-04 |  |
| [[ZMYND11]] | +0.73 | +0.66 / +0.57 | both halves | 8e-06 |  |
| [[AVEN]] | +0.73 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.73 | +0.69 / +0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[INO80D]] | +0.72 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SLC25A21]] | +0.72 | +0.67 / +0.30 | both halves | 2e-04 |  |
| [[LINC01004]] | +0.72 | +0.69 / +0.29 | both halves | 2e-04 |  |
| [[FAM174B]] | +0.72 | +0.67 / +0.38 | both halves | 6e-05 |  |
| [[ERMAP]] | +0.72 | +0.64 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | -0.74 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[YIF1B]] | -0.72 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ARRB2]] | -0.69 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MAST3]] | -0.69 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[WASF3]] | -0.68 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[LRFN3]] | -0.67 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[LPCAT2]] | -0.67 | -0.60 / -0.55 | both halves | 1e-05 | same gene group |
| [[GPR160]] | -0.67 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[SGSM1]] | -0.66 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.66 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SLC27A1]] | -0.65 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[TNFAIP8L1]] | -0.65 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92]] | B | TMEM92 activity lowers EFCAB2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.37× higher at baseline in the lines without TMEM92 | 0.025 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[ADGRB2]] | B | ADGRB2 activity raises EFCAB2's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without ADGRB2 | 0.027 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[TOP2A]] | B | TOP2A activity lowers EFCAB2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CBLC]] | B | CBLC activity lowers EFCAB2's level | lines that do not express CBLC (31) vs lines expressing it (19) | 1.50× higher at baseline in the lines without CBLC | 0.042 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[SYT11]] | B | SYT11 activity raises EFCAB2's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without SYT11 | 0.061 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[PLCXD2]] | B | PLCXD2 activity lowers EFCAB2's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 1.46× higher at baseline in the lines without PLCXD2 | 0.090 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[SLC2A3]] | B | SLC2A3 activity raises EFCAB2's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without SLC2A3 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[CBLC]] | C | CBLC activity weakens EFCAB2's drug response | lines that do not express CBLC (31) vs lines expressing it (17) | the lines without CBLC respond 1.03× as strongly (z diff -0.80); strongest at Brivudine 5 µM: 0.16x vs 0.22x (z diff -2.0) | 0.077 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8; target measured in part of the lines; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.4, 10.5); signed map (24.5, -25.3). **Vector** length 140, 43.4% of its response variance represented; |z| ≥ 3 in 1,289 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.2 | +27.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.8 | +10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +5.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +1.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -12.8 | -25.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -12.6 | -16.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -11.9 | -20.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -11.0 | -31.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -10.5 | -12.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -8.2 | -15.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.8 | -3.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.8 | -8.4 |

## What is on record

|  |  |
|---|---|
| Name | dynein regulatory complex subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:244,969,682-245,127,164 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC12458, DRC8, CFAP200; previously EFCAB2 |
| Gene groups (HGNC) | EF-hand domain containing; Dynein regulatory complex; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VUJ9](https://www.uniprot.org/uniprotkb/Q5VUJ9) (Dynein regulatory complex protein 8):

> Component of the nexin-dynein regulatory complex (N-DRC), a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes.

**Summary**, from NCBI Gene [84288](https://www.ncbi.nlm.nih.gov/gene/84288):

> The gene encodes a protein that contains two EF-hand calcium-binding domains although its function has yet to be determined. Alternatively spliced transcripts have been observed. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:28166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28166) · Entrez [84288](https://www.ncbi.nlm.nih.gov/gene/84288) · UniProt [Q5VUJ9](https://www.uniprot.org/uniprotkb/Q5VUJ9) · Ensembl [ENSG00000203666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203666)

## Data

Gene col 12774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12774); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12774]; `tensor/DDL_lfc|DDL_z.npy` [12774]; `embed/gene_vectors.npy` [12774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12774 or target_col == 12774). Every well: [[EFCAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
