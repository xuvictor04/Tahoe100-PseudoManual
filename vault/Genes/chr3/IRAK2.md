---
symbol: "IRAK2"
type: "gene"
col: 5506
ensembl_id: "ENSG00000134070"
name: "interleukin 1 receptor associated kinase 2"
location: "3p25.3"
module: 112
arm: "+"
pooled_cpm: 83.46
n_lines_expressing: 42
n_dd_up: 21
n_dd_down: 38
n_dd_up_clean: 18
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 17
direction_downstream: 0
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# IRAK2

*interleukin 1 receptor associated kinase 2* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 3.38× (z +19.0, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.428× (z -19.3, q 0e+00, down in 36 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIE]] (+0.70, fdr 7e-06), [[IL1A]] (+0.65, fdr 7e-06), [[EBI3]] (+0.64, fdr 1e-05); moves opposite to [[GHITM]] (-0.51, fdr 4e-05), [[CLCC1]] (-0.50, fdr 4e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[CSF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **3.38×** | +19.0 | 0e+00 | 37/40 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +16.7 | 0e+00 | 30/40 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **5.54×** | +14.5 | 3e-45 | 39/41 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.97×** | +11.0 | 4e-26 | 29/40 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.7 | 2e-20 | 27/40 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +8.8 | 2e-16 | 30/40 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +8.2 | 2e-14 | 28/39 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +8.0 | 1e-13 | 28/40 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +6.7 | 1e-09 | 32/40 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +6.4 | 7e-09 | 24/40 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 6e-06 | 21/40 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 9e-04 | 20/39 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 16/40 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 15/41 (MIA PaCa-2, A-172, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +3.6 | 0.014 | 17/40 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.018 | 16/39 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.019 | 17/40 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bexarotene (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.021 | 13/40 (HOP62, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.428×** | -19.3 | 0e+00 | 36/41 (HS-578T, A549, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -13.0 | 6e-36 | 28/33 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.514×** | -10.3 | 1e-22 | 37/40 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.538×** | -10.0 | 3e-21 | 32/40 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.323×** | -9.5 | 2e-19 | 35/39 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.626×** | -7.5 | 5e-12 | 32/40 (HS-578T, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.702×** | -6.9 | 4e-10 | 32/40 (A549, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.730×** | -6.2 | 3e-08 | 29/40 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -6.1 | 8e-08 | 26/40 (SNU-423, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.745×** | -6.0 | 1e-07 | 27/42 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.690×** | -5.9 | 1e-07 | 30/41 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.694×** | -5.8 | 2e-07 | 26/39 (HEC-1-A, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.755×** | -5.7 | 6e-07 | 26/41 (A498, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -5.5 | 2e-06 | 4/41 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.521×** | -5.5 | 2e-06 | 24/36 (A549, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.701×** | -5.3 | 5e-06 | 24/40 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.725×** | -5.2 | 9e-06 | 21/40 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.728×** | -5.1 | 1e-05 | 22/40 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -5.0 | 2e-05 | 23/40 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 279 | 2 | 13 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.86× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -21.6) |
| [[A-172 (line)]] | wt | 83.9 | 9 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.1) |
| [[SNU-423 (line)]] | alt | 283 | 6 (1 ⚠) | 7 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.50× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 38.0 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 171 | 6 | 4 | [[Harringtonine (drug)]] 5 µM 4.51× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -22.5) |
| [[NCI-H1573 (line)]] | alt | 58.2 | 4 (1 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.85× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +9.6) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.150× (z -13.8) |
| [[A498 (line)]] | wt | 94.5 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +20.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 88.5 | 3 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.91× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.0) |
| [[HOP62 (line)]] | alt | 172 | 3 | 5 | [[Harringtonine (drug)]] 5 µM 7.32× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 250 | 4 (1 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.12× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0963× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 142 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 130 | 4 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.67× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.0964× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 94.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +17.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 79.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 52.9 | 5 | 0 | [[Harringtonine (drug)]] 5 µM 4.20× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 135 | 1 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.38× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 109 | 3 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.28× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -17.2) |
| [[J82 (line)]] | alt | 93.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.6) |
| [[LS 180 (line)]] | wt | 37.0 | 2 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.44× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -8.7) |
| [[Hs 766T (line)]] | wt | 148 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.84× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -16.1) |
| [[LoVo (line)]] | wt | 27.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 146 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.71× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 50.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -10.0) |
| [[SW1417 (line)]] | alt | 43.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.9) | — |
| [[A-427 (line)]] | wt | 23.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.0) | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -13.2) |
| [[COLO 205 (line)]] | alt | 77.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -13.3) |
| [[H4 (line)]] | wt | 31.0 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.46× (z +8.8) | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -11.0) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 48.4 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.37× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 89.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 153 | 0 | 2 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0719× (z -10.5) |
| [[SW 1271 (line)]] | alt | 300 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0526× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -12.7) |
| [[SHP-77 (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 47.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.1) | — |
| [[SW480 (line)]] | alt | 39.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.1) |
| [[AN3 CA (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.82 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIE]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 | STRING 457 |
| [[IL1A]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 876 |
| [[EBI3]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[FAM43A]] | +0.64 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[CD82]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[IER3]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[G0S2]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[TRAF1]] | +0.61 | +0.51 / +0.68 | both halves | 1e-05 | STRING 671 |
| [[EPHB2]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[MIR3142HG]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CXCL8]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 644 |
| [[ARL4C]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GHITM]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[CLCC1]] | -0.50 | -0.51 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSF2]] | B | CSF2 activity raises IRAK2's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.94× lower at baseline in the lines without CSF2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[C1QTNF1]] | B | C1QTNF1 activity raises IRAK2's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without C1QTNF1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[MTSS1]] | B | MTSS1 activity raises IRAK2's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without MTSS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[HMGN2P46]] | B | HMGN2P46 activity raises IRAK2's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.81× lower at baseline in the lines without HMGN2P46 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[MAP2K1]] | B | MAP2K1 activity raises IRAK2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds |
| [[ITGA1]] | B | ITGA1 activity raises IRAK2's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.26× lower at baseline in the lines without ITGA1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[CXCL8]] | B | CXCL8 activity raises IRAK2's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without CXCL8 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[CD82]] | B | CD82 activity raises IRAK2's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without CD82 | 0.049 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[MIR3142HG]] | B | MIR3142HG activity raises IRAK2's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without MIR3142HG | 0.062 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[ICAM1]] | B | ICAM1 activity raises IRAK2's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without ICAM1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[TRIB1]] | B | TRIB1 activity raises IRAK2's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.84× lower at baseline in the lines without TRIB1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[IL1B]] | B | IL1B activity raises IRAK2's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.39× lower at baseline in the lines without IL1B | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.0, 0.8); signed map (1.9, 43.4). **Vector** length 128, 41.5% of its response variance represented; |z| ≥ 3 in 1,509 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.55 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.58 to 5); *KRAS signaling up* (hallmark, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +10.4 | +19.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +16.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.9 |
| fall | [[NG25 (drug)]] 5 µM |  | -8.4 | -9.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.5 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.6 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor associated kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:10,164,919-10,243,745 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Interleukin 1 receptor associated kinase family |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 39 pathways, smallest: IRAK2 mediated activation of TAK1 complex; IRAK2 mediated activation of TAK1 complex upon TLR7/8 or 9 stimulation; TRAF6-mediated induction of TAK1 complex within TLR4 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O43187](https://www.uniprot.org/uniprotkb/O43187) (Interleukin-1 receptor-associated kinase-like 2):

> Binds to the IL-1 type I receptor following IL-1 engagement, triggering intracellular signaling cascades leading to transcriptional up-regulation and mRNA stabilization.

**Summary**, from NCBI Gene [3656](https://www.ncbi.nlm.nih.gov/gene/3656):

> IRAK2 encodes the interleukin-1 receptor-associated kinase 2, one of two putative serine/threonine kinases that become associated with the interleukin-1 receptor (IL1R) upon stimulation. IRAK2 is reported to participate in the IL1-induced upregulation of NF-kappaB. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6113) · Entrez [3656](https://www.ncbi.nlm.nih.gov/gene/3656) · UniProt [O43187](https://www.uniprot.org/uniprotkb/O43187) · Ensembl [ENSG00000134070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134070)

## Data

Gene col 5506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5506); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5506]; `tensor/DDL_lfc|DDL_z.npy` [5506]; `embed/gene_vectors.npy` [5506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5506 or target_col == 5506). Every well: [[IRAK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRAK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
