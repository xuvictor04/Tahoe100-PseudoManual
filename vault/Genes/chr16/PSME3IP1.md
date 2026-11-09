---
symbol: "PSME3IP1"
type: "gene"
col: 10294
ensembl_id: "ENSG00000172775"
name: "proteasome activator subunit 3 interacting protein 1"
location: "16q13"
module: 148
arm: "+"
pooled_cpm: 54.97
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# PSME3IP1

*proteasome activator subunit 3 interacting protein 1* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +24.3, q 0e+00, up in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +15.6, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.669× (z -10.6, q 2e-23, down in 35 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.761× (z -10.1, q 1e-21, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS52]] (+0.82, fdr 7e-06), [[ZMPSTE24]] (+0.77, fdr 7e-06), [[ZMYND11]] (+0.74, fdr 9e-06); moves opposite to [[CARHSP1]] (-0.73, fdr 7e-06), [[RPL18]] (-0.70, fdr 3e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[TNNI3]] (-0.69, fdr 1e-05), [[SLC27A1]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[C8orf33]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +24.3 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +22.7 | 0e+00 | 39/43 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +15.6 | 0e+00 | 39/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +14.9 | 0e+00 | 35/45 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +9.0 | 2e-17 | 36/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +7.6 | 2e-12 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.2 | 4e-08 | 27/48 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +6.0 | 1e-07 | 26/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +5.6 | 2e-06 | 21/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +5.4 | 3e-06 | 23/48 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.24×** | +5.4 | 4e-06 | 27/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +5.0 | 2e-05 | 21/48 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.7 | 1e-04 | 18/48 (NCI-H2030, A549, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.7 | 1e-04 | 19/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 15/47 (C32, LS 180, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +4.1 | 0.002 | 14/48 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.046 | 5/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.052 | 8/47 (RPMI-7951, NCI-H23, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.052 | 17/47 (NCI-H460, J82, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -10.6 | 2e-23 | 35/47 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.761×** | -10.1 | 1e-21 | 41/48 (HT-29, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.683×** | -10.0 | 3e-21 | 35/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -9.6 | 8e-20 | 37/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.713×** | -8.9 | 9e-17 | 31/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -8.8 | 9e-17 | 29/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.720×** | -8.6 | 5e-16 | 34/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.733×** | -8.2 | 2e-14 | 37/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -8.1 | 3e-14 | 32/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.776×** | -6.7 | 2e-09 | 27/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.804×** | -5.7 | 6e-07 | 25/48 (J82, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -4.2 | 0.001 | 17/48 (J82, NCI-H1792, …) | rises with dose |  |
| [[Gallic acid (drug)]] 5 µM |  | 0.907× | -3.6 | 0.013 | 2/48 (NCI-H1792, H4) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.871× | -3.6 | 0.013 | 12/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.913× | -3.4 | 0.029 | 4/48 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.883× | -3.3 | 0.040 | 14/48 (Hs 766T, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.842× | -3.2 | 0.043 | 9/48 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.801×** | -3.0 | 0.072 | 5/48 (SW 900, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 72.7 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +8.7) | — |
| [[SW480 (line)]] | alt | 70.3 | 3 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.478× (z -10.9) |
| [[SNU-423 (line)]] | alt | 42.3 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 56.8 | 4 (2 ⚠) | 1 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.70× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -10.0) |
| [[HOP62 (line)]] | alt | 44.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 58.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +9.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.466× (z -9.2) |
| [[LS 180 (line)]] | wt | 46.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +11.4) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.418× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 88.7 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.476× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.508× (z -9.1) |
| [[PANC-1 (line)]] | alt | 43.5 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.523× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 58.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.09× (z +17.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 54.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 45.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 37.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.4) | — |
| [[J82 (line)]] | alt | 63.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.441× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 61.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 28.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.1) | — |
| [[A-172 (line)]] | wt | 65.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 76.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +13.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 35.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.6) | — |
| [[LoVo (line)]] | wt | 53.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.503× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 47.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 64.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 36.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 43.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +10.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 48.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 50.7 | 0 | 2 | — | [[Flutamide (drug)]] 0.5 µM 0.0745× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +8.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 45.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 65.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +11.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -12.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 61.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +10.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 59.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 74.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 61.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS52]] | +0.82 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[ZMPSTE24]] | +0.77 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ZMYND11]] | +0.74 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[MTHFSD]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[CLHC1]] | +0.71 | +0.67 / +0.39 | both halves | 6e-05 |  |
| [[PBLD]] | +0.70 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[C8orf33]] | +0.70 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[ARFGAP2]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MCTS1]] | +0.69 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[MAGOHB]] | +0.69 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[DECR1]] | +0.69 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARHSP1]] | -0.73 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | -0.70 | -0.46 / -0.67 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TNNI3]] | -0.69 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.69 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[RPS5]] | -0.69 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | -0.68 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.68 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[MAST3]] | -0.67 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[YIF1B]] | -0.67 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ELOB]] | -0.67 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[PEDS1]] | -0.67 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[RNF114]] | -0.67 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TOMM20]] | -0.66 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PSME3IP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NOVA2]] | B | NOVA2 activity raises PSME3IP1's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.14× lower at baseline in the lines without NOVA2 | 0.014 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PSME3IP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PSME3IP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers PSME3IP1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C8orf33]] | C | PSME3IP1's natural level strengthens C8orf33's drug response | PSME3IP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse -0.08; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.831). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-5.8, 3.5); signed map (16.8, -28.4). **Vector** length 113, 29.3% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +24.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +22.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +15.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.0 | -10.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.8 | -8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.6 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.6 | -8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | proteasome activator subunit 3 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:57,152,466-57,186,116 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NIP30, PIP30; previously C16orf94, FAM192A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZU8](https://www.uniprot.org/uniprotkb/Q9GZU8) (PSME3-interacting protein):

> Promotes the association of the proteasome activator complex subunit PSME3 with the 20S proteasome and regulates its activity. Inhibits PSME3-mediated degradation of some proteasome substrates, probably by affecting their diffusion rate into the catalytic chamber of the proteasome. Also inhibits the interaction of PSME3 with COIL, inhibits accumulation of PSME3 in Cajal bodies and positively regulates the number of Cajal bodies in the nucleus.

**Summary**, from NCBI Gene [80011](https://www.ncbi.nlm.nih.gov/gene/80011):

> Involved in negative regulation of proteasomal protein catabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29856) · Entrez [80011](https://www.ncbi.nlm.nih.gov/gene/80011) · UniProt [Q9GZU8](https://www.uniprot.org/uniprotkb/Q9GZU8) · Ensembl [ENSG00000172775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172775)

## Data

Gene col 10294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10294); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10294]; `tensor/DDL_lfc|DDL_z.npy` [10294]; `embed/gene_vectors.npy` [10294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10294 or target_col == 10294). Every well: [[PSME3IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSME3IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
