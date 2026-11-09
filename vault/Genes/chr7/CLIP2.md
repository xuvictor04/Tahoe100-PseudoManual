---
symbol: "CLIP2"
type: "gene"
col: 2791
ensembl_id: "ENSG00000106665"
name: "CAP-Gly domain containing linker protein 2"
location: "7q11.23"
module: 161
arm: "+"
pooled_cpm: 174.42
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 34
n_dd_up_clean: 14
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# CLIP2

*CAP-Gly domain containing linker protein 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +14.1, q 2e-42, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.387× (z -19.3, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.715× (z -9.6, q 9e-20, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3CD]] (+0.65, fdr 7e-06), [[TBC1D10A]] (+0.64, fdr 1e-05), [[TGFB1]] (+0.63, fdr 1e-05); moves opposite to [[DERA]] (-0.61, fdr 2e-05), [[RAB11FIP2]] (-0.58, fdr 3e-05), [[ZMYND11]] (-0.56, fdr 4e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PLAUR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +14.1 | 2e-42 | 33/48 (CFPAC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +10.6 | 9e-24 | 29/48 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +10.1 | 1e-21 | 37/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +9.4 | 8e-19 | 36/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +9.3 | 2e-18 | 34/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +8.9 | 4e-17 | 32/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.5 | 4e-06 | 28/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 9e-05 | 30/48 (HOP62, Hs 766T, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +4.3 | 9e-04 | 24/49 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +4.2 | 0.001 | 25/49 (KATO III, HT-29, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.005 | 27/48 (LoVo, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.023 | 20/49 (C32, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.057 | 22/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.1 | 0.067 | 14/48 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.072 | 13/49 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.081 | 20/48 (NCI-H2347, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.081 | 15/48 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2791.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.387×** | -19.3 | 0e+00 | 45/49 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -18.0 | 0e+00 | 41/44 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -12.7 | 6e-35 | 36/45 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -9.6 | 9e-20 | 32/49 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -8.6 | 9e-16 | 39/47 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -6.6 | 4e-09 | 29/48 (A-172, SW1417, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -6.5 | 9e-09 | 32/48 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.519×** | -6.4 | 9e-09 | 33/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.741×** | -6.1 | 8e-08 | 33/48 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.750×** | -5.8 | 3e-07 | 28/48 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.735×** | -5.8 | 4e-07 | 26/47 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.754×** | -5.7 | 5e-07 | 26/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -5.6 | 1e-06 | 27/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.824×** | -5.5 | 1e-06 | 24/48 (NCI-H2347, SW48, …) | top dose only | low cells (technical?) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.767×** | -5.4 | 3e-06 | 25/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.767×** | -5.4 | 3e-06 | 25/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.792×** | -4.7 | 7e-05 | 25/48 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.796×** | -4.6 | 1e-04 | 22/48 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.804×** | -4.4 | 3e-04 | 24/48 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.806×** | -4.4 | 3e-04 | 24/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.817×** | -4.1 | 0.001 | 22/48 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.673×** | -3.9 | 0.002 | 23/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 111 | 16 (9 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 84.8 | 6 (3 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.1) | [[Clobetasol propionate (drug)]] 5 µM 0.369× (z -9.8) |
| [[KATO III (line)]] | alt | 214 | 5 (1 ⚠) | 6 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.95× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -21.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 332 | 0 | 10 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.226× (z -14.7) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 168 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -23.4) |
| [[SW1417 (line)]] | alt | 365 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -21.2) |
| [[A-172 (line)]] | wt | 341 | 3 (1 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.14× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.393× (z -17.8) |
| [[AsPC-1 (line)]] | alt | 345 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -24.1) |
| [[C32 (line)]] | wt | 120 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.06× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -14.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 62.5 | 6 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.95× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 132 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +18.2) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Budesonide (drug)]] 0.5 µM 0.430× (z -8.9) |
| [[BT-474 (line)]] | alt | 57.1 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 251 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -12.4) |
| [[LoVo (line)]] | wt | 206 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.15× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -12.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 231 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.365× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 110 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 220 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.7) |
| [[A498 (line)]] | wt | 265 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -14.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 209 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +19.8) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 180 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0773× (z -22.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 128 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +24.6) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -12.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 153 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.16× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 354 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -11.8) |
| [[J82 (line)]] | alt | 121 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 83.7 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.3) |
| [[PANC-1 (line)]] | alt | 109 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.96× (z +12.2) | — |
| [[SW48 (line)]] | wt | 392 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -18.9) |
| [[SW480 (line)]] | alt | 226 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.0) |
| [[HCT15 (line)]] | alt | 176 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -21.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 131 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 3.04× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.33× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -13.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 157 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0541× (z -32.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 164 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.34× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 214 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 145 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 103 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.03× (z +9.9) | — |
| [[RKO (line)]] | wt | 86.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.59× (z +9.5) | — |
| [[A-427 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 203 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3CD]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TBC1D10A]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TGFB1]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GDPD5]] | +0.62 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[DLGAP4]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ARL4C]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ZBTB46]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[PPARA]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SPATA2L]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PLIN3]] | +0.60 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DERA]] | -0.61 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | -0.58 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.56 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SNX5]] | -0.55 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZC3HAV1L]] | -0.54 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[UHMK1]] | -0.54 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SEPHS1]] | -0.54 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[NNT]] | -0.54 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[FUBP1]] | -0.54 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ATL3]] | -0.53 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[SETD7]] | -0.53 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[ANGEL2]] | -0.52 | -0.45 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAUR]] | B | PLAUR activity raises CLIP2's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without PLAUR | 0.014 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[COL5A3]] | B | COL5A3 activity raises CLIP2's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.46× lower at baseline in the lines without COL5A3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[TOP2A]] | B | TOP2A activity raises CLIP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPAS1]] | B | NPAS1 activity raises CLIP2's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without NPAS1 | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers CLIP2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[MEGF6]] | B | MEGF6 activity raises CLIP2's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without MEGF6 | 0.086 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.0, -3.5); signed map (-2.0, 43.8). **Vector** length 151, 52.8% of its response variance represented; |z| ≥ 3 in 1,867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.3 | +8.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.7 | +10.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.4 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.1 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.1 | +9.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.1 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.8 | +3.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.5 | +3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.6 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -12.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -6.2 | -5.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.9 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.4 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -5.1 | -4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | CAP-Gly domain containing linker protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,289,407-74,405,935 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLIP-115, KIAA0291, WSCR4, CLIP, WSCR3; previously WBSCR4, CYLN2, WBSCR3 |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UDT6](https://www.uniprot.org/uniprotkb/Q9UDT6) (CAP-Gly domain-containing linker protein 2):

> Seems to link microtubules to dendritic lamellar body (DLB), a membranous organelle predominantly present in bulbous dendritic appendages of neurons linked by dendrodendritic gap junctions. May operate in the control of brain-specific organelle translocations (By similarity).

**Summary**, from NCBI Gene [7461](https://www.ncbi.nlm.nih.gov/gene/7461):

> The protein encoded by this gene belongs to the family of cytoplasmic linker proteins, which have been proposed to mediate the interaction between specific membranous organelles and microtubules. This protein was found to associate with both microtubules and an organelle called the dendritic lamellar body. This gene is hemizygously deleted in Williams syndrome, a multisystem developmental disorder caused by the deletion of contiguous genes at 7q11.23. Alternative splicing of this gene generates …

**Accessions** — [HGNC:2586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2586) · Entrez [7461](https://www.ncbi.nlm.nih.gov/gene/7461) · UniProt [Q9UDT6](https://www.uniprot.org/uniprotkb/Q9UDT6) · Ensembl [ENSG00000106665](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106665)

## Data

Gene col 2791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2791); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2791]; `tensor/DDL_lfc|DDL_z.npy` [2791]; `embed/gene_vectors.npy` [2791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2791 or target_col == 2791). Every well: [[CLIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
