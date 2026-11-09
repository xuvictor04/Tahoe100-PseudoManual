---
symbol: "EFL1"
type: "gene"
col: 6436
ensembl_id: "ENSG00000140598"
name: "elongation factor like GTPase 1"
location: "15q25.2"
module: 84
arm: "+"
pooled_cpm: 89.38
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 33
n_dd_up_clean: 9
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# EFL1

*elongation factor like GTPase 1* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.51× (z +8.0, q 1e-12, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.495× (z -19.1, q 0e+00, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO2B]] (+0.68, fdr 7e-06), [[ITGA2]] (+0.67, fdr 7e-06), [[LRRC8C]] (+0.67, fdr 7e-06); moves opposite to [[C1RL]] (-0.55, fdr 1e-04), [[FOXG1]] (-0.55, fdr 3e-04), [[RAF1]] (-0.55, fdr 4e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TMEM158]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +8.0 | 1e-12 | 28/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +5.7 | 4e-06 | 24/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.6 | 5e-06 | 24/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +5.3 | 1e-05 | 27/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 2e-05 | 28/48 (COLO 205, KATO III, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +4.8 | 2e-04 | 31/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.60×** | +4.5 | 7e-04 | 26/48 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +4.4 | 7e-04 | 25/47 (SW 900, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.4 | 7e-04 | 20/49 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.002 | 19/48 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.005 | 5/48 (Panc 03.27, A549, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.018 | 24/49 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.18× | +3.3 | 0.047 | 21/48 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.093 | 12/49 (BT-474, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.495×** | -19.1 | 0e+00 | 43/49 (RKO, A549, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -14.2 | 3e-43 | 46/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.503×** | -13.2 | 9e-38 | 43/49 (RKO, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.502×** | -12.8 | 3e-35 | 37/44 (HCT15, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -11.1 | 2e-26 | 40/47 (MIA PaCa-2, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -10.4 | 4e-23 | 42/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -9.4 | 5e-19 | 37/50 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -9.1 | 8e-18 | 38/48 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -8.9 | 5e-17 | 31/47 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.635×** | -8.1 | 3e-14 | 29/45 (RPMI-7951, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -7.8 | 3e-13 | 34/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -7.5 | 4e-12 | 34/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.691×** | -7.1 | 5e-11 | 32/49 (RKO, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.760×** | -6.5 | 3e-09 | 30/48 (RKO, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -5.9 | 2e-07 | 31/48 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.767×** | -5.6 | 9e-07 | 27/49 (RKO, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.743×** | -5.4 | 2e-06 | 29/48 (RKO, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.774×** | -4.5 | 2e-04 | 23/48 (RKO, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.825×** | -4.3 | 5e-04 | 24/48 (RKO, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.800×** | -4.3 | 5e-04 | 26/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.797×** | -4.2 | 7e-04 | 24/48 (RKO, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 347 | 0 | 21 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -27.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -26.9) |
| [[C32 (line)]] | wt | 88.2 | 0 | 15 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -11.4) |
| [[HOP62 (line)]] | alt | 137 | 0 | 12 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -21.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 93.8 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -12.1) |
| [[SW480 (line)]] | alt | 71.0 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -15.4) |
| [[A-172 (line)]] | wt | 113 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -15.5) |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 77.4 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -18.0) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 162 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.336× (z -10.4) |
| [[HS-578T (line)]] | alt | 104 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 59.1 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.33× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.408× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 85.8 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -15.8) |
| [[PANC-1 (line)]] | alt | 69.8 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -18.1) |
| [[J82 (line)]] | alt | 128 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.394× (z -10.7) |
| [[H4 (line)]] | wt | 83.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.262× (z -9.2) |
| [[SNU-423 (line)]] | alt | 72.6 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -15.7) |
| [[SW1417 (line)]] | alt | 58.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -15.9) |
| [[A549 (line)]] | wt | 237 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -19.5) |
| [[CFPAC-1 (line)]] | alt | 58.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 80.9 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 63.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -10.5) |
| [[LS 180 (line)]] | wt | 69.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 92.3 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.625× (z -13.6) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 79.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 93.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.6) |
| [[SW 900 (line)]] | alt | 78.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -11.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.7) |
| [[SW48 (line)]] | wt | 74.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -11.0) |
| [[COLO 205 (line)]] | alt | 74.3 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.00× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 92.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0499× (z -26.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 80.6 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0719× (z -17.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -13.0) |
| [[HT-29 (line)]] | alt | 74.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -10.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 60.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -10.1) |
| [[A-427 (line)]] | wt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 38.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -10.9) |
| [[BT-474 (line)]] | alt | 75.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 40.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -8.8) |
| [[AN3 CA (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO2B]] | +0.68 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[CSGALNACT2]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.66 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[STX1A]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[C13orf46]] | +0.64 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TUBB6]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[S100A16]] | +0.63 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[RASA3]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ENTPD7]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1RL]] | -0.55 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[FOXG1]] | -0.55 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[RAF1]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PON2]] | -0.54 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[RHOBTB3]] | -0.53 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[DYRK1A]] | -0.53 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[GTF2I]] | -0.52 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[NFIA]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[STOM]] | -0.51 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[HOTAIR]] | -0.51 | -0.40 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM158]] | B | TMEM158 activity raises EFL1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without TMEM158 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[ITPR1]] | B | ITPR1 activity raises EFL1's level | lines that do not express ITPR1 (15) vs lines expressing it (35) | 1.34× lower at baseline in the lines without ITPR1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, CCDC169, SPART; maybe low, not absent |
| [[BCL2A1]] | B | BCL2A1 activity raises EFL1's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.38× lower at baseline in the lines without BCL2A1 | 0.033 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[INSYN2B]] | B | INSYN2B activity raises EFL1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 1.44× lower at baseline in the lines without INSYN2B | 0.035 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[STC1]] | B | STC1 activity raises EFL1's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without STC1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[STAC]] | B | STAC activity raises EFL1's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.22× lower at baseline in the lines without STAC | 0.051 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[TM4SF19]] | B | TM4SF19 activity raises EFL1's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without TM4SF19 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[C13orf46]] | B | C13orf46 activity raises EFL1's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without C13orf46 | 0.064 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[KCNMA1]] | B | KCNMA1 activity raises EFL1's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 1.21× lower at baseline in the lines without KCNMA1 | 0.081 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ARHGAP22]] | B | ARHGAP22 activity strengthens EFL1's drug response | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | the lines without ARHGAP22 respond 0.75× as strongly (z diff +1.51); strongest at Idarubicin (hydrochloride) 5 µM: 0.64x vs 0.44x (z diff +3.0) | 0.089 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2; artifact flags |
| [[KCNC4]] | B | KCNC4 activity strengthens EFL1's drug response | lines that do not express KCNC4 (6) vs lines expressing it (44) | the lines without KCNC4 respond 0.54× as strongly (z diff +2.19); strongest at Idarubicin (hydrochloride) 5 µM: 0.71x vs 0.49x (z diff +4.0) | 0.090 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent; artifact flags |
| [[LINC01812]] | B | LINC01812 activity raises EFL1's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 1.42× lower at baseline in the lines without LINC01812 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.9, 2.3); signed map (2.0, 48.1). **Vector** length 140, 48.5% of its response variance represented; |z| ≥ 3 in 1,779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.4 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.4 | +8.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.3 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.2 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.0 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +5.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.2 | +2.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.4 | -14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -8.1 | -10.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.7 | -6.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.7 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.5 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.2 | -4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | elongation factor like GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,130,206-82,262,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13119, FAM42A, HsT19294, RIA1; previously EFTUD1 |
| Gene groups (HGNC) | Ribosome biogenesis factors; Translational GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2Z2](https://www.uniprot.org/uniprotkb/Q7Z2Z2) (Elongation factor-like GTPase 1):

> GTPase involved in the biogenesis of the 60S ribosomal subunit and translational activation of ribosomes. Together with SBDS, triggers the GTP-dependent release of EIF6 from 60S pre-ribosomes in the cytoplasm, thereby activating ribosomes for translation competence by allowing 80S ribosome assembly and facilitating EIF6 recycling to the nucleus, where it is required for 60S rRNA processing and nuclear export.

**Summary**, from NCBI Gene [79631](https://www.ncbi.nlm.nih.gov/gene/79631):

> Enables GTPase activity and ribosome binding activity. Involved in GTP metabolic process and cytosolic ribosome assembly. Predicted to be part of ribonucleoprotein complex. Predicted to be active in cytosol. Implicated in Shwachman-Diamond syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25789) · Entrez [79631](https://www.ncbi.nlm.nih.gov/gene/79631) · UniProt [Q7Z2Z2](https://www.uniprot.org/uniprotkb/Q7Z2Z2) · Ensembl [ENSG00000140598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140598)

## Data

Gene col 6436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6436); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6436]; `tensor/DDL_lfc|DDL_z.npy` [6436]; `embed/gene_vectors.npy` [6436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6436 or target_col == 6436). Every well: [[EFL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
