---
symbol: "ABL2"
type: "gene"
col: 6714
ensembl_id: "ENSG00000143322"
name: "ABL proto-oncogene 2, non-receptor tyrosine kinase"
location: "1q25.2"
module: 120
arm: "+"
pooled_cpm: 367.12
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 15
n_dd_up_clean: 24
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# ABL2

*ABL proto-oncogene 2, non-receptor tyrosine kinase* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.01× (z +24.4, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.352× (z -15.7, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.567× (z -8.9, q 1e-16, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NABP1]] (+0.76, fdr 7e-06), [[CFLAR-AS1]] (+0.66, fdr 1e-05), [[HDAC9]] (+0.65, fdr 9e-06); moves opposite to [[SETD3]] (-0.63, fdr 9e-06), [[RPA1]] (-0.62, fdr 1e-05), [[KDM1A]] (-0.61, fdr 1e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[PDCD1LG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.01×** | +24.4 | 0e+00 | 42/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.87×** | +16.5 | 0e+00 | 44/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.59×** | +14.9 | 0e+00 | 47/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.63×** | +14.1 | 3e-43 | 48/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.42×** | +13.3 | 3e-38 | 42/47 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.10×** | +11.6 | 4e-29 | 46/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.41×** | +10.0 | 9e-22 | 45/47 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.89×** | +9.9 | 2e-21 | 44/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +9.8 | 7e-21 | 43/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +7.4 | 6e-12 | 38/47 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.52×** | +6.3 | 1e-08 | 38/46 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +5.7 | 7e-07 | 32/47 (C32, SW48, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.6 | 9e-07 | 29/47 (A-172, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +5.0 | 2e-05 | 26/48 (HT-29, CHP-212, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.37×** | +4.9 | 3e-05 | 37/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.6 | 1e-04 | 29/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6714.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.352×** | -15.7 | 0e+00 | 43/44 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.409×** | -14.0 | 6e-42 | 44/48 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.567×** | -8.9 | 1e-16 | 41/47 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.584×** | -7.8 | 1e-12 | 35/45 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.642×** | -6.9 | 5e-10 | 35/47 (NCI-H23, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -6.2 | 7e-08 | 30/48 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -6.1 | 1e-07 | 31/47 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.681×** | -6.0 | 1e-07 | 33/47 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.715×** | -5.3 | 9e-06 | 30/47 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -5.1 | 2e-05 | 32/49 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.747×** | -4.6 | 3e-04 | 33/47 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.753×** | -4.4 | 4e-04 | 33/47 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.758×** | -4.3 | 7e-04 | 28/47 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.792×** | -3.6 | 0.011 | 27/47 (J82, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.677×** | -3.2 | 0.053 | 25/47 (Hs 766T, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.866× | -3.2 | 0.053 | 10/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 120 | 15 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +24.2) | — |
| [[NCI-H460 (line)]] | wt | 736 | 12 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.362× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 933 | 5 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -16.9) |
| [[SK-MEL-2 (line)]] | alt | 445 | 13 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -15.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 289 | 11 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 291 | 3 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -17.4) |
| [[A-172 (line)]] | wt | 651 | 5 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +21.3) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -12.5) |
| [[Hs 766T (line)]] | wt | 435 | 7 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +27.3) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.424× (z -8.7) |
| [[RKO (line)]] | wt | 1,435 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -16.2) |
| [[SW480 (line)]] | alt | 144 | 10 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +20.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.9) |
| [[LS 180 (line)]] | wt | 94.3 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 427 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.353× (z -9.9) |
| [[A498 (line)]] | wt | 376 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +25.3) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -10.2) |
| [[HS-578T (line)]] | alt | 201 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +27.4) | — |
| [[LoVo (line)]] | wt | 158 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +37.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 224 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +28.6) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.5) |
| [[PANC-1 (line)]] | alt | 218 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -13.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 455 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 465 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 397 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +25.2) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -10.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 105 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.73× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 477 | 5 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.15× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -8.6) |
| [[A-427 (line)]] | wt | 209 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -20.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 153 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 5.11× (z +16.6) | — |
| [[C32 (line)]] | wt | 298 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +26.2) | — |
| [[CFPAC-1 (line)]] | alt | 392 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -10.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 488 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +20.9) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -11.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 294 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 537 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 252 | 5 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -11.5) |
| [[A549 (line)]] | wt | 402 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -11.6) |
| [[J82 (line)]] | alt | 615 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 394 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 446 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.420× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 226 | 1 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.59× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 107 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 503 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 213 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 276 | 2 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.28× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -10.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 405 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 164 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 177 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.81× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 150 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -16.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 190 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +12.9) | — |
| [[SW 1088 (line)]] | alt | 417 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 88.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 372 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 424 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NABP1]] | +0.76 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[CFLAR-AS1]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[RND3]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 | same gene group; pathway: RAC1 GTPase cycle |
| [[CYTOR]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RASAL2]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ADNP2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZNF281]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[STARD13]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[KBTBD8]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SGK1]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.63 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[RPA1]] | -0.62 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.61 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.61 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SEPTIN7P14]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SEC61A2]] | -0.55 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SACM1L]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ZDHHC20]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ABHD12]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises ABL2's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.11× lower at baseline in the lines without PDCD1LG2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[FRMD6]] | B | FRMD6 activity raises ABL2's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.54× lower at baseline in the lines without FRMD6 | 0.007 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[NAV3]] | B | NAV3 activity raises ABL2's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without NAV3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[ADTRP]] | B | ADTRP activity raises ABL2's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.00× lower at baseline in the lines without ADTRP | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[LINC02057]] | B | LINC02057 activity raises ABL2's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.86× lower at baseline in the lines without LINC02057 | 0.026 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[DNAH11]] | B | DNAH11 activity raises ABL2's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without DNAH11 | 0.040 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[CCDC71L]] | B | CCDC71L activity raises ABL2's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 2.32× lower at baseline in the lines without CCDC71L | 0.044 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[GLIPR1]] | B | GLIPR1 activity raises ABL2's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without GLIPR1 | 0.047 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent |
| [[CCN1]] | B | CCN1 activity raises ABL2's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 2.52× lower at baseline in the lines without CCN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[ETS1]] | B | ETS1 activity raises ABL2's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 2.31× lower at baseline in the lines without ETS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[TOP2A]] | B | TOP2A activity raises ABL2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HRH1]] | B | HRH1 activity raises ABL2's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without HRH1 | 0.073 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.7, 5.7); signed map (12.5, 40.1). **Vector** length 126, 51.0% of its response variance represented; |z| ≥ 3 in 1,743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Peretinoin (drug)]] 5 µM |  | +7.8 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.5 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +16.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +1.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -6.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.7 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -5.3 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.7 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -3.2 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.7 | +0.3 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | -2.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ABL proto-oncogene 2, non-receptor tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:179,099,330-179,229,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARG; previously ABLL |
| Gene groups (HGNC) | SH2 domain containing; Abl family tyrosine kinases; SH3 domain containing |
| Reactome | 12 pathways, smallest: Role of ABL in ROBO-SLIT signaling; Negative regulation of FLT3; FLT3 Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P42684](https://www.uniprot.org/uniprotkb/P42684) (Tyrosine-protein kinase ABL2):

> Non-receptor tyrosine-protein kinase that plays an ABL1-overlapping role in key processes linked to cell growth and survival such as cytoskeleton remodeling in response to extracellular stimuli, cell motility and adhesion and receptor endocytosis. Coordinates actin remodeling through tyrosine phosphorylation of proteins controlling cytoskeleton dynamics like MYH10 (involved in movement); CTTN (involved in signaling); or TUBA1 and TUBB (microtubule subunits). Binds directly F-actin and regulates …

**Summary**, from NCBI Gene [27](https://www.ncbi.nlm.nih.gov/gene/27):

> This gene encodes a member of the Abelson family of nonreceptor tyrosine protein kinases. The protein is highly similar to the c-abl oncogene 1 protein, including the tyrosine kinase, SH2 and SH3 domains, and it plays a role in cytoskeletal rearrangements through its C-terminal F-actin- and microtubule-binding sequences. This gene is expressed in both normal and tumor cells, and is involved in translocation with the ets variant 6 gene in leukemia. Multiple alternatively spliced transcript …

**Accessions** — [HGNC:77](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:77) · Entrez [27](https://www.ncbi.nlm.nih.gov/gene/27) · UniProt [P42684](https://www.uniprot.org/uniprotkb/P42684) · Ensembl [ENSG00000143322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143322)

## Data

Gene col 6714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6714); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6714]; `tensor/DDL_lfc|DDL_z.npy` [6714]; `embed/gene_vectors.npy` [6714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6714 or target_col == 6714). Every well: [[ABL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
