---
symbol: "ZC3H6"
type: "gene"
col: 11983
ensembl_id: "ENSG00000188177"
name: "zinc finger CCCH-type containing 6"
location: "2q14.1"
module: 28
arm: "+"
pooled_cpm: 80.96
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 31
n_dd_up_clean: 14
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ZC3H6

*zinc finger CCCH-type containing 6* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.79× (z +32.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.394× (z -20.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD26]] (+0.77, fdr 7e-06), [[NFYB]] (+0.75, fdr 7e-06), [[HHLA3]] (+0.75, fdr 7e-06); moves opposite to [[ATG16L1]] (-0.66, fdr 1e-05), [[NAPG]] (-0.66, fdr 7e-06), [[GTF2E2]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +32.1 | 0e+00 | 46/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +16.8 | 0e+00 | 45/48 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +16.1 | 0e+00 | 45/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.84×** | +13.5 | 2e-39 | 43/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +12.5 | 9e-34 | 43/48 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.4 | 2e-23 | 34/49 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +9.4 | 4e-19 | 35/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +8.2 | 2e-14 | 35/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +8.1 | 4e-14 | 38/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.6 | 2e-12 | 31/50 (HT-29, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +6.6 | 2e-09 | 29/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 2e-06 | 30/48 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +5.4 | 3e-06 | 16/48 (RKO, SHP-77, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +5.2 | 7e-06 | 19/48 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +4.8 | 6e-05 | 22/49 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +3.8 | 0.005 | 12/49 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.394×** | -20.6 | 0e+00 | 48/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.419×** | -19.2 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.479×** | -16.2 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.258×** | -15.7 | 0e+00 | 46/49 (PANC-1, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.495×** | -15.5 | 0e+00 | 43/48 (PANC-1, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.270×** | -15.1 | 0e+00 | 47/48 (HS-578T, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.504×** | -15.1 | 0e+00 | 46/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.507×** | -15.0 | 0e+00 | 39/48 (PANC-1, LoVo, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.509×** | -14.9 | 0e+00 | 45/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.519×** | -14.4 | 1e-45 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.520×** | -13.6 | 2e-40 | 43/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.560×** | -11.8 | 2e-30 | 35/43 (NCI-H23, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.577×** | -11.6 | 1e-29 | 32/43 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -11.3 | 6e-28 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.621×** | -10.1 | 2e-22 | 34/47 (AN3 CA, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.648×** | -9.0 | 5e-18 | 33/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -8.9 | 1e-17 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.695×** | -8.0 | 3e-14 | 37/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.782×** | -7.7 | 4e-13 | 30/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.721×** | -7.2 | 1e-11 | 28/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.772×** | -5.7 | 2e-07 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.621×** | -5.5 | 8e-07 | 27/48 (HT-29, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 89.1 | 5 | 20 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +23.9) | [[Digitoxin (drug)]] 0.5 µM 0.238× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 98.9 | 4 | 20 (11 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +16.2) | [[Ixazomib citrate (drug)]] 5 µM 0.303× (z -16.6) |
| [[PANC-1 (line)]] | alt | 137 | 2 | 21 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.5) | [[Ixazomib citrate (drug)]] 5 µM 0.185× (z -22.8) |
| [[A498 (line)]] | wt | 86.6 | 6 | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.126× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 107 | 1 | 13 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +17.7) | [[Belinostat (drug)]] 5 µM 0.267× (z -13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.267× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 108 | 2 | 11 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +16.5) | [[Ixazomib citrate (drug)]] 5 µM 0.332× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 108 | 2 | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +18.7) | [[Belinostat (drug)]] 5 µM 0.365× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.424× (z -10.2) |
| [[SNU-423 (line)]] | alt | 89.3 | 1 | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.9) | [[Ixazomib citrate (drug)]] 5 µM 0.364× (z -11.7) |
| [[C32 (line)]] | wt | 106 | 3 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.5) | [[Auranofin (drug)]] 5 µM 0.248× (z -13.3) |
| [[HOP62 (line)]] | alt | 99.6 | 1 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -11.5) |
| [[HCT15 (line)]] | alt | 122 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.249× (z -12.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.261× (z -12.3) |
| [[Hs 766T (line)]] | wt | 106 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.9) | [[Ixazomib citrate (drug)]] 5 µM 0.320× (z -12.8) |
| [[HS-578T (line)]] | alt | 66.1 | 7 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +21.0) | [[PH-797804 (drug)]] 5 µM 0.121× (z -12.5) |
| [[LoVo (line)]] | wt | 77.7 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.338× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 84.3 | 0 | 8 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.266× (z -14.5) |
| [[A-172 (line)]] | wt | 82.4 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.0) | [[TAK-901 (drug)]] 5 µM 0.160× (z -11.0) |
| [[HT-29 (line)]] | alt | 54.5 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.4) | [[Ixazomib citrate (drug)]] 5 µM 0.232× (z -13.3) |
| [[J82 (line)]] | alt | 53.5 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.6) | [[Digitoxin (drug)]] 0.5 µM 0.307× (z -11.5) |
| [[SW1417 (line)]] | alt | 68.3 | 2 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.0) | [[Bortezomib (drug)]] 0.05 µM 0.269× (z -11.9) |
| [[A-427 (line)]] | wt | 72.1 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[H4 (line)]] | wt | 110 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.284× (z -12.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.112× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 82.6 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.1) | [[Belinostat (drug)]] 5 µM 0.290× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 72.6 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +21.1) | [[Belinostat (drug)]] 5 µM 0.248× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.283× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 72.9 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.376× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 91.9 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.6) | [[Auranofin (drug)]] 5 µM 0.294× (z -12.7) |
| [[LS 180 (line)]] | wt | 82.6 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.389× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 112 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +18.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0540× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 58.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.362× (z -9.6) |
| [[COLO 205 (line)]] | alt | 47.3 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +19.6) | [[Digitoxin (drug)]] 0.5 µM 0.179× (z -11.5) |
| [[KATO III (line)]] | alt | 56.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H2347 (line)]] | alt | 23.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +17.8) | — |
| [[RKO (line)]] | wt | 38.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +20.2) | — |
| [[SW 900 (line)]] | alt | 100 | 0 | 4 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.141× (z -10.6) |
| [[AN3 CA (line)]] | alt | 106 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.149× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.213× (z -9.7) |
| [[C-33 A (line)]] | alt | 62.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 79.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.2) | [[Auranofin (drug)]] 5 µM 0.294× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 106 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.2) | [[PH-797804 (drug)]] 5 µM 0.207× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 46.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 37.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +19.4) | — |
| [[CFPAC-1 (line)]] | alt | 24.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +15.4) | — |
| [[HepG2_C3A (line)]] | wt | 56.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.173× (z -11.1) |
| [[NCI-H596 (line)]] | alt | 82.1 | 1 | 1 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 3.64× (z +13.5) | [[Atazanavir (sulfate) (drug)]] 5 µM 0.437× (z -8.7) |
| [[SHP-77 (line)]] | alt | 65.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.297× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 63.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 76.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +10.7) | — |
| [[NCI-H2122 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 163 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD26]] | +0.77 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[NFYB]] | +0.75 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.75 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[GATAD1]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[RSF1]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[APLF]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[TRMT1L]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.70 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[ZNF638]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[HMGCL]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[CEP350]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[THAP1]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG16L1]] | -0.66 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[NAPG]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[GTF2E2]] | -0.64 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[USB1]] | -0.64 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[RAB5C]] | -0.63 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[HSF1]] | -0.63 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[TPST2]] | -0.63 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[POLR3H]] | -0.63 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.62 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[LRFN3]] | -0.62 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[SNRPD3]] | -0.62 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[HDAC1]] | -0.61 | -0.64 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZC3H6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.8, 6.6); signed map (6.5, -15.9). **Vector** length 156, 57.3% of its response variance represented; |z| ≥ 3 in 1,900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +16.0 | +32.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +14.7 | +16.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +14.4 | +16.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +14.3 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +11.0 | +13.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.5 | +8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +8.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.4 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +6.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -11.5 | -20.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -10.4 | -14.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -9.9 | -19.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -9.1 | -15.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.8 | -15.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.7 | -14.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.3 | -15.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.1 | -9.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,275,597-112,340,059 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41410, FLJ45877, KIAA2035; previously ZC3HDC6 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Matched by | ensembl_id |

UniProt [P61129](https://www.uniprot.org/uniprotkb/P61129) carries no function annotation.

**Summary**, from NCBI Gene [376940](https://www.ncbi.nlm.nih.gov/gene/376940):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific. Predicted to be involved in negative regulation of DNA-templated transcription, elongation. Predicted to be located in chromatin. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24762) · Entrez [376940](https://www.ncbi.nlm.nih.gov/gene/376940) · UniProt [P61129](https://www.uniprot.org/uniprotkb/P61129) · Ensembl [ENSG00000188177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188177)

## Data

Gene col 11983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11983); `tables/drug_effects.parquet` (79 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11983]; `tensor/DDL_lfc|DDL_z.npy` [11983]; `embed/gene_vectors.npy` [11983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11983 or target_col == 11983). Every well: [[ZC3H6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
