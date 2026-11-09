---
symbol: "ZFAND3"
type: "gene"
col: 8001
ensembl_id: "ENSG00000156639"
name: "zinc finger AN1-type containing 3"
location: "6p21.2"
module: 211
arm: "+"
pooled_cpm: 619.65
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# ZFAND3

*zinc finger AN1-type containing 3* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.50× (z +17.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.322× (z -20.7, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.691× (z -10.0, q 4e-21, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK3]] (+0.61, fdr 1e-05), [[GSK3B]] (+0.60, fdr 7e-06), [[PTK2]] (+0.52, fdr 1e-05); moves opposite to [[PRPF38A]] (-0.43, fdr 1e-04), [[MTR]] (-0.43, fdr 1e-04), [[TXNL4B]] (-0.42, fdr 2e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LARGE1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.50×** | +17.3 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +13.7 | 3e-40 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +12.9 | 5e-36 | 38/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.22×** | +12.7 | 6e-35 | 49/49 (SW480, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.85×** | +11.6 | 4e-29 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +11.4 | 5e-28 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +10.3 | 4e-23 | 37/48 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +9.4 | 5e-19 | 42/47 (Hs 766T, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.74×** | +8.9 | 3e-17 | 47/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +6.2 | 3e-08 | 40/48 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.2 | 4e-08 | 41/48 (C32, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +5.9 | 2e-07 | 42/48 (SW480, HCT15, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +4.8 | 8e-05 | 32/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 1e-04 | 32/48 (C32, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.005 | 27/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.4 | 0.022 | 22/48 (LoVo, KATO III, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.027 | 14/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.044 | 13/48 (SW48, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8001.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.322×** | -20.7 | 0e+00 | 44/44 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.356×** | -19.6 | 0e+00 | 48/49 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -10.0 | 4e-21 | 36/49 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -9.2 | 4e-18 | 43/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.687×** | -6.6 | 4e-09 | 33/45 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.711×** | -6.5 | 7e-09 | 43/48 (SW 1271, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.822×** | -5.3 | 9e-06 | 28/48 (SW480, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.798×** | -4.3 | 0.001 | 25/48 (NCI-H23, J82, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -4.1 | 0.003 | 28/48 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.824×** | -3.7 | 0.012 | 24/48 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 908 | 8 (2 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -26.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 662 | 10 (3 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -15.8) |
| [[A549 (line)]] | wt | 449 | 9 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +26.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -23.6) |
| [[BT-474 (line)]] | alt | 753 | 9 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 381 | 13 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.53× (z +25.0) | — |
| [[A-172 (line)]] | wt | 448 | 9 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +21.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -18.5) |
| [[J82 (line)]] | alt | 578 | 6 (2 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 408 | 9 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -19.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 835 | 7 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -13.0) |
| [[SW 900 (line)]] | alt | 523 | 8 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -10.5) |
| [[H4 (line)]] | wt | 567 | 9 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -16.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 796 | 7 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -10.1) |
| [[HS-578T (line)]] | alt | 785 | 7 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -12.7) |
| [[SW480 (line)]] | alt | 485 | 8 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -17.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 565 | 8 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +19.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 761 | 5 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 821 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -13.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 352 | 7 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.450× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 568 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -13.3) |
| [[C32 (line)]] | wt | 509 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -10.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 509 | 5 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.45× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 769 | 3 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 895 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -22.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 649 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -21.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 667 | 2 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -17.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 584 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +17.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -13.1) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 783 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -15.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 617 | 3 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -14.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 657 | 2 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -15.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 660 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 600 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -19.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 328 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.58× (z +13.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.95× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 504 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -12.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 611 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +10.2) | [[Docetaxel (drug)]] 0.05 µM 0.255× (z -12.5) ⚠ transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HCT15 (line)]] | alt | 605 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -15.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 447 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 1,009 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 1,286 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.478× (z -9.1) |
| [[RKO (line)]] | wt | 780 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.83× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -19.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 483 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -14.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 1,023 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.63× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -10.0) |
| [[KATO III (line)]] | alt | 677 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -16.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 313 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +16.2) | — |
| [[SK-MEL-2 (line)]] | alt | 670 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.26× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.6) |
| [[CHP-212 (line)]] | wt | 475 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.1) |
| [[LoVo (line)]] | wt | 661 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.24× (z +10.6) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.296× (z -16.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 661 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 578 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 650 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 469 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK3]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[GSK3B]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PTK2]] | +0.52 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[RABGAP1L]] | +0.50 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[EXOC6B]] | +0.50 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[KPNA1]] | +0.49 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[DENND5A]] | +0.48 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[XPR1]] | +0.48 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[EIF4G3]] | +0.47 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[LRRFIP2]] | +0.47 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[KIAA0232]] | +0.46 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[CLEC16A]] | +0.46 | +0.31 / +0.38 | both halves | 2e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF38A]] | -0.43 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[MTR]] | -0.43 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[TXNL4B]] | -0.42 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ZNF550]] | -0.42 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[NUP133]] | -0.42 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[CEP44]] | -0.41 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[PUS10]] | -0.40 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[GPATCH1]] | -0.40 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[COG4]] | -0.40 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[AASDH]] | -0.40 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[BCKDHA]] | -0.40 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[ZNF395]] | -0.39 | -0.41 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LARGE1]] | B | LARGE1 activity lowers ZFAND3's level | lines that do not express LARGE1 (9) vs lines expressing it (41) | 1.32× higher at baseline in the lines without LARGE1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000249141; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.5, -47.5); signed map (-17.1, 31.0). **Vector** length 93.8, 47.2% of its response variance represented; |z| ≥ 3 in 1,574 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.8 | +9.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | -0.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -9.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.6 | -3.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger AN1-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:37,819,727-38,154,624 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13222; previously TEX27 |
| Gene groups (HGNC) | Zinc fingers AN1-type; Zinc fingers A20-type |
| Matched by | ensembl_id |

UniProt [Q9H8U3](https://www.uniprot.org/uniprotkb/Q9H8U3) carries no function annotation.

**Summary**, from NCBI Gene [60685](https://www.ncbi.nlm.nih.gov/gene/60685):

> Predicted to enable DNA binding activity and zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18019) · Entrez [60685](https://www.ncbi.nlm.nih.gov/gene/60685) · UniProt [Q9H8U3](https://www.uniprot.org/uniprotkb/Q9H8U3) · Ensembl [ENSG00000156639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156639)

## Data

Gene col 8001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8001); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8001]; `tensor/DDL_lfc|DDL_z.npy` [8001]; `embed/gene_vectors.npy` [8001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8001 or target_col == 8001). Every well: [[ZFAND3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAND3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
