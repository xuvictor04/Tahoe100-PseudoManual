---
symbol: "CDKN1B"
type: "gene"
col: 3215
ensembl_id: "ENSG00000111276"
name: "cyclin dependent kinase inhibitor 1B"
location: "12p13.1"
module: 130
arm: "+"
pooled_cpm: 36.92
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 34
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# CDKN1B

*cyclin dependent kinase inhibitor 1B* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +16.1, q 0e+00, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.89× (z +15.3, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.328× (z -20.4, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.589× (z -9.7, q 2e-20, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO8]] (+0.73, fdr 7e-06), [[ACBD5]] (+0.71, fdr 7e-06), [[CCNG2]] (+0.67, fdr 7e-06); moves opposite to [[ANKS6]] (-0.64, fdr 1e-05), [[MPP3]] (-0.64, fdr 8e-06), [[TMEM241]] (-0.63, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[H2AJ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.86×** | +16.1 | 0e+00 | 36/47 (J82, HEC-1-A, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.89×** | +15.3 | 0e+00 | 46/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.1 | 1e-13 | 30/48 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +6.6 | 7e-09 | 30/48 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +6.3 | 4e-08 | 28/47 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.0 | 2e-07 | 22/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +5.4 | 7e-06 | 22/47 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.32×** | +5.2 | 2e-05 | 25/46 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 3e-05 | 23/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 6e-05 | 24/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +4.9 | 6e-05 | 18/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +4.6 | 2e-04 | 22/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 18/47 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.33×** | +4.3 | 9e-04 | 22/47 (A-427, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 19/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.002 | 19/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 20/48 (J82, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.005 | 15/48 (C32, KATO III, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.030 | 17/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3215.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.328×** | -20.4 | 0e+00 | 47/48 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.333×** | -20.2 | 0e+00 | 44/48 (NCI-H2347, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.433×** | -15.4 | 0e+00 | 43/48 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.516×** | -12.1 | 1e-31 | 39/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.567×** | -10.4 | 2e-23 | 35/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.575×** | -9.8 | 1e-20 | 27/39 (SW1417, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.589×** | -9.7 | 2e-20 | 38/48 (Panc 03.27, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.665×** | -7.5 | 5e-12 | 29/45 (HCT15, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.483×** | -7.0 | 2e-10 | 30/48 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.524×** | -6.2 | 3e-08 | 27/48 (HT-29, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -5.6 | 9e-07 | 2/49 (AN3 CA, SW 1088) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -5.6 | 9e-07 | 25/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.742×** | -5.5 | 2e-06 | 25/47 (SW 900, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.731×** | -5.4 | 3e-06 | 28/48 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.750×** | -5.3 | 5e-06 | 23/48 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.579×** | -5.2 | 5e-06 | 24/47 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.769×** | -4.6 | 1e-04 | 20/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.789×** | -4.3 | 4e-04 | 22/48 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.784×** | -4.3 | 5e-04 | 19/48 (A498, NCI-H2030, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.645×** | -4.2 | 6e-04 | 20/46 (SNU-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.645×** | -4.2 | 6e-04 | 21/48 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -4.0 | 0.001 | 20/48 (NCI-H2347, SW1417, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.857× | -4.0 | 0.001 | 20/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.678×** | -3.7 | 0.004 | 20/47 (A498, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Acetohexamide (drug)]] 5 µM |  | 0.879× | -3.3 | 0.016 | 11/48 (HEC-1-A, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 44.9 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.52× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -15.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -9.1) |
| [[LoVo (line)]] | wt | 63.4 | 4 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 68.3 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.82× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.249× (z -14.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 58.4 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -9.8) |
| [[BT-474 (line)]] | alt | 58.7 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -15.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -17.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.552× (z -8.5) |
| [[A549 (line)]] | wt | 38.8 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.35× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.236× (z -12.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 40.8 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 15.7× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.0994× (z -13.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 35.3 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.62× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 27.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +18.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 63.3 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 67.2 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.266× (z -11.4) |
| [[PANC-1 (line)]] | alt | 19.8 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.24× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.367× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 30.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW1417 (line)]] | alt | 53.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW480 (line)]] | alt | 37.8 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.64× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.313× (z -12.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 35.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.98× (z +9.2) | — |
| [[A498 (line)]] | wt | 39.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.370× (z -9.0) |
| [[HCT15 (line)]] | alt | 62.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0845× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.258× (z -9.7) |
| [[KATO III (line)]] | alt | 43.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.0) ⚠ cell-cycle shift, explains ~25% of this change | [[Panobinostat (drug)]] 5 µM 0.262× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 39.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +10.4) ⚠ position not correctable · without an alert: [[TAK-901 (drug)]] 5 µM 13.3× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -11.9) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 21.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -9.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -8.5) |
| [[C-33 A (line)]] | alt | 50.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 39.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -9.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[CHP-212 (line)]] | wt | 60.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -9.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +15.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Hs 766T (line)]] | wt | 40.0 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0617× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.336× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0647× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[RKO (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW 1271 (line)]] | alt | 48.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0754× (z -8.8) |
| [[SW48 (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +9.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO8]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ACBD5]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CCNG2]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 570 |
| [[APOLD1]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 | ⚠ same locus (3.5 kb, same strand: neighbours can correlate without regulation) |
| [[C3orf38]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CILK1]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[DNAJC27]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TRMT1L]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ATP23]] | +0.63 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[NBR1]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[ATOSA]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[CDKN2C]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 956 |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS6]] | -0.64 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[MPP3]] | -0.64 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[TMEM241]] | -0.63 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[LYPLA1]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TANGO6]] | -0.62 | -0.60 / -0.71 | both halves | 7e-06 |  |
| [[PPM1F]] | -0.62 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SEH1L]] | -0.61 | -0.65 / -0.57 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[LMBR1]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[NCLN]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[DFFA]] | -0.60 | -0.48 / -0.64 | both halves | 2e-05 | pathway: HALLMARK_APOPTOSIS |
| [[RNGTT]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ACOT7]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[H2AJ]] | B | H2AJ activity raises CDKN1B's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without H2AJ | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CDKN1B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[DHRS3]] | B | DHRS3 activity strengthens CDKN1B's drug response | lines that do not express DHRS3 (13) vs lines expressing it (36) | the lines without DHRS3 respond 0.69× as strongly (z diff +0.95); strongest at Belinostat 5 µM: 0.60x vs 0.41x (z diff +2.6) | 0.063 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2; target measured in part of the lines; the reference differs; artifact flags |
| [[GATA6]] | B | GATA6 activity strengthens CDKN1B's drug response | lines that do not express GATA6 (18) vs lines expressing it (31) | the lines without GATA6 respond 0.79× as strongly (z diff +0.85); strongest at Auranofin 5 µM: 0.67x vs 0.48x (z diff +2.7) | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.5, -27.0); signed map (12.5, -13.5). **Vector** length 135, 41.2% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.2 | +15.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +8.4 | +16.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +6.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.7 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.2 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +5.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.4 | -12.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.1 | -20.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.8 | -10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.2 | -20.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -9.7 |
|  | [[EX229 (drug)]] 5 µM |  | -5.5 | -7.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase inhibitor 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:12,685,498-12,722,369 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIP1, P27KIP1 |
| Gene groups (HGNC) | Cyclin dependent kinase inhibitor 1 family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, UV_RESPONSE_DN, APOPTOSIS, HYPOXIA, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 47 pathways, smallest: PTK6 Regulates Cell Cycle; TP53 Regulates Transcription of Genes Involved in G1 Cell Cycle Arrest; AKT phosphorylates targets in the cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P46527](https://www.uniprot.org/uniprotkb/P46527) (Cyclin-dependent kinase inhibitor 1B):

> Important regulator of cell cycle progression. Inhibits the kinase activity of CDK2 bound to cyclin A, but has little inhibitory activity on CDK2 bound to SPDYA. Involved in G1 arrest. Potent inhibitor of cyclin E- and cyclin A-CDK2 complexes. Forms a complex with cyclin type D-CDK4 complexes and is involved in the assembly, stability, and modulation of CCND1-CDK4 complex activation. Acts either as an inhibitor or an activator of cyclin type D-CDK4 complexes depending on its phosphorylation …

**Summary**, from NCBI Gene [1027](https://www.ncbi.nlm.nih.gov/gene/1027):

> This gene encodes a cyclin-dependent kinase inhibitor, which shares a limited similarity with CDK inhibitor CDKN1A/p21. The encoded protein binds to and prevents the activation of cyclin E-CDK2 or cyclin D-CDK4 complexes, and thus controls the cell cycle progression at G1. The degradation of this protein, which is triggered by its CDK dependent phosphorylation and subsequent ubiquitination by SCF complexes, is required for the cellular transition from quiescence to the proliferative state. …

**Accessions** — [HGNC:1785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1785) · Entrez [1027](https://www.ncbi.nlm.nih.gov/gene/1027) · UniProt [P46527](https://www.uniprot.org/uniprotkb/P46527) · Ensembl [ENSG00000111276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111276)

## Data

Gene col 3215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3215); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3215]; `tensor/DDL_lfc|DDL_z.npy` [3215]; `embed/gene_vectors.npy` [3215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3215 or target_col == 3215). Every well: [[CDKN1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
