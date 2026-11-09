---
symbol: "RELB"
type: "gene"
col: 2507
ensembl_id: "ENSG00000104856"
name: "RELB proto-oncogene, NF-kB subunit"
location: "19q13.32"
module: 14
arm: "+"
pooled_cpm: 66.59
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RELB

*RELB proto-oncogene, NF-kB subunit* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.01× (z +52.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.397× (z -18.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGIF2]] (+0.66, fdr 7e-06), [[BRAF]] (+0.64, fdr 1e-05), [[NFKB2]] (+0.63, fdr 7e-06); moves opposite to [[AHSA1]] (-0.67, fdr 7e-06), [[ATP2C1]] (-0.65, fdr 1e-05), [[NAPB]] (-0.59, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.01×** | +52.0 | 0e+00 | 48/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.38×** | +29.1 | 0e+00 | 47/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.40×** | +18.0 | 0e+00 | 43/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +14.7 | 0e+00 | 41/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +12.6 | 3e-34 | 41/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.00×** | +11.8 | 5e-30 | 46/49 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +10.7 | 1e-24 | 40/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +7.8 | 3e-13 | 32/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 2e-04 | 23/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.011 | 18/48 (RPMI-7951, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.011 | 17/48 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.17× | +3.3 | 0.044 | 17/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.397×** | -18.9 | 0e+00 | 44/48 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.427×** | -16.7 | 0e+00 | 33/43 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.477×** | -15.1 | 0e+00 | 43/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -13.7 | 9e-41 | 39/49 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.579×** | -11.2 | 8e-27 | 39/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.581×** | -11.1 | 1e-26 | 43/48 (RPMI-7951, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.586×** | -10.9 | 9e-26 | 37/49 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.692×** | -10.6 | 2e-24 | 35/48 (HS-578T, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[NG25 (drug)]] 5 µM |  | **0.393×** | -10.0 | 1e-21 | 44/47 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.711×** | -9.8 | 5e-21 | 33/48 (Hs 766T, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.632×** | -9.4 | 4e-19 | 40/48 (NCI-H1573, A-427, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.641×** | -9.1 | 5e-18 | 39/48 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -8.4 | 2e-15 | 32/50 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.679×** | -7.9 | 1e-13 | 34/48 (COLO 205, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.678×** | -7.5 | 3e-12 | 30/48 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.713×** | -6.9 | 2e-10 | 34/49 (NCI-H1792, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.529×** | -6.8 | 3e-10 | 38/49 (HS-578T, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.7 | 5e-07 | 27/48 (NCI-H23, A498, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -5.1 | 8e-06 | 26/48 (NCI-H661, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 190 | 7 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +31.1) | [[Auranofin (drug)]] 5 µM 0.291× (z -13.2) |
| [[PANC-1 (line)]] | alt | 64.6 | 4 | 12 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +30.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -14.5) |
| [[HS-578T (line)]] | alt | 102 | 3 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +27.0) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -15.4) |
| [[A549 (line)]] | wt | 138 | 4 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +37.2) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.366× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 101 | 6 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +36.8) | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.385× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 43.6 | 11 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +39.9) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 103 | 3 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +22.3) | [[Auranofin (drug)]] 5 µM 0.259× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 73.8 | 2 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.357× (z -10.4) |
| [[A-427 (line)]] | wt | 59.1 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.424× (z -8.9) |
| [[A498 (line)]] | wt | 62.2 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +31.3) | [[Selinexor (drug)]] 5 µM 0.540× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 82.0 | 3 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +20.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.476× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 85.5 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 66.0 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.320× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.351× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 74.8 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.5) | [[Belinostat (drug)]] 5 µM 0.230× (z -14.9) |
| [[SNU-423 (line)]] | alt | 65.6 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +23.0) | [[Auranofin (drug)]] 5 µM 0.252× (z -12.0) |
| [[SW 900 (line)]] | alt | 74.3 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +30.3) | [[Auranofin (drug)]] 5 µM 0.308× (z -11.8) |
| [[A-172 (line)]] | wt | 46.7 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +32.7) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.539× (z -8.6) |
| [[BT-474 (line)]] | alt | 57.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.77× (z +24.4) | — |
| [[LoVo (line)]] | wt | 49.8 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +26.4) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.391× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 54.6 | 5 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +35.1) | [[Auranofin (drug)]] 5 µM 0.383× (z -10.9) |
| [[SW480 (line)]] | alt | 40.6 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +22.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 57.2 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +23.1) | [[Belinostat (drug)]] 5 µM 0.345× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 82.8 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +22.6) | [[Auranofin (drug)]] 5 µM 0.264× (z -13.0) |
| [[SW48 (line)]] | wt | 70.5 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +21.8) | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.224× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 63.9 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +21.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -8.9) |
| [[C32 (line)]] | wt | 29.3 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +20.0) | [[Auranofin (drug)]] 5 µM 0.248× (z -8.9) |
| [[Hs 766T (line)]] | wt | 56.0 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +25.0) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.372× (z -12.9) |
| [[KATO III (line)]] | alt | 26.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.16× (z +20.6) | — |
| [[LS 180 (line)]] | wt | 24.4 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 88.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +17.4) | — |
| [[NCI-H2030 (line)]] | alt | 66.6 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +23.9) | [[Belinostat (drug)]] 5 µM 0.430× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 82.8 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +27.3) | [[Auranofin (drug)]] 5 µM 0.229× (z -14.5) |
| [[SW1417 (line)]] | alt | 76.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.69× (z +28.3) | — |
| [[CFPAC-1 (line)]] | alt | 55.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +29.2) | [[Selinexor (drug)]] 5 µM 0.533× (z -8.7) |
| [[COLO 205 (line)]] | alt | 44.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +10.9) | [[Selinexor (drug)]] 5 µM 0.303× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 49.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +18.7) | — |
| [[NCI-H1792 (line)]] | alt | 64.6 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 5.29× (z +15.2) | [[Selinexor (drug)]] 5 µM 0.519× (z -8.8) |
| [[RKO (line)]] | wt | 54.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -14.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 36.2 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +17.6) | [[Auranofin (drug)]] 5 µM 0.239× (z -8.7) |
| [[AN3 CA (line)]] | alt | 70.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +12.7) | — |
| [[H4 (line)]] | wt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +15.7) | — |
| [[J82 (line)]] | alt | 54.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +27.7) | — |
| [[NCI-H596 (line)]] | alt | 62.5 | 2 (1 ⚠) | 0 | [[Pentoxifylline (drug)]] 0.05 µM 3.30× (z +15.7) ⚠ transcription drop · without an alert: [[Citalopram (hydrobromide) (drug)]] 0.05 µM 2.72× (z +13.1) | — |
| [[SW 1271 (line)]] | alt | 80.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +8.5) | [[Thymol (drug)]] 0.5 µM 0.0732× (z -11.0) |
| [[C-33 A (line)]] | alt | 41.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +11.8) | — |
| [[CHP-212 (line)]] | wt | 65.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +13.4) | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0607× (z -8.6) |
| [[NCI-H2122 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGIF2]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[BRAF]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[NFKB2]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[BCL3]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 959 |
| [[TEF]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[SLC2A6]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CX3CL1]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NFKB1]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[MARCKS]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[POGZ]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[HIVEP1]] | +0.60 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ZNFX1]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.67 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[ATP2C1]] | -0.65 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[NAPB]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[GRB2]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CNIH1]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CACYBP]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SNX3]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[MTPN]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[GFM2]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[VDAC2]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[RNF216P1]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[VIPAS39]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RELB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYNPO]] | B | SYNPO activity raises RELB's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without SYNPO | 0.057 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 6.7); signed map (43.0, 6.1). **Vector** length 131, 43.5% of its response variance represented; |z| ≥ 3 in 1,568 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IkBA variant leads to EDA-ID* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +13.7 | +29.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +13.3 | +52.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +18.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +4.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.4 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +3.7 |
|  | [[Resveratrol (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +0.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.0 | -18.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.5 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.9 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -5.1 |
|  | [[NG25 (drug)]] 5 µM |  | -6.0 | -10.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | RELB proto-oncogene, NF-kB subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,001,461-45,038,192 (+) |
| Ensembl biotype | protein_coding |
| Also known as | REL-B |
| Gene groups (HGNC) | NF-kappa B complex subunits; IPT domain containing |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: CD209 (DC-SIGN) signaling; NIK-->noncanonical NF-kB signaling; Dectin-1 mediated noncanonical NF-kB signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01201](https://www.uniprot.org/uniprotkb/Q01201) (Transcription factor RelB):

> NF-kappa-B is a pleiotropic transcription factor which is present in almost all cell types and is involved in many biological processed such as inflammation, immunity, differentiation, cell growth, tumorigenesis and apoptosis. NF-kappa-B is a homo- or heterodimeric complex formed by the Rel-like domain-containing proteins RELA/p65, RELB, NFKB1/p105, NFKB1/p50, REL and NFKB2/p52. The dimers bind at kappa-B sites in the DNA of their target genes and the individual dimers have distinct preferences …

**Summary**, from NCBI Gene [5971](https://www.ncbi.nlm.nih.gov/gene/5971):

> Enables RNA polymerase II cis-regulatory region sequence-specific DNA binding activity and protein kinase binding activity. Involved in lymphocyte differentiation and negative regulation of interferon-beta production. Located in centrosome; chromatin; and nucleoplasm. Part of nucleus and transcription repressor complex. Implicated in breast cancer and immunodeficiency 53. Biomarker of breast cancer and transitional cell carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9956) · Entrez [5971](https://www.ncbi.nlm.nih.gov/gene/5971) · UniProt [Q01201](https://www.uniprot.org/uniprotkb/Q01201) · Ensembl [ENSG00000104856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104856)

## Data

Gene col 2507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2507); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2507]; `tensor/DDL_lfc|DDL_z.npy` [2507]; `embed/gene_vectors.npy` [2507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2507 or target_col == 2507). Every well: [[RELB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RELB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
