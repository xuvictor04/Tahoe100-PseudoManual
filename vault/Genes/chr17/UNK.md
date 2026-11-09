---
symbol: "UNK"
type: "gene"
col: 5328
ensembl_id: "ENSG00000132478"
name: "unk zinc finger"
location: "17q25.1"
module: 95
arm: "+"
pooled_cpm: 54.68
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# UNK

*unk zinc finger* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +23.7, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.382× (z -22.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFYC]] (+0.76, fdr 1e-05), [[HHLA3]] (+0.74, fdr 3e-05), [[RBX1]] (+0.73, fdr 7e-06); moves opposite to [[ST6GALNAC4]] (-0.72, fdr 2e-05), [[WASF3]] (-0.71, fdr 4e-05), [[STRAP]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZDHHC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +23.7 | 0e+00 | 39/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +19.3 | 0e+00 | 40/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +17.2 | 0e+00 | 44/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +9.1 | 2e-17 | 28/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +8.5 | 3e-15 | 29/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +8.0 | 9e-14 | 31/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +7.3 | 3e-11 | 36/48 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +5.2 | 1e-05 | 24/48 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +5.0 | 3e-05 | 24/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +4.7 | 1e-04 | 22/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.4 | 4e-04 | 18/48 (A-427, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.23×** | +4.4 | 5e-04 | 17/47 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.003 | 20/48 (A-427, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.008 | 15/48 (A549, BT-474, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.18× | +3.7 | 0.008 | 13/49 (C32, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.010 | 16/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.013 | 17/47 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.015 | 14/47 (HOP62, SW1417, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +3.5 | 0.015 | 7/48 (A549, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.015 | 14/47 (HEC-1-A, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.382×** | -22.3 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.402×** | -21.1 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.410×** | -20.7 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.417×** | -20.3 | 0e+00 | 46/48 (HOP62, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -16.0 | 0e+00 | 30/43 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -14.4 | 4e-45 | 40/48 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.576×** | -12.8 | 2e-35 | 44/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.585×** | -12.4 | 2e-33 | 41/48 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.465×** | -9.3 | 1e-18 | 42/49 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.671×** | -8.5 | 8e-16 | 27/44 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.545×** | -7.3 | 1e-11 | 39/49 (SW480, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.737×** | -6.6 | 1e-09 | 30/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -6.6 | 1e-09 | 27/48 (SW480, NCI-H2030, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -6.6 | 1e-09 | 29/47 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.583×** | -6.5 | 3e-09 | 30/43 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -5.7 | 4e-07 | 30/48 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.828×** | -4.2 | 9e-04 | 15/48 (A549, NCI-H460, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.739×** | -3.7 | 0.007 | 11/48 (HOP62, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 87.9 | 5 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.276× (z -17.8) |
| [[SW480 (line)]] | alt | 72.1 | 3 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -19.0) |
| [[HOP62 (line)]] | alt | 55.6 | 2 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.230× (z -17.9) |
| [[LoVo (line)]] | wt | 57.1 | 6 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +20.0) | [[Panobinostat (drug)]] 5 µM 0.323× (z -12.6) |
| [[A549 (line)]] | wt | 57.8 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.408× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 65.9 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +21.1) | [[Belinostat (drug)]] 5 µM 0.322× (z -14.7) |
| [[A-172 (line)]] | wt | 60.3 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +25.1) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.389× (z -10.5) |
| [[LS 180 (line)]] | wt | 60.0 | 3 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.338× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 44.6 | 4 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.403× (z -9.4) |
| [[HT-29 (line)]] | alt | 55.6 | 1 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +13.6) | [[Belinostat (drug)]] 5 µM 0.268× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +15.7) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 57.6 | 3 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +17.5) | [[Belinostat (drug)]] 5 µM 0.371× (z -9.9) |
| [[SNU-423 (line)]] | alt | 64.2 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.316× (z -12.7) |
| [[A498 (line)]] | wt | 50.7 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 46.6 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -12.9) |
| [[A-427 (line)]] | wt | 64.9 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.448× (z -8.9) |
| [[C-33 A (line)]] | alt | 84.1 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -11.6) |
| [[COLO 205 (line)]] | alt | 70.9 | 1 | 4 | [[Harringtonine (drug)]] 5 µM 3.50× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.269× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 53.4 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.334× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 71.1 | 0 | 5 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -24.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.451× (z -8.9) |
| [[PANC-1 (line)]] | alt | 45.1 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +21.4) | [[Panobinostat (drug)]] 5 µM 0.503× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 52.4 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.338× (z -9.8) |
| [[SW1417 (line)]] | alt | 48.9 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.6) |
| [[C32 (line)]] | wt | 49.8 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.5) | [[Auranofin (drug)]] 5 µM 0.372× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 36.1 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.339× (z -9.4) |
| [[HCT15 (line)]] | alt | 69.0 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +13.5) | [[Auranofin (drug)]] 5 µM 0.302× (z -10.9) |
| [[KATO III (line)]] | alt | 59.0 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.441× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 45.0 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.303× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 44.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.356× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 39.5 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -9.3) |
| [[SW 900 (line)]] | alt | 60.3 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.259× (z -13.2) |
| [[H4 (line)]] | wt | 53.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0687× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.178× (z -12.9) |
| [[Hs 766T (line)]] | wt | 29.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -15.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 40.3 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.7) | [[Auranofin (drug)]] 5 µM 0.239× (z -13.2) |
| [[RKO (line)]] | wt | 36.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +17.4) | — |
| [[SNU-1 (line)]] | wt | 49.2 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.51× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -11.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 70.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.283× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 49.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.332× (z -9.2) |
| [[J82 (line)]] | alt | 36.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.373× (z -8.9) |
| [[AN3 CA (line)]] | alt | 73.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -12.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 61.2 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0646× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFYC]] | +0.76 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[HHLA3]] | +0.74 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[RBX1]] | +0.73 | +0.66 / +0.65 | both halves | 7e-06 | same gene group |
| [[CREBBP]] | +0.72 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.71 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TRAF3IP2-AS1]] | +0.71 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[WBP4]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[LRCH3]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PATL2]] | +0.71 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[AP5S1]] | +0.70 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[RBM5]] | +0.70 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | +0.70 | +0.69 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | -0.72 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[WASF3]] | -0.71 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[STRAP]] | -0.69 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ATP13A2]] | -0.67 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[TCP1]] | -0.67 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[BLTP2]] | -0.67 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[PAPSS1]] | -0.65 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MBOAT2]] | -0.65 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[HK1]] | -0.64 | -0.67 / -0.37 | both halves | 8e-05 |  |
| [[RNF216P1]] | -0.64 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[PAFAH1B2]] | -0.64 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[NDRG3]] | -0.63 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDHHC1]] | C | ZDHHC1 activity raises UNK's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without ZDHHC1 | 0.019 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |
| [[MIR181A2HG]] | C | MIR181A2HG activity raises UNK's level | lines that do not express MIR181A2HG (3) vs lines expressing it (47) | 1.29× lower at baseline in the lines without MIR181A2HG | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: APOBEC3C, VAT1, CAPRIN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.782). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (1.5, 10.7); signed map (21.6, -16.3). **Vector** length 133, 39.8% of its response variance represented; |z| ≥ 3 in 1,303 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.56 to 7); *Activation of HOX genes during differentiation* (reactome, mean cos +0.60 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.2 | +23.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.7 | +19.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +12.0 | +17.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.9 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.8 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.8 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.9 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.8 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.6 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.9 | -21.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.7 | -20.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.3 | -12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.4 | -12.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.8 | -22.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.1 | -7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -6.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | unk zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,784,806-75,825,799 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1753; previously ZC3HDC5, ZC3H5 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0B0](https://www.uniprot.org/uniprotkb/Q9C0B0) (RING finger protein unkempt homolog):

> Sequence-specific RNA-binding protein which plays an important role in the establishment and maintenance of the early morphology of cortical neurons during embryonic development. Acts as a translation repressor and controls a translationally regulated cell morphology program to ensure proper structuring of the nervous system. Translational control depends on recognition of its binding element within target mRNAs which consists of a mandatory UAG trimer upstream of a U/A-rich motif. Associated …

**Summary**, from NCBI Gene [85451](https://www.ncbi.nlm.nih.gov/gene/85451):

> Enables mRNA CDS binding activity. Involved in cell morphogenesis involved in neuron differentiation and negative regulation of cytoplasmic translation. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29369) · Entrez [85451](https://www.ncbi.nlm.nih.gov/gene/85451) · UniProt [Q9C0B0](https://www.uniprot.org/uniprotkb/Q9C0B0) · Ensembl [ENSG00000132478](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132478)

## Data

Gene col 5328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5328); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5328]; `tensor/DDL_lfc|DDL_z.npy` [5328]; `embed/gene_vectors.npy` [5328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5328 or target_col == 5328). Every well: [[UNK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
