---
symbol: "ZNFX1"
type: "gene"
col: 4497
ensembl_id: "ENSG00000124201"
name: "zinc finger NFX1-type containing 1"
location: "20q13.13"
module: 32
arm: "+"
pooled_cpm: 171.18
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 25
n_dd_up_clean: 21
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 34
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ZNFX1

*zinc finger NFX1-type containing 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.96× (z +12.0, q 3e-30, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.374× (z -18.2, q 0e+00, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.471× (z -13.9, q 6e-42, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT3]] (+0.87, fdr 7e-06), [[PARP9]] (+0.86, fdr 7e-06), [[IFI35]] (+0.86, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 34 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +12.0 | 3e-30 | 35/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +11.6 | 8e-29 | 41/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +9.7 | 4e-20 | 35/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +9.6 | 1e-19 | 38/49 (NCI-H460, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +9.4 | 6e-19 | 35/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +8.7 | 3e-16 | 30/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.6 | 4e-09 | 33/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +6.5 | 6e-09 | 32/48 (LS 180, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 1e-07 | 37/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 7e-05 | 27/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 2e-04 | 26/48 (A-427, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 2e-04 | 27/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.4 | 4e-04 | 0/50 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +4.4 | 5e-04 | 26/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.18× | +4.3 | 7e-04 | 19/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.001 | 24/49 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.003 | 25/50 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.374×** | -18.2 | 0e+00 | 43/49 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -17.0 | 0e+00 | 39/44 (A549, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.471×** | -13.9 | 6e-42 | 46/48 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.468×** | -13.0 | 2e-36 | 38/45 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.562×** | -10.7 | 2e-24 | 39/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.574×** | -10.3 | 8e-23 | 41/48 (A549, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.681×** | -10.1 | 7e-22 | 30/49 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.591×** | -9.8 | 1e-20 | 39/48 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.625×** | -8.7 | 2e-16 | 36/49 (RPMI-7951, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.621×** | -8.5 | 1e-15 | 33/47 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.633×** | -8.5 | 1e-15 | 38/48 (A549, C-33 A, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.636×** | -8.4 | 2e-15 | 33/48 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.746×** | -7.7 | 6e-13 | 31/49 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.774×** | -6.7 | 8e-10 | 29/48 (HS-578T, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.730×** | -5.8 | 2e-07 | 29/49 (C-33 A, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.750×** | -5.3 | 3e-06 | 30/48 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.584×** | -5.2 | 6e-06 | 28/48 (C-33 A, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **0.608×** | -4.8 | 5e-05 | 33/48 (BT-474, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.653×** | -4.1 | 0.001 | 27/49 (A549, C-33 A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 322 | 0 | 21 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -14.8) |
| [[MIA PaCa-2 (line)]] | alt | 237 | 3 | 14 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 180 | 13 (3 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +37.1) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.474× (z -9.5) |
| [[A549 (line)]] | wt | 246 | 0 | 15 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0791× (z -29.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.227× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 314 | 0 | 14 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.232× (z -16.5) |
| [[C-33 A (line)]] | alt | 263 | 0 | 13 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.247× (z -16.5) |
| [[SNU-423 (line)]] | alt | 247 | 3 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.311× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 231 | 6 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.348× (z -11.1) |
| [[HS-578T (line)]] | alt | 178 | 5 (1 ⚠) | 7 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.26× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.497× (z -11.3) |
| [[A-172 (line)]] | wt | 261 | 3 | 7 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.58× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.366× (z -10.4) |
| [[LoVo (line)]] | wt | 180 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 305 | 3 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.82× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.349× (z -11.3) |
| [[HOP62 (line)]] | alt | 90.2 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +26.2) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -10.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 88.4 | 8 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.02× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.462× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 194 | 3 | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 6.19× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.461× (z -11.1) |
| [[LS 180 (line)]] | wt | 84.3 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +20.5) | [[Auranofin (drug)]] 5 µM 0.381× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 137 | 4 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.29× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.479× (z -9.8) |
| [[HT-29 (line)]] | alt | 228 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.440× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 139 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.54× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.394× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 137 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +32.1) | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.451× (z -9.1) |
| [[A498 (line)]] | wt | 156 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.524× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 94.0 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 389 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.0730× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.462× (z -8.5) |
| [[SW1417 (line)]] | alt | 312 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.418× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 97.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +18.5) | — |
| [[J82 (line)]] | alt | 303 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 159 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 169 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -8.6) |
| [[H4 (line)]] | wt | 98.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.2) | — |
| [[COLO 205 (line)]] | alt | 227 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.345× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 189 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.471× (z -11.2) |
| [[SNU-1 (line)]] | wt | 194 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0444× (z -29.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.468× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 115 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.7) | — |
| [[SW480 (line)]] | alt | 66.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.2) | — |
| [[C32 (line)]] | wt | 122 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.25× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 79.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.5) | — |
| [[KATO III (line)]] | alt | 122 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 145 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 192 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT3]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 464 |
| [[PARP9]] | +0.86 | +0.80 / +0.88 | both halves | 7e-06 | STRING 635 |
| [[IFI35]] | +0.86 | +0.82 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[IFIH1]] | +0.86 | +0.79 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 644 |
| [[SP110]] | +0.85 | +0.82 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[HELZ2]] | +0.85 | +0.79 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 560 |
| [[RSAD2]] | +0.85 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[RIGI]] | +0.84 | +0.81 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 454 |
| [[OAS1]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 |  |
| [[IFIT1]] | +0.84 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[MX1]] | +0.83 | +0.76 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 617 |
| [[IRF9]] | +0.83 | +0.69 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 27, C 7. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises ZNFX1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without OAS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises ZNFX1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without SAMD9 | 0.012 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[OAS2]] | B | OAS2 activity raises ZNFX1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without OAS2 | 0.021 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[LMO2]] | B | LMO2 activity raises ZNFX1's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without LMO2 | 0.022 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[TRIM34]] | B | TRIM34 activity raises ZNFX1's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without TRIM34 | 0.028 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises ZNFX1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without GBP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[OASL]] | B | OASL activity raises ZNFX1's level | lines that do not express OASL (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without OASL | 0.036 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[ODF3B]] | B | ODF3B activity raises ZNFX1's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without ODF3B | 0.037 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[TYMP]] | B | TYMP activity raises ZNFX1's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without TYMP | 0.039 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[OAS1]] | B | OAS1 activity strengthens ZNFX1's drug response | lines that do not express OAS1 (13) vs lines expressing it (36) | the lines without OAS1 respond 0.60× as strongly (z diff +2.15); strongest at Auranofin 5 µM: 0.75x vs 0.51x (z diff +4.3) | 0.041 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MX1]] | B | MX1 activity raises ZNFX1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.56× lower at baseline in the lines without MX1 | 0.043 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI44]] | B | IFI44 activity raises ZNFX1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.51× lower at baseline in the lines without IFI44 | 0.044 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.876). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 52.8); signed map (65.1, 30.5). **Vector** length 167, 63.6% of its response variance represented; |z| ≥ 3 in 1,775 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.73 to 56); *interferon* (control, mean cos +0.81 to 23); *Interferon Signaling* (reactome, mean cos +0.75 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.7 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +9.0 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +9.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.1 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.2 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.0 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.0 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.5 | +4.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.8 | -6.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -9.7 | -10.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.7 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -10.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.8 | -8.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.7 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger NFX1-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,237,946-49,278,426 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1404, FLJ11277 |
| Gene groups (HGNC) | UPF1 like RNA helicases; Zinc fingers NFX1-type; RING finger E3 ubiquitin protein ligases; Degenerate RING E3 ubiquitin ligases |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2E3](https://www.uniprot.org/uniprotkb/Q9P2E3) (NFX1-type zinc finger-containing protein 1):

> RNA-activated non-canonical E3 ubiquitin ligase required for cell survival during interferon (IFN) responses. Functions as an ATP-dependent 5'-> 3' RNA translocase that selectively recognizes long single-stranded RNA (ssRNA) molecules (>100 nt) from viral or host origin during immune activation. Upon ssRNA binding, oligomerizes to assemble a split E3 active site in trans, involving the Z-RING domain that binds and activates E2-ubiquitin conjugates, such as UBE2D2, and the RZ catalytic domain …

**Summary**, from NCBI Gene [57169](https://www.ncbi.nlm.nih.gov/gene/57169):

> Enables RNA binding activity. Involved in defense response to bacterium and defense response to virus. Is active in cytoplasmic stress granule. Implicated in immunodeficiency 91. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29271) · Entrez [57169](https://www.ncbi.nlm.nih.gov/gene/57169) · UniProt [Q9P2E3](https://www.uniprot.org/uniprotkb/Q9P2E3) · Ensembl [ENSG00000124201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124201)

## Data

Gene col 4497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4497); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4497]; `tensor/DDL_lfc|DDL_z.npy` [4497]; `embed/gene_vectors.npy` [4497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4497 or target_col == 4497). Every well: [[ZNFX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNFX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
