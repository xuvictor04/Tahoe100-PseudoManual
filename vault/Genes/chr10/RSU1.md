---
symbol: "RSU1"
type: "gene"
col: 7290
ensembl_id: "ENSG00000148484"
name: "Ras suppressor protein 1"
location: "10p13"
module: 111
arm: "+"
pooled_cpm: 97.2
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 26
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# RSU1

*Ras suppressor protein 1* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.13× (z +18.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.342× (z -25.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPZB]] (+0.70, fdr 1e-05), [[RPRD1A]] (+0.65, fdr 1e-05), [[STX2]] (+0.63, fdr 2e-05); moves opposite to [[BTN2A1]] (-0.70, fdr 1e-05), [[ZNF563]] (-0.65, fdr 9e-05), [[STAP2]] (-0.65, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[C11orf52]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7290.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.13×** | +18.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.64×** | +16.1 | 0e+00 | 47/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.64×** | +16.0 | 0e+00 | 47/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +10.0 | 1e-21 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +9.0 | 3e-17 | 39/48 (SW1417, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +8.9 | 5e-17 | 33/43 (HCT15, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +7.6 | 2e-12 | 34/49 (SNU-423, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +5.9 | 3e-07 | 43/49 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +4.9 | 6e-05 | 24/45 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.003 | 26/49 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.004 | 27/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.038 | 17/48 (RKO, SW480, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.046 | 14/49 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.342×** | -25.0 | 0e+00 | 48/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.355×** | -17.1 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.390×** | -15.6 | 0e+00 | 46/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.429×** | -13.4 | 6e-39 | 45/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.462×** | -12.7 | 4e-35 | 40/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -11.6 | 3e-29 | 35/49 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -10.3 | 9e-23 | 40/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -9.1 | 4e-18 | 36/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -7.9 | 2e-13 | 33/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.432×** | -7.2 | 2e-11 | 42/49 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -6.1 | 4e-08 | 34/47 (HepG2/C3A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.710×** | -5.7 | 7e-07 | 30/48 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.729×** | -5.2 | 8e-06 | 27/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.552×** | -5.1 | 1e-05 | 31/47 (LOX-IMVI, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.746×** | -4.8 | 5e-05 | 28/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.749×** | -4.8 | 7e-05 | 25/48 (J82, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -4.4 | 3e-04 | 27/48 (AN3 CA, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.802×** | -3.4 | 0.018 | 22/48 (MIA PaCa-2, NCI-H661, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.815×** | -3.4 | 0.021 | 19/48 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.4 | 7 (2 ⚠) | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.63× (z +17.4) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.4) |
| [[J82 (line)]] | alt | 164 | 3 | 10 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -21.5) |
| [[LoVo (line)]] | wt | 87.6 | 4 (1 ⚠) | 6 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -20.3) |
| [[LOX-IMVI (line)]] | wt | 139 | 1 | 9 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -22.4) |
| [[NCI-H23 (line)]] | alt | 147 | 3 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -24.2) |
| [[KATO III (line)]] | alt | 107 | 3 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -19.6) |
| [[NCI-H1573 (line)]] | alt | 70.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -20.7) |
| [[NCI-H1792 (line)]] | alt | 176 | 2 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.255× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.6) |
| [[PANC-1 (line)]] | alt | 156 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -25.2) |
| [[SW1417 (line)]] | alt | 79.3 | 4 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.82× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -15.6) |
| [[SW480 (line)]] | alt | 56.8 | 7 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.32× (z +17.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -12.1) |
| [[A-427 (line)]] | wt | 185 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.6) |
| [[A549 (line)]] | wt | 111 | 3 (1 ⚠) | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.4) |
| [[C32 (line)]] | wt | 115 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -16.7) |
| [[HOP62 (line)]] | alt | 103 | 1 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 150 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.14× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 53.5 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.69× (z +16.5) | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.5) |
| [[SNU-423 (line)]] | alt | 85.5 | 6 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.32× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.6) |
| [[A498 (line)]] | wt | 96.8 | 3 (1 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 2.71× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -22.8) |
| [[BT-474 (line)]] | alt | 61.6 | 1 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 150 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -20.6) |
| [[HT-29 (line)]] | alt | 64.8 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.85× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.185× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -11.3) |
| [[LS 180 (line)]] | wt | 73.8 | 5 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.71× (z +14.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -9.7) |
| [[SHP-77 (line)]] | alt | 54.3 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.211× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -8.9) |
| [[A-172 (line)]] | wt | 78.2 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 3.77× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.8) |
| [[HS-578T (line)]] | alt | 165 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 177 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.14× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 60.5 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +10.1) | [[Harringtonine (drug)]] 5 µM 0.290× (z -10.4) |
| [[SW 900 (line)]] | alt | 73.3 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.41× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 49.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.29× (z +16.3) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.9) |
| [[Hs 766T (line)]] | wt | 74.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.15× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 110 | 1 | 3 | [[Panobinostat (drug)]] 5 µM 3.56× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 51.7 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.86× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -12.2) |
| [[RKO (line)]] | wt | 105 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.71× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.233× (z -12.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.2) |
| [[HCT15 (line)]] | alt | 45.5 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.76× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 92.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 139 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 3.79× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.4) |
| [[AN3 CA (line)]] | alt | 222 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.5) |
| [[H4 (line)]] | wt | 53.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 33.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 60.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -10.1) |
| [[SW48 (line)]] | wt | 118 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.8) |
| [[COLO 205 (line)]] | alt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.2) |
| [[CHP-212 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPZB]] | +0.70 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[RPRD1A]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[STX2]] | +0.63 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[GNB1]] | +0.63 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[MICAL2]] | +0.62 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[NAPG]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[STK25]] | +0.61 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[NOMO1]] | +0.61 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[ATP13A2]] | +0.60 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[CS]] | +0.60 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[RHOA]] | +0.59 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CORO1C]] | +0.59 | +0.47 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A1]] | -0.70 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[ZNF563]] | -0.65 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[STAP2]] | -0.65 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[C3orf38]] | -0.64 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MR1]] | -0.63 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[UNK]] | -0.62 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[ZNF616]] | -0.60 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[N4BP2L1]] | -0.60 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[PBDC1]] | -0.60 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[KIAA1586]] | -0.59 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CREB3L4]] | -0.59 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[ATP23]] | -0.59 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf52]] | B | C11orf52 activity lowers RSU1's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.38× higher at baseline in the lines without C11orf52 | 0.033 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[SATB1]] | B | SATB1 activity lowers RSU1's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.49× higher at baseline in the lines without SATB1 | 0.061 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RSU1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RSU1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[STX2]] | C | STX2 activity raises RSU1's level | lines that do not express STX2 (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without STX2 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NPW, PALS2, CAPRIN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.5, 23.4); signed map (-9.7, 35.9). **Vector** length 120, 41.5% of its response variance represented; |z| ≥ 3 in 1,508 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G-protein beta:gamma signalling* (reactome, mean cos +0.50 to 4); *G beta:gamma signalling through PI3Kgamma* (reactome, mean cos +0.52 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.9 | +16.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.7 | +16.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.3 | +18.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +10.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +9.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | -0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.9 | -11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.2 | -25.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -6.4 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | Ras suppressor protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:16,590,611-16,817,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RSP-1, FLJ31034 |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Regulation of cytoskeletal remodeling and cell spreading by IPP complex components; Cell-extracellular matrix interactions; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15404](https://www.uniprot.org/uniprotkb/Q15404) (Ras suppressor protein 1):

> Potentially plays a role in the Ras signal transduction pathway. Capable of suppressing v-Ras transformation in vitro.

**Summary**, from NCBI Gene [6251](https://www.ncbi.nlm.nih.gov/gene/6251):

> This gene encodes a protein that is involved in the Ras signal transduction pathway, growth inhibition, and nerve-growth factor induced differentiation processes, as determined in mouse and human cell line studies. In mouse, the encoded protein was initially isolated based on its ability to inhibit v-Ras transformation. Multiple alternatively spliced transcript variants for this gene have been reported; one of these variants was found only in glioma tumors. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10464) · Entrez [6251](https://www.ncbi.nlm.nih.gov/gene/6251) · UniProt [Q15404](https://www.uniprot.org/uniprotkb/Q15404) · Ensembl [ENSG00000148484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148484)

## Data

Gene col 7290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7290); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7290]; `tensor/DDL_lfc|DDL_z.npy` [7290]; `embed/gene_vectors.npy` [7290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7290 or target_col == 7290). Every well: [[RSU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
